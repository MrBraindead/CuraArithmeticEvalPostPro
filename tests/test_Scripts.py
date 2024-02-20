# usage: PS > python3 -m CuraArithmeticEvalPostPro.tests.test_Scripts 

import unittest

# import Scripts
import ArithmLogicExprEval

class Test_ArithmLogicExprEval(unittest.TestCase):

    def test_RegEx(self):
        self.assertEqual(ArithmLogicExprEval.ArithmLogicExprEval.execute(self, "F(10*20* math.sin(0) *20*math.cos(3*3.141)*30*math.sin(10))"), "F0")