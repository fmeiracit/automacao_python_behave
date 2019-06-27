# -*- coding: utf-8 -*-
from random import randint

from behave import *
from selenium.webdriver.support.select import Select

from page_objects.home import Home

@step("the user clicks on the Admin Registration button")
def step_impl(context):
    home = Home(context.driver)
    home.click_admin_registration_button()


@step("the form to registration a admin should be shown")
def step_impl(context):
    home = Home(context.driver)
    home.check_table_if_is_opened()
    assert home.check_table_if_is_opened() == "wpn_content", 'Form not opened'


@step("I see the value Admin in the employee type field")
def step_impl(context):
    home = Home(context.driver)
    assert home.get_value_from_employee_type_field() == "Admin", 'Field was not filled up'


@step("que eu esteja na pagina de cadastro")
def step_impl(context):
    id_btn_admin = "/html/body/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[3]/td/ul/li[2]/a"
    context.driver.find_element_by_xpath(id_btn_admin).click()


@step('preencha o campo username com "{nome}"')
def step_impl(context, nome):
    context.driver.find_element_by_id("employee_id").send_keys(nome)


@step('preencha o campo firstname com "{firstname}"')
def step_impl(context,firstname ):
    context.driver.find_element_by_name("first_name").send_keys(firstname)


@step('preencha o campo Company/Dept. Name com "{company_name}"')
def step_impl(context,company_name ):
    context.driver.find_element_by_name("company_name").send_keys(company_name)


@step('preencha o campo Password com "{password}"')
def step_impl(context,password):
    context.driver.find_element_by_name("password").send_keys(password)


@step('preencha o campo Confirma Password com "{confirma_password}"')
def step_impl(context,confirma_password):
    context.driver.find_element_by_name("confirmpassword").send_keys(confirma_password)


@step('preencha o campo Data de Admissão com "{data_adm}"')
def step_impl(context,data_adm):
    context.driver.find_element_by_name("date").send_keys(data_adm)


@step('preencha o campo Email ID com "{email}"')
def step_impl(context, email):
    context.driver.find_element_by_name("emailid").send_keys(email)


@step('preencha o campo Country com "{pais}"')
def step_impl(context, pais):
    dropboxContry = context.driver.find_element_by_id("country")
    #from ipdb import set_trace; set_trace()
    dropboxContry.click()
    Select(dropboxContry).select_by_visible_text(pais)


@step('preencha o campo Area de Interesse com "{area}"')
def step_impl(context, area):
    context.driver.find_element_by_name("interest").send_keys(area)


@step("clicar no botão Salvar")
def step_impl(context):
    btn_salva = "/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr[13]/td[2]/input[1]"
    context.driver.find_element_by_xpath(btn_salva).click()



@step("mensagem de sucesso é apresentada")
def step_impl(context):
    textomensagem = "/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/span"
    esperado = "Than you for registering as a member. Your application has been sent. As soon as your registration is approved, you will be able to log onto the site."
    atual = context.driver.find_element_by_xpath(textomensagem).text
    assert esperado == atual, f"{esperado} diferente do {atual}"