from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Marissa opens the homepage to check out to-do app
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# She is invited to enter a to-do item straight away

		# She types "Buy plane tickets to Cartagena" into a text box

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy plane tickets to Cartagena" as an item in a to-do list

		# There is still a text box inviting her to add another item. She
		# enters "Find Airbnb in Cartagena"

		# The page updates again and now shows both items on her list

		# Marissa wonders whether the site will remember her list. Then
		# she sees that the site has generated a unique URL for her --
		# -- there is some explanatory text to that effect

		# She visits that URL - her to-do list is still there

		# Satisfied she goes back to sleep


if __name__ == '__main__':
	unittest.main()

