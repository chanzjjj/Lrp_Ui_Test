from pages.ludan import LudanPage
from pages.login import LoginPage
from pages.fenfa import FenfaPage

class TestFenfa():

    def test_01(self, login:LoginPage, ludan:LudanPage, fenfa:FenfaPage):
        '''分发是否正常'''
        fenfa.open("/#/login")
        login.normal_information()
        fenfa.normal_information()
