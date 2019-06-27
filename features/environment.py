import os
from shutil import rmtree

from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Firefox()
    context.driver.get('http://qualitypointtech.net/timesheetdemo/index.php')


def before_scenario(context, scenario):
    ...


def after_step(context, step):
    ...


def after_all(context):
    ...
    # context.driver.quit()
