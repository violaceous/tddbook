from django.conf import settings
from .base import FunctionalTest
from .server_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
User = get_user_model()
from django.contrib.sessions.backends.db import SessionStore

from .base import FunctionalTest

class MyListsTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        if self.against_staging:
            session_key = create_session_on_server(self.server_host, email)
        else:
            session_key = create_pre_authenticated_session(email)
        ## to set a cookie we need to visit the domain
        ## 404 pages load the quickest
        self.browser.get(self.server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session_key,
            path='/',
        ))

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Rico is a logged-in user
        self.create_pre_authenticated_session('sexy_rico@sexy.com')
        
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Finish the bathroom\n')
        self.get_item_input_box().send_keys('Make Granola dinner\n')
        first_list_url = self.browser.current_url

        # he sees a "my lists" link
        self.browser.find_element_by_link_text('My lists').click()

        # he sees that his list is there named according to the first item
        self.browser.find_element_by_link_text('Finish the bathroom\n').click()
        self.assertEqual(self.browser.current_url, first_list_url)

        # he starts another list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('build a deck\n')
        second_list_url = self.browser.current_url

        # under my lists the new list appears
        self.browser.find_element_by_link_text('My lists').click()
        self.browser.find_element_by_link_text('build a deck\n')
        self.assertEqual(self.browser.current_url, second_list_url)

        # he logs out and the my lists option goes away
        self.browser.find_element_by_id('id_logout').click()
        self.assertEqual(
            self.browser.find_elements_by_link_text('My lists'), []
        )
        
