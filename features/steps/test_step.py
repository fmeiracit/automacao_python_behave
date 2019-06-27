# -*- coding: utf-8 -*-
from random import randint

from behave import *
from selenium.webdriver.support.select import Select

from page_objects.home import Home
from page_objects.CadastroPage import CadastroPage

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
    pag_cadastro = CadastroPage(context.driver)
    pag_cadastro.preencher_username(nome)


@step('preencha o campo firstname com "{firstname}"')
def step_impl(context,firstname ):
    pag_cadastro = CadastroPage(context.driver)
    pag_cadastro.preencher_firstname(firstname)


@step('preencha o campo Company/Dept. Name com "{company_name}"')
def step_impl(context,company_name ):
    pag_cadastro = CadastroPage(context.driver)
    pag_cadastro.preencher_company(company_name)


@step('preencha o campo Password com "{password}"')
def step_impl(context,password):
    pag_cadastro = CadastroPage(context.driver)
    pag_cadastro.preencher_password(password)


@step('preencha o campo Confirma Password com "{confirma_password}"')
def step_impl(context,confirma_password):
    pag_cadastro = CadastroPage(context.driver)
    pag_cadastro.preencher_confirm_password(confirma_password)


@step('preencha o campo Data de Admissão com "{data_adm}"')
def step_impl(context,data_adm):
    pag_cadastro = CadastroPage(context.driver)
    pag_cadastro.preencher_data(data_adm)


@step('preencha o campo Email ID com "{email}"')
def step_impl(context, email):
    pag_cadastro = CadastroPage(context.driver)
    pag_cadastro.preencher_email(email)


@step('preencha o campo Country com "{pais}"')
def step_impl(context, pais):
    pag_cadastro = CadastroPage(context.driver)
    pag_cadastro.preencher_country(pais)


@step('preencha o campo Area de Interesse com "{area}"')
def step_impl(context, area):
    pag_cadastro = CadastroPage(context.driver)
    pag_cadastro.preencher_areainteresse(area)


@step("clicar no botão Salvar")
def step_impl(context):
    pag_cadastro = CadastroPage(context.driver)
    pag_cadastro.clicar_btnsalvar()

@step("mensagem de sucesso é apresentada")
def step_impl(context):
    pag_cadastro = CadastroPage(context.driver)
    pag_cadastro.comparar_mensagem(context.text)

