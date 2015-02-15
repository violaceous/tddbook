from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Rico tests the site by adding an empty list item.
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # The home page refreshes, and there is an error message saying
        # that the list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # He enters an item, and it works
        self.get_item_input_box().send_keys('Pet granola\n')
        self.check_for_row_in_list_table('1: Pet granola')

        # He tries another blank item
        self.get_item_input_box().send_keys('\n')

        # He receives another warning on the list page
        self.check_for_row_in_list_table('1: Pet granola')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # and he fixes it by adding some text
        self.get_item_input_box().send_keys('Charlie roll\n')
        self.check_for_row_in_list_table('1: Pet granola')
        self.check_for_row_in_list_table('2: Charlie roll')

    def test_cannot_add_duplicate_items(self):
        # Rico goes to the homepage and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy raw milk\n')
        self.check_for_row_in_list_table('1: Buy raw milk')

        # He tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy raw milk\n')

        # He sees an error message
        self.check_for_row_in_list_table('1: Buy raw milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You've already got this in your list")
    
