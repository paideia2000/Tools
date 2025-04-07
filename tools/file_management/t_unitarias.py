import unittest
from unittest.mock import mock_open, patch
import io
from main import create_file, write_json, write_bin, read_txt, read_json, read_bin

class TestCreateFile(unittest.TestCase):
    
    @patch('builtins.open', new_callable=mock_open, create=True)
    def test_create_file(self, mock_created_file):
        """ Test if the file is created successfully """
        
        name_file = "create_file.txt"
        content = "Hello, World!"
        
        # Call the function to test
        with patch("sys.stdout", new=io.StringIO()) as get_output:
            create_file(name_file, content)
            self.assertEqual(get_output.getvalue().strip(), "The file '(.TXT)' created  was succesfully.")
        
        # Check if the file was opened in write mode
        mock_created_file.assert_called_once_with(name_file, "x")
        mock_created_file().write.assert_called_once_with(content)

class Test_Write_Json(unittest.TestCase):
    
    @patch("builtins.open", new_callable = mock_open, create=True)
    def test_write_jason(self, mock_write_json):
        """ Test if the function write_json works """

        # Argumnets for the function
        name_file = "create_file.json"
        content = "Hello, World!"
        
        # Call the function to test
        with patch("sys.stdout", new=io.StringIO()) as get_output:
            write_json(name_file, content)
        
        # Check if the function returned the expected output
        result = get_output.getvalue().strip()
        self.assertIsInstance(result, str)
            
        mock_write_json.assert_called_once_with(name_file, "w")
        mock_write_json().write.assert_called_once()
        
class Test_Write_Bin(unittest.TestCase):
    
    @patch("builtins.open", new_callable = mock_open, create=True)
    def test_write_bin(self, mock_write_bin):
        """ Test if the function write_json works """

        # Argumnets for the function
        name_file = "create_file.bin"
        content = "Hello, World!"
        
        # Call the function to test
        with patch("sys.stdout", new=io.StringIO()) as get_output:
            write_bin(name_file, content)
        
        # Check if the function returned the expected output
        result = get_output.getvalue().strip()
        self.assertIsInstance(result, str)
            
        mock_write_bin.assert_called_once_with(name_file, "wb")
        mock_write_bin().write.assert_called_once()

class Test_Read_Txt(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data = "Hello, World!")
    def test_read_txt(self, mock_open_file):
        """ check if the file is read correctly and returns the expected content ."""

        name_file = "create_file.txt"
        
        #call the function to test
        with patch("sys.stdout", new=io.StringIO()):
            result = read_txt(name_file)

            #check if content returned is a string
            self.assertIsInstance(result, str)
        mock_open_file.assert_called_once_with(name_file, "r")
        
class Test_Read_Json(unittest.TestCase):
    
    @patch("main.json.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_read_json(self, mock_open_file, mock_json_load):
        """ check if the file is read correctly and returns the expected content ."""

        name_file = "create_file.json"
        mock_json_load.return_value = "Hello, World!"

        with patch("sys.stdout", new=io.StringIO()):
            get_output = read_json(name_file)
        
        self.assertIsInstance(get_output, str)
        mock_open_file.assert_called_once_with(name_file, "r")

class Test_Read_Bin(unittest.TestCase):
    
    @patch("main.pickle.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_read_bin(self, mock_open_file, mock_pickle_load):
        """ check if the file is read correctly and returns the expected content ."""

        name_file = "create_file.bin"
        mock_pickle_load.return_value = "Hello, World!"
        
        #get the output and restore the output
        with patch("sys.stdout", new=io.StringIO()):
            result = read_bin(name_file)
        
        #check if returne str
        self.assertIsInstance(result, str)
        mock_open_file.assert_called_once_with(name_file, "rb")

if __name__ == '__main__':
    unittest.main()