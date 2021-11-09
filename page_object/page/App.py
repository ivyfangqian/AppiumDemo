"""
    @Project:AppiumDemo
    @File:App.py
    @Author:fangqian8
    @Datetime:2021/11/8 2:59 下午
"""
from page_object.driver.AndroidClient import AndroidClient
from page_object.page.MainPage import MainPage


class App(object):

    @classmethod
    def main(cls):
        AndroidClient.restart_app()
        return MainPage()
