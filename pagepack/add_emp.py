from selenium import webdriver
from selenium.webdriver.common.by import By
from configpack.config import Acts
from hrm_data.hrm_datas import ohrm_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilpack.util_all import Util_all



class Emp_add_cls:

    def __init__(self, driver):
        self.driver = driver

    # clicking PIM module in left-side menu.
    def click_pim_menu(self):
        pim_click = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.pim_module_xpath))
        pim_click.click()

    # click add btn in after clicking PIM module.
    def click_add_btn(self):
        add_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, Ohrm_locators.pim_add_btn_link_text))
        add_btn.click()

    # this method for tests adding employee.
    def main_add(self, f_name, m_name, l_name, emp_id, u_name, pwd, oth_id, dri_no, l_ex_dt, dob, gen, T_field):

        print("execute main_add in Emp_add_cls")
        try:
            Util_all.add_hrm(f_name, m_name, l_name, emp_id, u_name, pwd, oth_id, dri_no, l_ex_dt, dob, gen, T_field)
        except Exception as e:
            print(" something error in main_add", e)



        
