import unittest
from unittest.mock import patch, Mock
import requests as req
from io import StringIO
from main import method_get_api

class TestGetDataUsers(unittest.TestCase):
    ENDPOINT = "https://jsonplaceholder.typicode.com/users"
    MOCK_API_RESPONSE = [{"id": 1, "name": "John Doe"}]
    
    @patch("main.req.get")  # 🔄 Evita que se le haga request.get a la api real y lo redirige a la api_fake
    def test_get_data_users_returns_list(self, fake_api):
        """✅ Verifica que method_get_api() retorne una lista"""
        
        with patch("sys.stdout", new=StringIO()):
            mock_response = Mock()  # Simulamos la respuesta de la API
            mock_response.status_code = 200
            mock_response.json.return_value = self.MOCK_API_RESPONSE  # JSON que va a devolver la api_fake
            fake_api.return_value = mock_response  # La api falsa va a devolver un status code de 200 y un contenido en formato json como el anterior

            result = method_get_api(self.ENDPOINT)  # Llamamos a la función
            self.assertEqual(result, self.MOCK_API_RESPONSE)  # ✅ Verifica que el resultado sea una lista

    @patch("main.req.get")
    def test_get_data_users_http_error(self, fake_api):
        """❌ Prueba cuando la API responde con un error HTTP"""
        fake_api.side_effect = req.exceptions.HTTPError("HTTP Error")  # Simulamos un error HTTP
        
        with patch("sys.stdout", new=StringIO()):
            with self.assertRaises(req.exceptions.HTTPError):  # Esperamos que la función lance un HTTPError
                method_get_api(self.ENDPOINT)
            
    
    @patch("main.req.get")
    def test_get_data_users_connectionerror(self, fake_api):
        """ test when the connection fails """
        fake_api.side_effect = req.exceptions.ConnectionError("ConnectionError")
        with patch("sys.stdout", new=StringIO()):
            with self.assertRaises(req.exceptions.ConnectionError):
                method_get_api(self.ENDPOINT)
            

if __name__ == "__main__":
    unittest.main()