from django.test import SimpleTestCase

class PageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        
    def test_home_page_contains_name(self):
        response = self.client.get('/')
        self.assertContains(response, 'Taneisha Banks')
        
    def test_about_page_contains_fact(self):
        response = self.client.get('/about/')
        self.assertContains(response, 'live concerts')