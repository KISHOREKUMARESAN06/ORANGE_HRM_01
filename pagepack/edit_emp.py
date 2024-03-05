from selenium import webdriver
from selenium.webdriver.common.by import By
from configpack.config import Acts
from hrm_data.hrm_datas import ohrm_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilpack.util_all import Util_all



class Emp_edit_cls:

    def __init__(self, driver):
        super().__int__(driver)
        self.driver = driver

    # this method for tests editing employee.
    def main_edit(self, m_name, l_name, emp_id):

        print("searching the employee")
        try:
            Util_all.emp_search_hrm(ser_name, ser_id)
        except:
            print("something went wrong in main_edit--searching option")


        print("execute main_edit in Emp_edit_cls")
        try:
            Util_all.edit_hrm(m_name, l_name, emp_id)
        except Exception as e:
            print(" something error in main_edit", e)

