from selenium import webdriver
from .base import FunctionalTest
from .home_and_list_pages import HomePage

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
        list_page = HomePage(self).start_new_list('trabajo')

        # He shares his wisdom
        share_box = list_page.get_share_box()
        self.assertEqual(
            share_box.get_attribute('placeholder'),
            'your-friend@example.com'
        )
        
        list_page.share_list_with('josh@derpcore.io')

        # josh derp now goes to thei lists page
        self.browser = josh_browser
        HomePage(self).go_to_home_page().go_to_my_lists_page()

        # he sees Rico's wisdom
        self.browser.find_element_by_link_text('trabajo').click()

        # Josh sees that it is Rico's list
        self.wait_for(lambda: self.assertEqual(
            list_page.get_list_owner(),
            'sexy_rico@rico.com'
        ))

        # He adds an item to the list
        list_page.add_new_item('Praise Rico!')

        # When Rico refreshes the page he sees it
        self.browser = rico_browser
        self.browser.refresh()
        list_page.wait_for_new_item_in_list('Praise Rico!', 2)
