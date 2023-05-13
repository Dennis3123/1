from selenium import webdriver
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM.pageObjects.loginPage import LoginPage
from POM.pageObjects.homePage import HomePage

sys.tracebacklimit = 0

__unittest = True


class LinksTest(LoginPage, HomePage):
    baseUrl = "https://www.saucedemo.com/"
    standard_user = "standard_user"
    problem_user = "problem_user"
    password = "secret_sauce"
    homeURL = "https://www.saucedemo.com/inventory.html"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseUrl)
        lg = LoginPage(cls.baseUrl)
        lg.setUsername(cls.standard_user)
        lg.setPassword(cls.password)
        lg.clickLogin()
        cls.AddButtonsError = []
        cls.RemoveButtonsErrors = []

    def test_SocialLinks(self):
        hp = HomePage(self.driver)
        expect_links = ["https://twitter.com/saucelabs", "https://www.facebook.com/saucelabs",
                        "https://www.linkedin.com/company/sauce-labs/"]
        links = hp.getSocialLinks()
        for link in links:
            self.assertIn(link.get_attribute("href"), expect_links, "\n Link Error:" + link.get_attribute("href"))
            print("Test social link:" + expect_links[links.index(link)] + " - DONE")
        print("Test social links - DONE")

    def test_AddtoCart_Activate(self):
        hp = HomePage(self.driver)
        addButtons = hp.getAddtoCartButtons()

        # check if add to cart buttons working or not
        for button in addButtons:
            button.click()
            afterClick = hp.getAddtoCartButtons()

            try:
                self.assertEqual("Remove", afterClick[addButtons.index(button)].get_attribute("textContent"),
                                 addButtons.index(button))
            except AssertionError as e:
                self.AddButtonsErrors.append(button.get_attribute("name"))
            # button.click

        self.assertEqual([], self.AddButtonsErrors)
        print("Test press Add to cart button - DONE")
        # check if remove buttons working or not
        addButtons = hp.getAddToCartButtons()
        for button in addButtons:
            button.click()
            afterClick = hp.getAddToCartButtons()
            try:
                self.assertEqual("Add to cart", afterClick[addButtons.index(button)].get_attribute("textContent"),
                                 addButtons.index(button))
            except AssertionError as e:
                self.RemoveButtonsErrors.append(button.get_attribute("name"))

        self.assertEqual([], self.RemoveButtonsErrors)
        print("Test press Remove button - DONE")

    @classmethod
    def tearDown(cls):
        cls.drive.quit()


if __name__ == '__main__':
    pytest.main()
