class Ohrm_locators:

    def __init__(self, driver):
        self.driver = driver

##### Login page locators ######

    l_username_name = 'username'
    l_password_name = 'password'
    login_btn_name = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

##### PIM Module Locators for (ADD employee information) #####

    # before entering pim module locators
    pim_module_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    pim_add_btn_link_text = ' Add '
    pim_add_emp_link_text = 'Add Employee' ## xapth = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a'
    # after entering pim module locators
    first_name_name = 'firstName'
    mid_name_name = 'middleName' ## optional
    last_name_name = 'lastName'
    emp_id_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    # After enable Create Login Details.
    Create_Login_Details_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    emp_user_name_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    emp_password_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    confirm_pass_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    pim_save_btn_link_text = ' Save ' ## xpath= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    # after entering the Personal Details page
    nick_name_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    other_id_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    Drivers_lis_num_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    license_ex_date_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input' ##yyyy-dd-mm
    ssn_num_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    sin_num_xpath =  '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    dd_nationality_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div'
    dd_marital_sts_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
    dob_xpath_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input' ##yyyy-dd-mm
    male_radio_btn_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label' ## Gender male
    female_radio_btn_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span' ## Gender female
    mil_ser_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    save_btn_two_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'
    dd_blood_grp_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]'
    test_field_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[2]/div/div[2]/input'
    save_btn_three_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button'
    
##### PIM Module Locators search option for (EDIT and DELETE employee information) #####

    edi_emp_name_xapth = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    edi_emp_id_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input'
    search_btn_link_text = ' Search ' ## xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    del_sel_btn_link_text = ' Delete Selected ' ## xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/button'
    check_box_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/input'
    dele_yes_btn_xpath = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'

##### add profile picture ######
    add_pro_pic_btn_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button'


##### Finally logout Locators #####

    # account locators
    dd_account_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span'
    logout_link_text = 'Logout'




