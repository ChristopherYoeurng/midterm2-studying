# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):

#postfix tests
    def test_postfix_eval_01(self):
        #test simple operations 
        self.assertAlmostEqual(postfix_eval("3  5 +"), 8)
        self.assertAlmostEqual(postfix_eval("2 3 * 4 *"), 24)
        self.assertAlmostEqual(postfix_eval("2 3 /    4 /"), 0.1666666666)
        self.assertAlmostEqual(postfix_eval("2 10 - 14 -"), -22)
        self.assertAlmostEqual(postfix_eval("10 3 >> 5 <<"), 32)
        self.assertAlmostEqual(postfix_eval("80 1 >> 2   >>"), 10)
        self.assertAlmostEqual(postfix_eval("2  -1 +"), 1)
        self.assertAlmostEqual(postfix_eval("18.0 -3 -"), 21.0)
        self.assertAlmostEqual(postfix_eval("2 2 /"), 1.0)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
    
    def test_right_associativity(self):
        self.assertAlmostEqual(postfix_eval('2 3 1  2 2 ** ** **  **'), 8)
        self.assertNotAlmostEqual(postfix_eval('2 3 1 2 2 **  ** ** **'), 4096)

    def test_eval_exceptions(self): 
        #test empty string
        try:
            postfix_eval("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Empty input")
        
        #test insufficient operands
        try:
            postfix_eval("3 2 + -")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

        #test insufficient operands with exponentiation
        try:
            postfix_eval("3 2 1 3 4 ** ** ** ** **")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

        #test too many operands
        try:
            postfix_eval("1 2 + 2 + 3")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

        #test illegal bit shift operand 
        try:
            postfix_eval("3 3 / 1 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
        try:
            postfix_eval("3 3 / 1 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

        #test 0 divisor exception 
        with self.assertRaises(ValueError): 
            postfix_eval("1 1 + 0 /")

#infix tests 
    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix(""), "")
        self.assertEqual(infix_to_postfix("3 * -3 - 20"), "3 -3 * 20 -")
        self.assertEqual(infix_to_postfix("3 *  ( -3 -   20 )"), "3 -3 20 - *")
        self.assertEqual("3 2 >> 8 >> 3 / 17 12 4.2 / 1.2 8 << / 6 * << * 6.9 17 23 >> * 6 2.2 << / 3.2 << 56 21 / 1.4 * << 2.3 >> 4.1 * *", infix_to_postfix("( 3 >> 2 ) >> 8 / 3 * 17 << ( 12 / 4.2 / 1.2 << 8 * 6 ) * ( ( 6.9 * 17 >> 23 / 6 << 2.2 ) << 3.2 << ( 56 / 21 * 1.4 ) >> 2.3 * 4.1 )"))

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("3 >> 4 >> 5 + 6 * 7"), "3 4 >> 5 >> 6 7 * +")
        self.assertEqual(infix_to_postfix("3 >> 2 ** 2 + 14 * 3"), "3 2 >> 2 ** 14 3 * +")
    
    def test_infix_repeated_operators(self):
        self.assertEqual(infix_to_postfix("2 + 3 + 2 + 4 + 3"), '2 3 + 2 + 4 + 3 +')
        self.assertEqual(infix_to_postfix("2 * 2 * 2 * 2 / 2 / 3 / 1 / 7"), "2 2 * 2 * 2 * 2 / 3 / 1 / 7 /")
    
    def test_infix_right_associativity(self):
        self.assertEqual(infix_to_postfix('2 ** 3 ** 1 ** 2 ** 2'), '2 3 1 2 2 ** ** ** **')
        self.assertEqual(infix_to_postfix("2 + 3 ** 2 ** 2 / 3"), "2 3 2 2 ** ** 3 / +")

#prefix tests         
    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("* + 3 1 + 2 4"), "3 1 + 2 4 + *")
        self.assertEqual(prefix_to_postfix("+ 2 >> << 3 4 8"), "2 3 4 << 8 >> +")
        self.assertEqual(prefix_to_postfix("+ -1 2"), "-1 2 +")
        self.assertEqual(prefix_to_postfix("+ -1 2.0"), "-1 2.0 +")

#tests the interaction on functions 
    def test_cross_use(self):
        self.assertEqual(infix_to_postfix("2 ** 3 ** 2"), '2 3 2 ** **')
        self.assertEqual(postfix_eval(infix_to_postfix("2 ** 3 ** 2")), 512)
        self.assertEqual(prefix_to_postfix("**  2 **    3 2"), infix_to_postfix("2 ** 3 ** 2"))

if __name__ == "__main__":
    unittest.main()
