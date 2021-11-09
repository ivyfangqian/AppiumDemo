"""
    @Project:AppiumDemo
    @File:MainPage.py
    @Author:fangqian8
    @Datetime:2021/11/5 3:03 下午
"""
from appium.webdriver.common.mobileby import MobileBy
from page_object.page.BasePage import BasePage
from page_object.page.InformationPage import InfomationPage


class MainPage(BasePage):

    def go_to_information(self):
        hangqing = '行情'
        self.find_by_text(hangqing)
        self.find_by_text(hangqing).click()
        # self.driver.find_element_by_xpath("//*[@text='行情']")
        # self.driver.find_element_by_xpath("//*[@text='行情']").click()
        return InfomationPage()