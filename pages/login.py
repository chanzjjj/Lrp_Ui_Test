from common.base import Base
import time
from selenium import webdriver



class LoginPage(Base):
    ele_switch = ("xpath", '//*[@class="corner-icon-viewV2"]/*[name()="svg"]') # 二维码模式切换为密码模式的按钮
    ele_username = ("xpath", '//*[@id="app"]/div/div[2]/div/div/div[3]/form/div[1]/div/div[1]/input') # 用户名
    ele_pwd = ("xpath", '//*[@id="app"]/div/div[2]/div/div/div[3]/form/div[2]/div/div[1]/input') # 密码
    ele_login = ("xpath", '//*[@id="app"]/div/div[2]/div/div/div[3]/form/div[3]/div/button') # 登录按钮
    ele_shouye = ("xpath", '//*[@id="app"]/div/div[2]/div[1]/div[3]/span[1]/span[1]/span') # 首页

    def input_username(self, username):
        '输入用户名'
        self.send(self.ele_username, username)

    def input_psw(self, password):
        '输入密码'
        self.send(self.ele_pwd, password)

    def click_login(self):
        '点击登录按钮'
        self.click(self.ele_login)

    def normal_information(self):
        '输入正常的账号密码'
        self.click(self.ele_switch) # 切换登录模式为账号密码模式
        self.input_username("chenzijia")
        self.input_psw("Zj123456!")
        self.click_login()
        time.sleep(0.5)
