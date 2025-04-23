from common.base import Base
import time
import pyautogui


class FenfaPage(Base):
    '''定义所需要的元素'''
    ele_shouye_button = ("xpath", '//*[@id="tab-/index"]')   #导航栏最左侧首页按钮
    ele_fenfa_button = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/dl[3]/dt/img')   #首页样本分发入口
    ele_barcode = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/div[1]/ul/li[1]/div/div/form/div/div/div/div/div/input')   #条码号输入框
    ele_receive = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div/div/div[1]/div/form/div[2]/div/div/div/div/div/span[1]/div/input')   #接收人输入框
    ele_receive_window = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div/div/div[1]/div/form/div[2]/div/div/div/div/div/span[1]/div/input')   #接收人下拉框
    ele_professional_group_checkbox = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span')   #第一个专业组复选框
    ele_receive_button = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div/div/div[2]/button[1]/span')   #确认接收按钮

    def to_shouye(self):
        '''跳转首页'''
        self.click(self.ele_shouye_button)

    def to_fenfa_page(self):
        '''跳转样本分发页面'''
        self.click(self.ele_fenfa_button)

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

    def click_receive_button(self):
        '''点击确认接收按钮'''
        self.click(self.ele_receive_button)

    def normal_information(self, barcode):
        self.to_shouye()
        self.to_fenfa_page()
        self.input_barcode(barcode)

