from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):

	def tes_home_page(self):
		response=self.client.get('/')
		self.assertEquals(response.status_code,200)

	def test_about_page(self):
		response=self.client.get('/about/')
		self.assertEquals(response.status_code,200)
			