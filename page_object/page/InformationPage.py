"""
    @Project:AppiumDemo
    @File:InformationPage.py
    @Author:fangqian8
    @Datetime:2021/11/5 3:06 下午
"""
from appium.webdriver.common.mobileby import MobileBy

from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage


class InfomationPage(BasePage):

    def get_shanghai_stock(self):
        # shanghai_stock = self.driver.find_element_by_id("com.xueqiu.android:id/single_line_quote_price").text
        # shanghai_stock_pct = self.driver.find_element_by_id("com.xueqiu.android:id/single_line_quote_pct").text
        shanghai_stock_element= (MobileBy.ID, "com.xueqiu.android:id/single_line_quote_price")
        shanghai_stock = self.find(shanghai_stock_element).text
        shanghai_stock_pct_element = (MobileBy.ID, "com.xueqiu.android:id/single_line_quote_pct")
        shanghai_stock_pct = self.find(shanghai_stock_pct_element).text
        return float(shanghai_stock), float(shanghai_stock_pct[:-1])