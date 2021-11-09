"""
    @Project:AppiumDemo
    @File:test_information.py
    @Author:fangqian8
    @Datetime:2021/11/5 3:22 下午
"""
from page_object.page.App import App


class TestInformation(object):

    def test_shanghai_stock(self):
        assert App.main().go_to_information().get_shanghai_stock()[0] > 3000

