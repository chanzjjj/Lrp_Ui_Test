from pages.login import LoginPage
import time

class TestLogin():

    def test_01(self, login:LoginPage):
        '''登录是否正常'''
        login.open("/#/login")  #打开登录页
        login.normal_information() # 登录
        result = login.is_element_exist(login.ele_shouye) # 首页元素是否存在
        assert result == True


