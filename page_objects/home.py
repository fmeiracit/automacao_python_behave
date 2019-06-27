from page_objects.base_page import BasePageObject


class Home(BasePageObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.admin_regs_path = '// a[text() = "Admin Registration"]'

    def click_admin_registration_button(self):
        self.driver.find_element_by_xpath(self.admin_regs_path).click()
        return self

    def check_table_if_is_opened(self):
        table_class = self.driver.find_element_by_css_selector('table.wpn_content')
        return table_class.get_attribute('class')

    def get_value_from_employee_type_field(self):
        employee_type_field_path = '//*[@id="employee_type"]'
        employee_type_field = self.driver.find_element_by_xpath(employee_type_field_path)
        return employee_type_field.get_attribute('value')

