"""
    @Project:AppiumDemo
    @File:BasePage.py
    @Author:fangqian8
    @Datetime:2021/11/8 3:15 下午
"""
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy

from page_object.driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):
        self.driver = AndroidClient.driver

    def find(self, kv) -> WebElement:
        return self.driver.find_element(*kv)

    def find_by_text(self, text) -> WebElement:
        return self.find((MobileBy.XPATH, "//*[@text='%s']" % text))
