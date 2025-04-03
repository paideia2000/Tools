from unittest.mock import patch 
import unittest
from work_DB import load_data_dataset, dump_user_file

class Test_load_data_dataset(unittest.TestCase):
    
    @patch("work_DB.pck.load")
    @patch("work_DB.open", create=True)
    def test_load_data_dataset(self, mock_open, mock_pck_load):
        """ check that function returned a lis """
        PATH = "sqlite3/data.bin"
        
        #simulate, the value return will be a list of tuple
        lis_of_tuple  = [(1,"rene")]
        mock_pck_load.return_value = lis_of_tuple
        
        get_list = load_data_dataset(PATH)
        self.assertIsInstance(get_list, list)


if __name__=="__main__":
    unittest.main()