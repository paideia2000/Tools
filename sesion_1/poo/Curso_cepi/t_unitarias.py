import unittest
from main import check_who_is_better
from package import comparation, phones


class TestComparation_class(unittest.TestCase):
    def test_return_ValueError(self):
        """ check if the method_magic(__gt__) returned a ValueError."""
        p1 = comparation.Comparation(10, 100, "Iphone 16", "Iphone", "htop")
        p2 = comparation.Comparation(5, 110, "Samsung s24", "Samsung", "top")
        with self.assertRaises(ValueError) as vl:
            p1 > p2
            self.assertIsInstance(vl, str)

class TestPhones_class(unittest.TestCase):
    def test_return_AttributeError(self):
        """ check an (AttributeError) is returned if the object's property are not (INT or Float). """
        
        with self.assertRaises(AttributeError) as typ:
            p1 = phones.Phones("5",5, "Iphone 16", "Iphone")
            self.assertIsInstance(typ, str)

class TestCheckWhoIsBetter(unittest.TestCase):
    def test_return_str(self):
        """ check returned a str the function """
        p1 = comparation.Comparation(6,100, "Iphone 16", "Iphone")
        p2 = comparation.Comparation(5, 110, "Samsung s24", "Samsung")
        get_return: str = check_who_is_better(p1, p2)
        self.assertIsInstance(get_return, str)

if __name__=="__main__":
    unittest.main()