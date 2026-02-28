import unittest
import requests
from config import YANDEX_TOKEN

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
headers = {"Authorization": f"OAuth {YANDEX_TOKEN}"}

class TestYandexDiskAPI(unittest.TestCase):
    
    def setUp(self):
        self.test_folder = f"netology_test_{__name__}"
    
    def tearDown(self):
        delete_url = f"{BASE_URL}?path={self.test_folder}"
        try:
            requests.delete(delete_url, headers=headers)
        except:
            pass
    
    def test_create_folder_success(self):
        create_url = f"{BASE_URL}?path={self.test_folder}"
        response = requests.put(create_url, headers=headers)
        self.assertEqual(response.status_code, 201, f"Ожидали 201, получили {response.status_code}")
        
        list_url = f"{BASE_URL}?path=/"
        list_response = requests.get(list_url, headers=headers)
        self.assertEqual(list_response.status_code, 200)
        self.assertIn(self.test_folder, list_response.text)
    
    def test_create_existing_folder(self):
        create_url = f"{BASE_URL}?path={self.test_folder}"
        
        requests.put(create_url, headers=headers)
        
        response = requests.put(create_url, headers=headers)
        self.assertEqual(response.status_code, 409)
    
    def test_create_folder_bad_token(self):
        bad_headers = {"Authorization": "OAuth invalid_token_123"}
        create_url = f"{BASE_URL}?path=test_bad_token"
        response = requests.put(create_url, headers=bad_headers)
        self.assertIn(response.status_code, [401, 403])
    
    def test_create_folder_no_auth(self):
        create_url = f"{BASE_URL}?path=test_no_auth"
        response = requests.put(create_url, headers={})
        self.assertIn(response.status_code, [401, 403])
    
    def test_create_root_folder(self):
        create_url = f"{BASE_URL}?path=disk"
        response = requests.put(create_url, headers=headers)
        self.assertEqual(response.status_code, 409)  
        
        list_url = f"{BASE_URL}?path=/"
        list_response = requests.get(list_url, headers=headers)
        self.assertIn("disk", list_response.text)

if __name__ == '__main__':
    unittest.main(verbosity=2)