from selenium import webdriver
from selenium.webdriver.common.by import By
from configpack.config import Acts
from hrm_data.hrm_datas import Ohrm_locators
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from utilpack.util_exl import XLU
from pagepack.add_emp import Emp_add_cls
import os

class Util_all:

    def __init__(self, driver):
        self.driver = driver

    # for login operation enter the orange-hrm-site
    def login_hrm(self, username, password):

        user_na = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, Ohrm_locators.l_username_name))
        user_na.clear()
        user_na.send_keys(username)
        pwd = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, Ohrm_locators.l_password_name))
        pwd.clear()
        pwd.send_keys(password)
        l_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(BY.NAME, Ohrm_locators.login_btn_name))
        l_btn.click()
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert.accept()  # Accept the alert
        except:
            pass
        driver.implicitly_wait(20)

    # for searching function to edit or delete the particular employee information
    def emp_search_hrm(self,ser_name,ser_id):

        ser_emp_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.edi_emp_name_xapth))
        ser_emp_name.clear()
        ser_emp_name.send_keys(ser_name)

        ser_emp_id = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.edi_emp_id_xpath))
        ser_emp_id.clear()
        ser_emp_id.send_keys(ser_id)
        driver.implicitly_wait(10)

    # for adding profile picture of the employee
    def add_profile_pic(self, img_path):

        click_add_btn = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.add_pro_pic_btn_xpath))
        click_add_btn.click()

        click_add_btn.send_keys(os.path.abspath(img_path))
        driver.implicitly_wait(10)

    # for adding employee information into the PIM module
    def add_hrm(self,f_name, m_name, l_name, emp_id, u_name, pwd, oth_id, dri_no, l_ex_dt, dob, gen, T_field):

        fst_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, Ohrm_locators.first_name_name))
        fst_name.clear()
        fst_name.send_keys(f_name)

        mid_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, Ohrm_locators.mid_name_name))
        mid_name.clear()
        mid_name.send_keys(m_name)

        lst_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, Ohrm_locators.last_name_name))
        lst_name.clear()
        lst_name.send_keys(l_name)

        empid = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.emp_id_xpath))
        empid.clear()
        empid.send_keys(emp_id)

        enable_CLD = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.Create_Login_Details_xpath))
        enable_CLD.click()

        uname = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.emp_user_name_xpath))
        uname.clear()
        uname.send_keys(u_name)

        paswd = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.emp_password_xpath))
        paswd.clear()
        paswd.send_keys(pwd)

        confirm_paswd = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.confirm_pass_xpath))
        confirm_paswd.send_keys(pwd)

        save_enter = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, Ohrm_locators.pim_save_btn_link_text))
        save_enter.click()

        driver.implicitly_wait(30)

        other_id = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.other_id_xpath))
        other_id.send_keys(oth_id)

        drive_lic_num = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.Drivers_lis_num_xpath))
        drive_lic_num.send_keys(dri_no)

        lic_exp_date = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.license_ex_date_xpath))
        lic_exp_date.send_keys(l_ex_dt)

        nationality = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.dd_nationality_xpath)))
        nationality.select_by_visible_text("India")

        marital_sts = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.dd_marital_sts_xpath)))
        marital_sts.select_by_visible_text("Single")

        d_o_birth = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.dob_xpath_xpath))
        d_o_birth.send_keys(dob)

        gender = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.male_radio_btn_xpath))
        gender.send_keys(gen)

        save_btn_2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.save_btn_two_xpath))
        save_btn_2.click()

        blood_type = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.dd_blood_grp_xpath)))
        blood_type.select_by_visible_text("O+")

        tst_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.test_field_xpath))
        tst_field.send_keys(T_field)

        save__btn_3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.save_btn_three_xpath))
        save__btn_3.click()
        driver.implicitly_wait(20)

        return Emp_add_cls.click_pim_menu()

    # for edit the employee information from PIM module if any changes
    def edit_hrm(self,m_name, l_name, emp_id):

        mid_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, Ohrm_locators.mid_name_name))
        mid_name.clear()
        mid_name.send_keys(m_name)

        last_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, Ohrm_locators.last_name_name))
        last_name.clear()
        last_name.send_keys(l_name)

        employ_id = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.emp_id_xpath))
        employ_id.clear()
        employ_id.send_keys(emp_id)

        save__btn_2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.save_btn_two_xpath))
        save__btn_2.click()
        driver.implicitly_wait(20)

        return Emp_add_cls.click_pim_menu()

    # for delete the employee information.
    def delete_hrm(self):

        check_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.check_box_xpath))
        check_box.click()

        delete_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, Ohrm_locators.del_sel_btn_link_text))
        delete_btn.click()

        del_yes_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.dele_yes_btn_xpath ))
        del_yes_btn.click()

        return self.logout_hrm()

    # for finally getting logout.
    def logout_hrm(self):

        find_logout = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, Ohrm_locators.dd_account_xpath))
        find_logout.click()
        logout_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, Ohrm_locators.login_btn_name))
        logout_btn.click()

