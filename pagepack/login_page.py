from selenium import webdriver
from selenium.webdriver.common.by import By
from configpack.config import Acts
from hrm_data.hrm_datas import ohrm_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilpack.util_all import Util_all
from utilpack.util_exl import XLU


class Login_cls:

    def __init__(self, driver):
        self.driver = driver

    # method of login with username and password.
    def main_login(self, username, password):

        print("execute main_login in login_cls")
        try:
            Util_all.login_hrm(username, password)
        except Exception as e:
            print(" something error in main_login", e)

