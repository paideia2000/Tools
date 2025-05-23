import unittest
import time
from unittest.mock import patch
from main import get_data_CREATETABLE

class TestGet_data_CREATETABLE(unittest.TestCase):

    @patch("builtins.input")
    def test_return_str(self, mock_input):
        """Should return the name table when asking for table name"""
        
        #Mock configuration
        table_name = "customers"
        mock_input.return_value = table_name
        
        result: str = get_data_CREATETABLE()
        
        #execute test
        self.assertIsInstance(result, str)
        self.assertAlmostEqual(result, table_name)
        mock_input.assert_called_once_with("\nEnter the name of the table to create: ")
    
if __name__=="__main__":
    unittest.main()
