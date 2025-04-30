from selenium.common import JavascriptException
from common.base import Base
import time
import pyautogui

class JieguoPage(Base):
    '''定义所需要的元素'''
    ele_jieguo_button = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/dl[7]')   #   首页结果录单按钮
    ele_professional_group = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/form/div[1]/div/div/div/div/div[1]/div/div/span[1]/div/input')   #专业组输入框
    ele_professional_group_window = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/form/div[1]/div/div/div/div/div[1]/div/div/span[1]/div/input')   #专业组下拉框
    ele_barcode = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/form/div[3]/div[2]/div[2]/div/input')   #条码号输入框
    ele_result = ("xpath", '//*[@id="pane-first"]/div[1]/div/div[1]/div/div/div[3]/table/tbody/tr/td[3]/div/div/div[1]/span[1]/div/input')   #结果输入框
    ele_submit_button = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/button[4]')   #全部提交按钮

    def to_shouye(self):
        '''跳转首页'''
        try:
            self.driver.execute_script("document.getElementsByClassName('el-tabs__item is-top is-closable')[0].click();")
        except JavascriptException as e:
            print(f"JavaScript执行异常: {e}")

    def to_jieguo(self):
        '''跳转结果录入页面'''
        self.click(self.ele_jieguo_button)

    def input_profession_group(self, text):
        '''输入专业组'''
        self.send(self.ele_professional_group, text)

    def click_profession_group(self):
        '''点击专业组下拉框'''
        self.click(self.ele_professional_group_window)

    def input_barcode(self, text):
        '''输入条码号'''
        self.send(self.ele_barcode, text)

    def input_result(self, text):
        '''输入结果'''
        self.send(self.ele_result, text)

    def click_submit_button(self):
        '''点击全部提交按钮'''
        self.click(self.ele_submit_button)

    def normal_information(self, bar_code):
        '''正常结果录入流程'''
        self.to_shouye()
        self.to_jieguo()
        self.input_profession_group("07")
        self.click_profession_group()
        self.input_barcode(bar_code)
        pyautogui.press("enter")
        self.input_result("60")
        pyautogui.press("enter")
        self.click_submit_button()

