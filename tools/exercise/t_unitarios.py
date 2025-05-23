import unittest
from io import StringIO
from unittest.mock import patch


class Test_ex_1(unittest.TestCase):
    
    def test_returned_int(self):
        """ The function ex_1 must be returned a integer """
        from ex_1 import sum_numb_list
        
        argument = list(range(1,20))
        
        result: int = sum_numb_list(argument)
        
        self.assertIsInstance(result, int)

    def test_returned_Valuerror(self):
        """  """
        from ex_1 import sum_numb_list
        
        argument = "renne"

        with self.assertRaises(ValueError) as vl:
            result = sum_numb_list(argument)
            
            self.assertIsInstance(vl, str)

class Test_Anagrama(unittest.TestCase):

    def test_returned_str(self):
        """ check if the function retuner a str """
        from anagrama import check_if_anagrama
        
        result = check_if_anagrama("amor")
        
        self.assertIsInstance(result,str)
        
    def test_returned_ValueError(self):
        """ chek if the function returner error when ani characters is not alphabetic o the funtion take a arguments empty"""
        from anagrama import check_if_anagrama
        
    
        with self.assertRaises(ValueError):
            
            self.assertEqual(check_if_anagrama(""), "ERROR: Please check the content of the varibales")
            self.assertEqual(check_if_anagrama("am3or", "ERROR: The word contain other character taht is not alphabetic."))

class Test_fibonacci(unittest.TestCase):
    
    def test_returned_int(self):
        """ check if the function returned a interger value """

        from fibonacci import suce_fibonacci
        
        self.assertIsInstance(suce_fibonacci(20), int)
    
    def test_returned_TypeError(self):
        """ chek if the function returner typerror if not take the argument whit a number insite the variable"""
        from fibonacci import suce_fibonacci
        
        with self.assertRaises(TypeError):
            
            self.assertEqual(suce_fibonacci(""), "ERROR: Please check the content of the varibales")



class Test_Fcatorial_Recursive(unittest.TestCase):
    from factorial_recursive import factorial
    
    @patch("factorial_recursive.factorial")
    def test_returned_a_number(self, fake_function):
        """ check that function retorned a number """
        
        fake_function.return_value = 120
        
        result = fake_function(5)
        
        self.assertIsInstance(result, int)
    
    @patch("factorial_recursive.factorial")
    def test_returned_ValueError(self, fake_function):
        """ the function must be retorned a ValueError """
        
        fake_function.side_effect = ValueError('ERROR: You must insert a numbers.')
        
        with self.assertRaises(ValueError) as context:
            fake_function("")

        self.assertEqual(str(context.exception), 'ERROR: You must insert a numbers.')
        


if __name__=="__main__":
    unittest.main()