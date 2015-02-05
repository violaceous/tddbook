from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Rico tests the site by adding an empty list item.
        
        # The home page refreshes, and there is an error message saying
        # that the list items cannot be blank

        # He enters an item, and it works

        # He tries another blank item

        # He receives another warning on the list page

        # and he fixes it by adding some text

        self.fail('write me!')
    
