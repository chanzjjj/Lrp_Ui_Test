from selenium.common import JavascriptException
from common.base import Base
import time
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains


class FenfaPage(Base):
    '''定义所需要的元素'''
    ele_shouye_button = ("xpath", '//*[@class="el-tabs__nav is-top"]/div')   #导航栏最左侧首页按钮 //*[@id="tab-/index"]
    ele_fenfa_button = ("xpath", '//*[@class="quickEntryItems"]/dl[3]')   #首页样本分发入口 //*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/dl[3]/dt
    ele_barcode = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/div[1]/ul/li[1]/div/div/form/div/div/div/div/div/input')   #条码号输入框
    ele_receive = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div/div/div[1]/div/form/div[2]/div/div/div/div/div/span[1]/div/input')   #接收人输入框
    ele_receive_window = ("xpath", '//*[@class="el-select-dropdown__item hover"]/div')   #接收人下拉框
    ele_receive_psw = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div/div/div[1]/div/form/div[3]/div/div/div/div/div/input')   #接收人密码输入框
    ele_professional_group_checkbox = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span')   #第一个专业组复选框
    ele_receive_button = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div/div/div[2]/button[1]')   #确认接收按钮
    ele_success_toast = ("xpath", '//*[@class="el-message el-message--success is-closable"]')  #toast提示

    def to_shouye(self):
        '''跳转首页'''
        try:
            self.driver.execute_script("document.getElementsByClassName('el-tabs__item is-top is-closable')[0].click();")
        except JavascriptException as e:
            print(f"JavaScript执行异常: {e}")

    def to_fenfa_page(self):
        '''跳转样本分发页面'''
        try:
            self.driver.execute_script("document.getElementsByClassName('quickEntryImage')[2].click();")
        except JavascriptException as e:
            print(f"JavaScript执行异常: {e}")

    def input_barcode(self, barcode):
        '''输入条码号'''
        self.send(self.ele_barcode, barcode)

    def check_professional_group(self):
        '''勾选分发列表第一个实验室专业组'''
        self.click(self.ele_professional_group_checkbox)

    def input_receive_people(self, text):
        '''输入接收人'''
        self.send(self.ele_receive, text)

    def click_receive_window(self):
        '''点击接收人下拉框'''
        self.click(self.ele_receive_window)

    def input_receive_people_pwd(self, text):
        '''输入接收人密码'''
        self.send(self.ele_receive_psw, text)

    def click_receive_button(self):
        '''点击确认接收按钮'''
        self.click(self.ele_receive_button)

    def normal_information(self, barcode):
        self.to_shouye()
        time.sleep(2)
        self.to_fenfa_page()
        self.input_barcode(barcode)
        pyautogui.press("enter")
        time.sleep(1)
        self.check_professional_group()
        self.input_receive_people("chenzijia")
        time.sleep(1)
        self.click_receive_window()
        self.input_receive_people_pwd("Zj123456!")
        time.sleep(1)
        self.click_receive_button()
        time.sleep(2)
