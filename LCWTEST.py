import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class LCWaikikiNavigationTest(unittest.TestCase):
    CATEGORY_PAGE = (By.CSS_SELECTOR, ".menu-header-item  ")
    SUB_CATEGORY_PAGE = (By.LINK_TEXT, "Tunik")
    PRODUCT_PAGE = (By.CLASS_NAME, "product-card--one-of-4")
    SIZE = (By.CSS_SELECTOR, "#option-size a:not([data-stock*='0']")
    ADD_TO_CART = (By.ID, "pd_add_to_cart")
    GO_TO_CART = (By.CLASS_NAME, "dropdown-label")
    HOME_PAGE = (By.CLASS_NAME, "main-header-logo")
    CART_PAGE = (By.CLASS_NAME, 'keep-shopping-label')

    base_url = "https://www.lcwaikiki.com/tr-TR/TR"
    time = 10

    @classmethod
    def setUpClass(cls):
        cls.chrome_driver_path = 'chromedriver.exe'
        cls.driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument('--disable-extensions'))
        cls.driver.maximize_window()

    def test_case(self):
        self.driver.get(self.base_url)
        self.assertIn("LC Waikiki | Türkiye’nin Moda ve Giyim Online Alışveriş Sitesi - LC Waikiki", self.driver.title, "Home Page Not Opened")
        self.driver.implicitly_wait(self.time)
        self.wait = WebDriverWait(self.driver, self.time)

        women = self.driver.find_element(*self.CATEGORY_PAGE)
        ActionChains(self.driver).move_to_element(women).perform()

        self.driver.find_element(*self.SUB_CATEGORY_PAGE).click()
        self.assertIn("Tunik Modelleri, Spor Tunik Modelleri - LC Waikiki", self.driver.title, "Wrong Category")

        self.driver.find_elements(*self.PRODUCT_PAGE)[3].click()
        self.assertTrue(self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)))

        self.driver.find_element(*self.SIZE).click()
        self.driver.find_element(*self.ADD_TO_CART).click()

        self.driver.find_elements(*self.GO_TO_CART)[2].click()
        self.assertEqual("Alışverişe Devam Et", self.wait.until(ec.element_to_be_clickable(self.CART_PAGE)).text, "You are not in the cart.")

        self.driver.find_element(*self.HOME_PAGE).click()
        self.assertIn("LC Waikiki | Türkiye’nin Moda ve Giyim Online Alışveriş Sitesi - LC Waikiki", self.driver.title,"Home Page Not Opened")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
