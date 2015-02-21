from selenium import webdriver
from .base import FunctionalTest

def quit_if_possible(browser):
    try: browser.quit()
    except: pass

class SharingTest(FunctionalTest):

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Rico is a logged-in user
        self.create_pre_authenticated_session('sexy_rico@sexy.com')
        rico_browser = self.browser
        self.addCleanup(lambda: quit_if_possible(rico_browser))

        # His bff Josh is also on the site
        josh_browser = webdriver.Firefox()
        self.addCleanup(lambda: quit_if_possible(josh_browser))
        self.browser = josh_browser
        self.create_pre_authenticated_session('josh@derpcore.io')

        # Rico goes to the home page and starts a list
        self.browser = rico_browser
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('trabajo\n')

        # He shares his wisdom
        share_box = self.browser.find_element_by_css_selector('input[name=email]')
        self.assertEqual(
            share_box.get_attribute('placeholder'),
            'your-friend@example.com'
        )
