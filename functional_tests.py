from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Rico wants to make a to-do list - he opens the homepage
        self.browser.get('http://localhost:8000')
        
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
        
        # Rico hits enter and the page updates
        # it now has '1: dig a rico hole'
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: dig a rico hole', [row.text for row in rows])        
        
        # Rico enters another item 'swallow the sadness'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('swallow the sadness')
        inputbox.send_keys(Keys.ENTER)
        
        # the page updates and now includes both items
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            '2: swallow the sadness' ,
            [row.text for row in rows]
        )

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

# Rico enters another item 
# it is 'swallow the sadness'

#the page updates to include both items

#Rico notes the unique url and explantory text

#rico navigates to that url and sees his list

# rico embraces the sadness

    
