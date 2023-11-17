from django.test import TestCase, SimpleTestCase

# Create your tests here.
class Simpletest(SimpleTestCase):
    def test_homepage_status(self):
        response = self.client.get("/")
        self.assertAlmostEqual(response.status_code, 200)
    