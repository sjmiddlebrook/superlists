from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(2)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Marissa opens the homepage to check out to-do app
		self.browser.get(self.live_server_url)

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

		# When she hits enter, she is taken to a new URL, and now the page lists
		# "1: Buy plane tickets to Cartagena" as an item in a to-do list
		inputBox.send_keys(Keys.ENTER)

		marissa_list_url = self.browser.current_url
		self.assertRegex(marissa_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy plane tickets to Cartagena')

		# There is still a text box inviting her to add another item. She
		# enters "Find Airbnb in Cartagena"
		inputBox = self.browser.find_element_by_id('id_new_item')
		inputBox.send_keys('Find Airbnb in Cartagena')
		inputBox.send_keys(Keys.ENTER)

		# The page updates again and now shows both items on her list
		self.check_for_row_in_list_table('1: Buy plane tickets to Cartagena')
		self.check_for_row_in_list_table('2: Find Airbnb in Cartagena')
		
		# Now a new user, Heidi comes along to the site

		## We use a new browser session to make sure that no information
		## of Marissa's is coming through from cookies etc
		self.browser.quit()
		self.browser = webdriver.Firefox()

		# Heidi visits the home page. There is no sign of Marissa's lists
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy plane tickets', page_text)
		self.assertNotIn('Find Airbnb', page_text)


		# Heidi starts a new list by entering a new item
		inputBox = self.browser.find_element_by_id('id_new_item')
		inputBox.send_keys('Buy new movie')
		inputBox.send_keys(Keys.ENTER)

		# Heidi gets her own unique URL
		heidi_list_url = self.browser.current_url
		self.assertRegex(heidi_list_url, '/lists/.+')
		self.assertNotEqual(heidi_list_url, marissa_list_url)

		# Again there is no trace of Marissa's list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy plane tickets', page_text)
		self.assertNotIn('Find Airbnb', page_text)

		# Satisfied, they go back to sleep


