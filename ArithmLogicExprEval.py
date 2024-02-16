# Arithmetic and logical expression evaluation post processing script
#
# Author:   Mika Schmitt
# Date:     February 14, 2024
# Modified: February 15, 2024
# License:  You may use, distribute and modify this code under the terms of the GNU LGPL v2.1 license.

import re #To perform the search and replace.
import math

from ..Script import Script

class ArithmLogicExprEval(Script):

    def getSettingDataString(self):
        return """{
            "name": "Arithmetic And Logical Expression Evaluation",
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
                    "default_value": "binary"
                }
            }

        }"""

    def execute(self, data):       
        RegExPattern = (# Detect Comments
                        "(?:;"
                        # Detect arithmetic expressions                                                   
                        "|[\d()]+[\d.+\-*/%() ]*[+\-*/%][\d.+\-*/%() ]*[\d()]+"
                        # Detect logical expressions
                        "|[\d\w.=!<>&|^~' ]*[=!<>&|^~][\d\w.=!<>&|^~' ]+"
                        # Detect mathematical functions
                        "|[\d.+\-*/%() ]*math\.[a-z\d]+\(.+\)[\d.+\-*/%() ]*)+"
        )
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
                    continue

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
                        if(type(result) == bool):
                            # should be binary representation
                            if(BoolRepresentation == "binary"):
                                result = int(result)

                        snippets[snippet_number] = str(result) + " "

                lines[line_number] = "".join(snippets)               

            new_layer = "\n".join(lines)
            data[layer_number] = new_layer

        return data
