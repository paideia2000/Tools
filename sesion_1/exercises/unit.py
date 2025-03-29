import unittest
from io import StringIO
from unittest.mock import patch
from test_1 import interface, board, check_who_winner, get_choise_player


class TestInterface(unittest.TestCase):
    
    def test_return_str(self):
        """ the function interface must returned a str """
        with patch("sys.stdout", new=StringIO()):
            string: None = interface()
            print(type(string))
        self.assertIsNone(string, None)
        
class TestBoard(unittest.TestCase):
    
    def test_return_none(self):
        """ the function must reurned a str """
        with patch("sys.stdout", new=StringIO()):
            string = board({i:i for i in range(1,10)})
        self.assertIsNone(string, None)

class TestCheckWhoWinner(unittest.TestCase):
    
    def test_return_bool(self):
        """ check if the function retuned a bool """
        with patch("sys.stdout", new=StringIO()):
            get_response: bool = check_who_winner([1,2,3])
        self.assertIsInstance(get_response, bool)
        
class TestGetChoisePlayer(unittest.TestCase):
    
    def test_return_integer_and_list(self):
        """ the function must returned  a integer number. """
        with patch("sys.stdout", new=StringIO()):
            with patch("builtins.input", return_value ="4"):
                result_1: int = get_choise_player("Choise move player", [3,4,5])
                self.assertIsInstance(result_1, int)
        

if __name__ == "__main__":
    unittest.main()