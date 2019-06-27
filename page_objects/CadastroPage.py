from random import randint

from selenium.webdriver.support.select import Select


class CadastroPage:

    def __init__(self, driver):
        self.driver = driver
        self.id_username = "employee_id"
        self.name_firstname = "first_name"
        self.name_companyname = "company_name"
        self.name_password = "password"
        self.confirm_password = "confirmpassword"
        self.data = "date"
        self.e_mail = "emailid"
        self.country = "country"
        self.area_interesse = "interest"
        self.btn_salva = "/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr[13]/td[2]/input[1]"
        self.textomensagem = "/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/span"

    def preencher_username(self, nome):
        self.driver.find_element_by_id(self.id_username).send_keys(nome + str(randint(1,10000)))

    def preencher_firstname(self, firstname):
        self.driver.find_element_by_name(self.name_firstname).send_keys(firstname)

    def preencher_company(self, company_name):
        self.driver.find_element_by_name(self.name_companyname).send_keys(company_name)

    def preencher_password(self, password):
        self.driver.find_element_by_name(self.name_password).send_keys(password)

    def preencher_confirm_password(self, confirma_password):
        self.driver.find_element_by_name(self.confirm_password).send_keys(confirma_password)

    def preencher_data(self, data_adm):
        self.driver.find_element_by_name(self.data).send_keys(data_adm)

    def preencher_email(self, email):
        self.driver.find_element_by_name(self.e_mail).send_keys(email)

    def preencher_country(self, pais):
        dropboxContry = self.driver.find_element_by_id(self.country)
        dropboxContry.click()
        Select(dropboxContry).select_by_visible_text(pais)

    def preencher_areainteresse(self, area):
        self.driver.find_element_by_name(self.area_interesse).send_keys(area)

    def clicar_btnsalvar(self):
        self.driver.find_element_by_xpath(self.btn_salva).click()

    def comparar_mensagem(self, esperado):
        atual = self.driver.find_element_by_xpath(self.textomensagem).text
        assert esperado == atual, f"{esperado} diferente do {atual}"


