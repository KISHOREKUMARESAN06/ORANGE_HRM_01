from selenium import webdriver
from selenium.webdriver.common.by import By
from configpack.config import Acts
from hrm_data.hrm_datas import ohrm_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilpack.util_all import Util_all



class Emp_delete_cls:

    def __init__(self, driver):
        self.driver = driver

    # this method for tests deleting employee.
    def main_delete(self):

        print("searching the employee")
        try:
            Util_all.emp_search_hrm(ser_name, ser_id)
        except:
            print("something went wrong in main_edit--searching option")

        print("execute main_delete in Emp_delete_cls")
        try:
            Util_all.delete_hrm()
        except Exception as e:
            print(" something error in main_delete", e)

