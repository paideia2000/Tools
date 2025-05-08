import unittest



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
        

if __name__=="__main__":
    unittest.main()