from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrive_it_later(self):
        # Rico wants to make a to-do list - he opens the homepage
        self.browser.get(self.server_url)
        
        # Rico notes at the header of the page for he is all seeing
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Rico is prompted to enter a to-do
        inputbox = self.get_item_input_box()
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
        inputbox = self.get_item_input_box()
        inputbox.send_keys('swallow the sadness')
        inputbox.send_keys(Keys.ENTER)

        # the page updates and now includes both items
        self.check_for_row_in_list_table('1: dig a rico hole')
        self.check_for_row_in_list_table('2: swallow the sadness')


        # A new user, Josh, comes to the site

        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        # Josh visits the homepage and doesn't see Rico's list
        
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('dig a rico hole', page_text)
        self.assertNotIn('swallow the sadness', page_text)

        # Josh enters a new item

        inputbox = self.get_item_input_box()
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
        
    
