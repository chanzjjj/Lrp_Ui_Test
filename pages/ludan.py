from common.base import Base
from common.barcode_rule import DailyCounter
from datetime import datetime
from pages.login import LoginPage
import time
from selenium import webdriver


class LudanPage(Base, DailyCounter):
    '''定义所需要的元素'''
    ele_ludan = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/dl[1]')   #首页录单按钮
    ele_barcode = ("xpath", '//*[@id="pane-0"]/div/div/div[1]/div[1]/div[2]/div/form/div[1]/div/div/div/div[2]/div[1]/input')   #条码号输入框
    ele_songjian_xiala_button = ("xpath", '//*[@id="pane-0"]/div/div/div[1]/div[1]/div[2]/div/form/div[2]/div/div/div/div[2]/div/span[1]/div/div/button')   #送检单位下拉按钮
    ele_songjian_input = ("xpath", '//*[@id="pane-0"]/div/div/div[1]/div[1]/div[2]/div/form/div[2]/div/div/div/div[2]/div/span[1]/div/input')   #送检单位输入框
    ele_songjian_window = ("xpath", '//*[@class="el-select-dropdown__item hover"]/div')   #送检单位下拉框
    ele_name = ("xpath", '//*[@id="pane-0"]/div/div/div[1]/div[1]/div[2]/div/form/div[3]/div/div/div/div[2]/input')   #姓名输入框
    ele_sex_input = ("xpath", '//*[@id="pane-0"]/div/div/div[1]/div[1]/div[2]/div/form/div[5]/div/div/div/div[2]/div[1]/span[1]/div/input')   #性别输入框
    ele_sex_button = ("xpath", '//*[@id="pane-0"]/div/div/div[1]/div[1]/div[2]/div/form/div[5]/div/div/div/div[2]/div[1]/span[1]/div/div/button')   #性别下拉按钮
    ele_sex_window = ("xpath", '//*[@class="el-select-dropdown__item hover"]/div/div')   #性别下拉框
    ele_age_button = ("xpath", '//*[@id="pane-0"]/div/div/div[1]/div[1]/div[2]/div/form/div[6]/div/div/div/div[2]/div[1]/div[1]/span[1]/div/div/button')   #年龄下拉按钮
    ele_age_window = ("xpath", '//*[@class="el-select-dropdown__item hover"]/div/div')   #年龄下拉框
    ele_caiyang_time_day = ("xpath", '//*[@id="pane-0"]/div/div/div[1]/div[1]/div[2]/div/form/div[14]/div/div/div/div[2]/div[3]/input')   #采样时间-天 输入框
    ele_caiyang_time_hour = ("xpath", '//*[@id="pane-0"]/div/div/div[1]/div[1]/div[2]/div/form/div[14]/div/div/div/div[2]/div[4]/input')    #采样时间-时 输入框
    ele_caiyang_time_minute = ("xpath", '//*[@id="pane-0"]/div/div/div[1]/div[1]/div[2]/div/form/div[14]/div/div/div/div[2]/div[5]/input')   #采样时间-分 输入框
    ele_shenqing_time_day = ("xpath", '//*[@id="pane-0"]/div/div/div[1]/div[1]/div[2]/div/form/div[15]/div/div/div/div[2]/div[3]/input')   #申请日期-天 输入框
    ele_xiangmu_input = ("xpath", '//*[@id="pane-0"]/div/div/div[1]/div[2]/div/div[2]/div/form/div/div/div/div/div/div/div[1]/span[1]/div/input')   #送检项目输入框
    ele_xiangmu_window = ("xpath", '//*[@class="el-select-dropdown__item hover"]/div')   #送检项目下拉框
    ele_save_button = ("xpath", '//*[@class="pane-footer"]/div[2]/div/button[3]')   #保存按钮
    ele_quanxuan_button = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div[2]/div[1]/div[4]/div/div/div[1]/div[2]/table/thead/tr/th[1]/div/label/span/span')   #全部勾选按钮
    ele_submit_button = ("xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div[2]/div[1]/div[3]/button[1]')   #批量提交按钮
    ele_submit_window = ("xpath", '//*[@class="el-button el-button--default el-button--small el-button--primary "]')   #确认是否批量提交弹窗的确认按钮
    ele_save_toast = ("xpath", '//*[@class="el-message__content"]')   #保存成功toast

    def to_ludan(self):
        '''点击首页的录单按钮'''
        self.click(self.ele_ludan)

    def barcode_rule(self):
        '''条码号生成规则 AT2504110100'''
        count = DailyCounter()
        number = count.format_number()  #每天从01开始自增
        today = datetime.now().strftime("%y%m%d")  #获取今天日期，格式250411
        bar_code = "AT" + str(today) + str(number) + "00"  #条码格式：AT2504110100
        # print(bar_code)
        return bar_code

    def input_barcode(self, bar_code):
        '''输入条码号'''
        self.send(self.ele_barcode, bar_code)

    def click_songjian_button(self):
        '''点击送检单位下拉按钮'''
        self.click(self.ele_songjian_xiala_button)

    def input_songjian(self, text):
        '''送检单位输入文案'''
        self.send(self.ele_songjian_input, text)

    def click_songjian_xialakuang(self):
        '''点击送检单位下拉框'''
        self.click(self.ele_songjian_window)

    def get_name(self):
        '''姓名生成规则 自动化250411'''
        today = datetime.now().strftime("%y%m%d")  #获取今天日期，格式250411
        name = "自动化" + str(today)
        return name

    def input_name(self, text):
        '''输入姓名'''
        self.send(self.ele_name, text)

    def click_sex(self):
        '''点击性别下拉按钮'''
        self.click(self.ele_sex_button)

    def click_sex_window(self):
        '''点击性别下拉框'''
        self.click(self.ele_sex_window)

    def click_age(self):
        '''点击性别下拉按钮'''
        self.click(self.ele_age_button)

    def click_age_window(self):
        '''点击性别下拉框'''
        self.click(self.ele_age_window)

    def get_day(self):
        '''获取当天日期，具体到天'''
        day = datetime.now().strftime("%d")  #获取今天日期，具体到天
        return day

    def input_caiyang_day(self, text):
        '''输入采样时间-天'''
        self.send(self.ele_caiyang_time_day, text)

    def input_caiyang_hour(self, text):
        '''输入采样时间-时'''
        self.send(self.ele_caiyang_time_hour, text)

    def input_caiyang_minute(self, text):
        '''输入采样时间-分'''
        self.send(self.ele_caiyang_time_minute, text)

    def input_shenqing_time_day(self, text):
        '''输入申请时间-天'''
        self.send(self.ele_shenqing_time_day, text)

    def input_xiangmu(self, text):
        '''送检项目输入框输入内容'''
        self.send(self.ele_xiangmu_input, text)

    def click_xiangmu_window(self):
        '''点击送检项目下拉框'''
        self.click(self.ele_songjian_window)

    def click_save_button(self):
        '''单击保存按钮'''
        self.click(self.ele_save_button)

    def click_quanxuan_button(self):
        '''点击全部勾选按钮'''
        self.click(self.ele_quanxuan_button)

    def click_submit_button(self):
        '''点击批量提交按钮'''
        self.click(self.ele_submit_button)

    def click_submit_window(self):
        '''点击批量提交确认弹窗的确定按钮'''
        self.click(self.ele_submit_window)

    def normal_infotmation(self):
        '''输入正确的录单信息'''
        self.to_ludan()
        bar_code = self.barcode_rule()  #获取条码号
        self.input_barcode(bar_code)
        self.click_songjian_button()
        self.input_songjian("100417")
        self.click_songjian_xialakuang()
        name = self.get_name()  #获取姓名
        self.input_name(name)
        self.click_sex()
        self.click_sex_window()
        self.click_age()
        self.click_age_window()
        day = self.get_day()   #获取当天
        self.input_caiyang_day(day)
        self.input_caiyang_hour("09")
        self.input_caiyang_minute("00")
        self.input_shenqing_time_day(day)
        self.input_xiangmu("100689")
        self.click_xiangmu_window()
        self.click_save_button()
        self.click_quanxuan_button()
        self.click_submit_button()
        self.click_submit_window()
        print(self.get_text(self.ele_save_toast))
        return bar_code
