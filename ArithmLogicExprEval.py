# Arithmetic and logical expression evaluation post processing script
#
# Author:   Mika Schmitt
# Date:     February 14, 2024
# Modified: 
# License: You may use, distribute and modify this code under the terms of the LGPLv3 license.

import re #To perform the search and replace.

from ..Script import Script

class ArithmicEval(Script):

    def getSettingDataString(self):
        return """{
            "name": "Arithmetic and logical expression evaluation",
            "key": "ArithmLogicExprEval",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "EvalComment":
                {
                    "label": "Evaluate Comments",
                    "description": "Expressions in Comments will be evaluated.",
                    "type": "bool",
                    "default_value": false
                },
                "BoolRep":
                {
                    "label": "Boolean Representation",
                    "description": "Choose how booleans are represented.",
                    "type": "enum",
                    "options": {
                        "binary": "Binary ( 1  or 0 )",
                        "text": "Text (True or False)"
                    },
                    "default_value": "Binary"
                }

        }"""

    def execute(self, data):
        # Define regex for finding arithmetic expressions
        # Matches Semicolons and Expressions
        RegExPattern = "(;|[\d()+\-*/%<>&!=|~:. ]+[()+\-*/%<>&!=|~:]+[\d()+\-*/%<>&!=|~:. ]+)"
        RegExObj = re.compile(RegExPattern)

        # should comments be evaluated?
        EvalComments = self.getSettingValueByKey("EvalComment")

        # how should booleans be represented
        BoolRepresentation = self.getSettingValueByKey("BoolRep")

        for layer_number, layer in enumerate(data):
            lines = layer.split("\n")
            for line_number, line in enumerate(lines):
                
                # find arithmetic and logical expression
                snippets = re.split(RegExObj, line)

                # there are no expressions
                if(len(snippets) == 1):
                    break

                # evaluate arithmetic and logical expression
                for snippet_number, snippet in enumerate(snippets):

                    # is expression or comment
                    if(re.fullmatch(RegExObj, snippet) != None):
                        
                        # the following is a comment
                        if(snippet == ";"):
                            if(EvalComments):
                                continue
                            break
                        
                        # evaluate expression
                        result = eval(snippet)

                        # is boolean
                        if(isinstance(result), (bool)):
                            # should be binary representation
                            if(BoolRepresentation == "binary"):
                                result = int(result)

                        snippets[snippet_number] = result

                lines[line_number] = snippets
                    
            new_layer = "\n".join(lines)
            data[layer_number] = new_layer

        return data