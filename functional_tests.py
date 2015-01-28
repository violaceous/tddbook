from selenium import webdriver
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
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

# Rico is prompted to enter a to-do

# Rico types 'dig a rico hole'

# Rico hits enter and the page updates
# it now has '1: dig a rico hole'

# Rico enters another item 
# it is 'swallow the sadness'

#the page updates to include both items

#Rico notes the unique url and explantory text

#rico navigates to that url and sees his list

# rico embraces the sadness

    
