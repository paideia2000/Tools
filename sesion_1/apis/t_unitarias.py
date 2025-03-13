import unittest
from unittest.mock import patch, Mock
import requests as req
from main import get_data_users, save_data_jsonfile  # Importa la función desde tu archivo

class TestGetDataUsers(unittest.TestCase):

    @patch("main.req.get")  # 🔄 Evita que se le haga request.get a la api real y lo redirige a la api_fake
    def test_get_data_users_returns_list(self, fake_api):
        """✅ Verifica que get_data_users() retorne una lista"""
        mock_response = Mock()  # Simulamos la respuesta de la API
        mock_response.status_code = 200
        mock_response.json.return_value = [{"id": 1, "name": "John Doe"}]  # JSON que va a devolver la api_fake
        fake_api.return_value = mock_response  # La api falsa va a devolver un status code de 200 y un contenido en formato json como el anterior

        endpoint = "https://jsonplaceholder.typicode.com/users"
        result = get_data_users(endpoint)  # Llamamos a la función
        self.assertIsInstance(result, list)  # ✅ Verifica que el resultado sea una lista

    @patch("main.req.get")
    def test_get_data_users_http_error(self, fake_api):
        """❌ Prueba cuando la API responde con un error HTTP"""
        fake_api.side_effect = req.exceptions.HTTPError("HTTP Error")  # Simulamos un error HTTP

        endpoint = "https://jsonplaceholder.typicode.com/users"
        with self.assertRaises(req.exceptions.HTTPError):  # Esperamos que la función lance un HTTPError
            get_data_users(endpoint)
    
    @patch("main.req.get")
    def test_get_data_users_connectionerror(self, fake_api):
        """ test when the connection fails """
        fake_api.side_effect = req.exceptions.ConnectionError("ConnectionError")
        
        endpoint = "https://jsonplaceholder.typicode.com/users"
        with self.assertRaises(req.exceptions.ConnectionError):
            get_data_users(endpoint)


if __name__ == "__main__":
    unittest.main()