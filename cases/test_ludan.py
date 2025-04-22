from pages.ludan import LudanPage
from pages.login import LoginPage
import time

class TestLudan():

    def test_01(self, login:LoginPage, ludan:LudanPage):
        '''录单是否正常'''
        ludan.open("/#/login")
        login.normal_information()
        ludan.normal_infotmation()
        is_toast_exit = ludan.is_element_exist(ludan.ele_save_toast)
        assert is_toast_exit == True
