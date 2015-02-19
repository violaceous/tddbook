from .base import FunctionalTest
import time
from selenium.webdriver.support.ui import WebDriverWait

TEST_EMAIL = 'sexy_rico@mockmyid.com'

class LoginTest(FunctionalTest):

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

    def test_login_with_persona(self):
        # Rico goes to the list site
        # and notices he can sign in

        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()

        # A Persona login box appears
        self.switch_to_new_window('Mozilla Persona')

        # Rico logs in with his email address
        ## use mockmyid.com for test email
        self.browser.find_element_by_id(
            'authentication_email'
        ).send_keys(TEST_EMAIL)
        self.browser.find_element_by_tag_name('button').click()

        # The Persona window closes
        self.switch_to_new_window('To-Do')

        # Rico can see that he is logged in
        self.wait_to_be_logged_in(email=TEST_EMAIL)

        # Rico refreshes the page and sees he is still logged in
        self.browser.refresh()
        self.wait_to_be_logged_in(email=TEST_EMAIL)

        # Rico logs out
        self.browser.find_element_by_id('id_logout').click()
        self.wait_to_be_logged_out(email=TEST_EMAIL)

        # Rico refreshes to check he is really logged out
        self.browser.refresh()
        self.wait_to_be_logged_out(email=TEST_EMAIL)
