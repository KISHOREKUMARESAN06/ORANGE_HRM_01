import pytest
from openpyxl.styles import PatternFill
from datetime import datetime

from tests import test_hrm
from hrm_data.hrm_datas import Ohrm_locators
from configpack.config import Get_files
from utilpack.util_exl import XLU
from utilpack.util_all import Util_all
from pagepack.login_page import Login_cls
from pagepack.add_emp import Emp_add_cls
from pagepack.edit_emp import Emp_edit_cls
from pagpack.delete_emp import Emp_delete_cls

@pytest.mark.usefixtures("chrome_driver")
class Test_hrm:

    # TC_Login_01.
    def test_login(self):

        username = XLU.readData(exl_file_path, sheet1, 2, 6)
        password = XLU.readData(exl_file_path, sheet1, 2, 7)

        login = Login_cls(self.driver)
        dashboard = login.main_login(username, password)

        try:
            dashboard.dashboard_page().is_displayed()
            assert self.driver.current_url == Get_files.dashboard_url
            print(XLU.login_exp_res())
            XLU.date_and_time()
            XLU.writeData(exl_file_path, sheet1, 2, 9, 'TEST PASSED')
            XLU.fillGreenColor(exl_file_path, sheet1, 2, 9)
            XLU.writeData(exl_file_path, sheet1, 2, 10, 'KISHORE.K')

            assert self.driver.current_url != Get_files.dashboard_url
            XLU.writeData(exl_file_path, sheet1, 2, 9, 'TEST FAILED')
            XLU.fillRedColor(exl_file_path, sheet1, 2, 9)
            XLU.writeData(exl_file_path, sheet1, 2, 10, 'KISHORE.K')

        except Exception as e:
            print("error of login_test ", e)

    # TC_Login_02.
    def test_invalid_login(self):

        username = XLU.readData(exl_file_path, sheet1, 3, 6)
        password = XLU.readData(exl_file_path, sheet1, 3, 7)

        login = Login_cls(self.driver)
        dashboard = login.main_login(username, password)

        try:
            dashboard.dashboard_page().is_displayed()
            assert self.driver.current_url != Get_files.dashboard_url
            print(XLU.invalid_login_exp_res())
            XLU.date_and_time()
            XLU.writeData(exl_file_path, sheet1, 3, 9, 'TEST PASSED')
            XLU.fillGreenColor(exl_file_path, sheet1, 3, 9)
            XLU.writeData(exl_file_path, sheet1, 3, 10, 'KISHORE.K')

            assert self.driver.current_url == Get_files.dashboard_url
            XLU.writeData(exl_file_path, sheet1, 3, 9, 'TEST FAILED')
            XLU.fillRedColor(exl_file_path, sheet1, 3, 9)
            XLU.writeData(exl_file_path, sheet1, 3, 10, 'KISHORE.K')

        except Exception as e:
            print("error of invalid_login_test ", e)

    # TC_PIM_01.
    @pytest.mark.parametrize("username, password, f_name, m_name, l_name, emp_id, u_name, pwd, oth_id, dri_no, l_ex_dt, dob, gen, T_field",[(XLU.adding_datas(exl_file_path, sheet2))])
    def test_add_employee(self, username, password, f_name, m_name, l_name, emp_id, u_name, pwd, oth_id, dri_no, l_ex_dt, dob, gen, T_field):

        try:
            login = Login_cls(self.driver)
            login.main_login(username, password)

            add_emp = Emp_add_cls(self.driver)

            # click pim menu
            add_emp.click_pim_menu()
            print("pim clicked successfully")

            # click the add button
            add_emp.click_add_btn()
            print("clicking +Add button successfully")

            # upload profile picture
            Util_all.add_profile_pic(Get_files.image_path)
            print("profile picture uploaded successfully")

            # add employee information
            add_emp.main_add(f_name, m_name, l_name, emp_id, u_name, pwd, oth_id, dri_no, l_ex_dt, dob, gen, T_field)
            print("enter the all values into the input fields")
            print("employee added successfully")

            add_emp.pim_page().is_displayed()
            assert self.driver.current_url == Get_files.pim_url
            print(XLU.pim01_exp_res())
            XLU.date_and_time()
            XLU.writeData(exl_file_path, sheet1, 4, 9, 'TEST PASSED')
            XLU.fillGreenColor(exl_file_path, sheet1, 4, 9)
            XLU.writeData(exl_file_path, sheet1, 4, 10, 'KISHORE.K')

            assert self.driver.current_url != Get_files.pim_url
            XLU.writeData(exl_file_path, sheet1, 4, 9, 'TEST FAILED')
            XLU.fillRedColor(exl_file_path, sheet1, 4, 9)
            XLU.writeData(exl_file_path, sheet1, 4, 10, 'KISHORE.K')

        except Exception as e:
            print("error of EMP ADDING PAGE ", e)


    # TC_PIM_02.
    @pytest.mark.parametrize("username, password, m_name, l_name, emp_id", [(XLU.editing_datas(exl_file_path, sheet2))])
    def test_edit_employee(self, username, password, m_name, l_name, emp_id):

        try:
            login = Login_cls(self.driver)
            login.main_login(username, password)

            edit_emp = Emp_edit_cls(self.driver)

            # click pim menu
            edit_emp.click_pim_menu()
            print("pim clicked successfully")

            # searching via excel util read_data, the existing employee for edit operation.
            Util_all.emp_search_hrm(XLU.readData(exl_file_path, sheet2, 4, 4), XLU.readData(exl_file_path, sheet2, 4, 7))
            print("it is showing existing employee on the screen")

            # edit the existing employee information
            edit_emp.main_edit(m_name, l_name, emp_id)
            print("existing employee edited successfully")

            edit_emp.pim_page().is_displayed()
            assert self.driver.current_url == Get_files.pim_url
            print(XLU.pim02_exp_res())
            XLU.date_and_time()
            XLU.writeData(exl_file_path, sheet1, 5, 9, 'TEST PASSED')
            XLU.fillGreenColor(exl_file_path, sheet1, 5, 9)
            XLU.writeData(exl_file_path, sheet1, 5, 10, 'KISHORE.K')

            assert self.driver.current_url != Get_files.pim_url
            XLU.writeData(exl_file_path, sheet1, 5, 9, 'TEST FAILED')
            XLU.fillRedColor(exl_file_path, sheet1, 5, 9)
            XLU.writeData(exl_file_path, sheet1, 5, 10, 'KISHORE.K')

        except Exception as e:
            print("error of EMP EDITING PAGE ", e)

    # TC_PIM_03.
    def test_delete_employee(self):

        try:
            login = Login_cls(self.driver)
            login.main_login(username, password)

            delete_emp = Emp_delete_cls(self.driver)

            # click pim menu
            delete_emp.click_pim_menu()
            print("pim clicked successfully")

            # searching via excel util read_data, the existing employee for edit operation.
            Util_all.emp_search_hrm(XLU.readData(exl_file_path, sheet2, 4, 4), XLU.readData(exl_file_path, sheet2, 4, 7))
            print("it is showing existing employee on the screen")

            # delete the existing employee information
            delete_emp.main_delete()
            print("existing employee deleted successfully")

            delete_emp.pim_page().is_displayed()
            assert self.driver.current_url == Get_files.pim_url
            print(XLU.pim03_exp_res())
            XLU.date_and_time()
            XLU.writeData(exl_file_path, sheet1, 6, 9, 'TEST PASSED')
            XLU.fillGreenColor(exl_file_path, sheet1, 6, 9)
            XLU.writeData(exl_file_path, sheet1, 6, 10, 'KISHORE.K')

            assert self.driver.current_url != Get_files.pim_url
            XLU.writeData(exl_file_path, sheet1, 6, 9, 'TEST FAILED')
            XLU.fillRedColor(exl_file_path, sheet1, 6, 9)
            XLU.writeData(exl_file_path, sheet1, 6, 10, 'KISHORE.K')

        except Exception as e:
            print("error of EMP DELETE PAGE ", e)


