from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(2)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Marissa opens the homepage to check out to-do app
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item straight away
		inputBox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputBox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# She types "Buy plane tickets to Cartagena" into a text box
		inputBox.send_keys('Buy plane tickets to Cartagena')

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy plane tickets to Cartagena" as an item in a to-do list
		inputBox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy plane tickets to Cartagena' for row in rows),
			"new to-do item did not appear in table"
		)

		# There is still a text box inviting her to add another item. She
		# enters "Find Airbnb in Cartagena"
		self.fail('Finish the Test!')

		# The page updates again and now shows both items on her list

		# Marissa wonders whether the site will remember her list. Then
		# she sees that the site has generated a unique URL for her --
		# -- there is some explanatory text to that effect

		# She visits that URL - her to-do list is still there

		# Satisfied she goes back to sleep


if __name__ == '__main__':
	unittest.main()

