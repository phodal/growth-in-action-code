from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver


class BlogpostCase(LiveServerTestCase):
    def setUp(self):
        # setUp is where you instantiate the selenium webdriver and loads the browser.
        User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@example.com'
        )

        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(BlogpostCase, self).setUp()

    def tearDown(self):
        # Call tearDown to close the web browser
        self.selenium.quit()
        super(BlogpostCase, self).tearDown()

    def test_create_user(self):
        """
        Django admin create user test
        This test will create a user in django admin and assert that
        page is redirected to the new user change form.
        """
        # Open the django admin page.
        # DjangoLiveServerTestCase provides a live server url attribute
        # to access the base url in tests
        self.selenium.get(
            '%s%s' % (self.live_server_url,  "/admin/")
        )

        # Fill login information of admin
        username = self.selenium.find_element_by_id("id_username")
        username.send_keys("admin")
        password = self.selenium.find_element_by_id("id_password")
        password.send_keys("admin")


        # Locate Login button and click it
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/admin/blogpost/blogpost/add/")
        )

        # Fill the create user form with username and password
        self.selenium.find_element_by_id("id_title").send_keys("hello")
        self.selenium.find_element_by_id("id_author").send_keys("author")
        self.selenium.find_element_by_id("id_slug").send_keys("this_is_a_slug")
        self.selenium.find_element_by_id("id_body").send_keys("this is a body")

        # Forms can be submitted directly by calling its method submit
        self.selenium.find_element_by_css_selector(".default").submit()
        self.assertIn("Select blogpost to change | Django site admin", self.selenium.title)
