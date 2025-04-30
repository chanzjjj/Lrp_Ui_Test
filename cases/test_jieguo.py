from pages.ludan import LudanPage
from pages.login import LoginPage
from pages.fenfa import FenfaPage
from pages.jieguo import  JieguoPage

class TestJieguo():

    def test_01(self, login:LoginPage, ludan:LudanPage, fenfa:FenfaPage, jieguo:JieguoPage):
        '''结果录入是否正常'''
        fenfa.open("/#/login")  #打开登录页
        login.normal_information()  #登录
        bar_code = ludan.normal_infotmation()  #录单
        fenfa.normal_information(bar_code)  #分发
        jieguo.normal_information(bar_code)   #结果录入
