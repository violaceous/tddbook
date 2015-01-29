from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):
        # Rico wants to make a to-do list - he opens the homepage
        self.browser.get(self.live_server_url)
        
        # Rico notes at the header of the page for he is all seeing
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Rico is prompted to enter a to-do
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )

        # Rico enters 'dig a rico hole'
        inputbox.send_keys('dig a rico hole')
        
        # Rico hits enter and he is taken to a new URL, and now
        # it now has '1: dig a rico hole'
        inputbox.send_keys(Keys.ENTER)
        rico_list_url = self.browser.current_url
        self.assertRegex(rico_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: dig a rico hole')
        
        # Rico enters another item 'swallow the sadness'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('swallow the sadness')
        inputbox.send_keys(Keys.ENTER)

        # the page updates and now includes both items
        self.check_for_row_in_list_table('1: dig a rico hole')
        self.check_for_row_in_list_table('2: swallow the sadness')


        # A new user, Josh, comes to the site

        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        # Josh visits the homepage and doesn't see Rico's list
        
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('dig a rico hole', page_text)
        self.assertNotIn('swallow the sadness', page_text)

        # Josh enters a new item

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('get gold')
        inputbox.send_keys(Keys.ENTER)

        # Josh gets his own URL
        josh_list_url = self.browser.current_url
        self.assertRegex(josh_list_url, '/lists/.+')
        self.assertNotEqual(josh_list_url, rico_list_url)

        #Again, there is no trace of Rico's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('dig a rico hole', page_text)
        self.assertIn('get gold', page_text)
        
        self.fail('Finish the test!')



    
