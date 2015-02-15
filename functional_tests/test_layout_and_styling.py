from .base import FunctionalTest
        
class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Rico goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # He notices the input box is centered
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5
        )

        # He starts a new list and sees that input is also centered
        inputbox.send_keys('testing\n')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5
        )

    
