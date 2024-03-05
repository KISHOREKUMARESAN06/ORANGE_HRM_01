from selenium import webdriver
from selenium.webdriver.common.by import By
from configpack.config import Acts
from hrm_data.hrm_datas import ohrm_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilpack.util_all import Util_all



class Emp_add_cls:

    def __init__(self, driver):
        super().__int__(driver)
        self.driver = driver

    # only for validate the Dashboard page
    def dashboard_page(self):
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert.accept()  # Accept the alert
        except:
            pass
        driver.implicitly_wait(20)

    # only for validate the PIM page
    def pim_page(self):

        driver.implicitly_wait(20)
        return click_pim_menu()
        print("NOW IN PIM PAGE")
