"""
    @Project:AppiumDemo
    @File:AndroidClient.py
    @Author:fangqian8
    @Datetime:2021/11/5 2:27 下午
"""
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient(object):
    """
    AndroidClient:
        包含两个方法，install_app首次启动App与restart_app重启App方法
    """
    
    driver: WebDriver

    @classmethod
    def install_app(cls) -> WebDriver:
        capabilities = {
            "platformName": "android",
            # "deviceName": "6SCUZHHAKN4DJZKB",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "autoGrantPermissions": "true"
        }
        # capabilities["app"] = ""

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def restart_app(cls) -> WebDriver:
        capabilities = {
            "platformName": "android",
            # "deviceName": "6SCUZHHAKN4DJZKB",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True
        }
        # capabilities["app"] = ""

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
        cls.driver.implicitly_wait(10)
        return cls.driver
