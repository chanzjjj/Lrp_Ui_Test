from pages.ludan import LudanPage
from pages.login import LoginPage
import time

class TestLudan():

    def test_01(self, login:LoginPage, ludan:LudanPage):
        '''录单是否正常'''
        ludan.open("/#/login")  #打开登录页
        login.normal_information()  #登录
        ludan.normal_infotmation()  #录单
        is_toast_exit = ludan.is_element_exist(ludan.ele_save_toast)  #获取录单后的toast元素是否存在
        assert is_toast_exit == True
