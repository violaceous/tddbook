from .base import FunctionalTest
import time
from selenium.webdriver.support.ui import WebDriverWait

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

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id),
            'Could not find element with id {}. Page text was {}'.format(
                element_id, self.browser.find_element_by_tag_name('body').text
                )
            )

    def wait_to_be_logged_in(self):
        self.wait_for_element_with_id('id_logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('sexy_rico@mockmyid.com', navbar.text)

    def wait_to_be_logged_out(self):
        self.wait_for_element_with_id('id_login')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn('sexy_rico@mockmyid.com', navbar.text)
        
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
        ).send_keys('sexy_rico@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        # The Persona window closes
        self.switch_to_new_window('To-Do')

        # Rico can see that he is logged in
        self.wait_to_be_logged_in()

        # Rico refreshes the page and sees he is still logged in
        self.browser.refresh()
        self.wait_to_be_logged_in()

        # Rico logs out
        self.browser.find_element_by_id('id_logout').click()
        self.wait_to_be_logged_out()

        # Rico refreshes to check he is really logged out
        self.browser.refresh()
        self.wait_to_be_logged_out()
