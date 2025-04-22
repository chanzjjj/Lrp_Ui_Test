from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
import platform
from pages.login import LoginPage
from pages.ludan import LudanPage
from pages.fenfa import FenfaPage



# @pytest.fixture(scope="session", name="driver")
# def browser():
#     chrome_options = Options()
#     chrome_options.add_argument('--headless') # 无界面模式
#     chrome_options.add_argument('--window-size=1920,1080')
#     driver = webdriver.Chrome(options=chrome_options)
#     yield driver
#     driver.quit()

@pytest.fixture(scope="session", name="driver")
def browser():
    '''定义全局driver'''
    if platform.system() == 'Windows':
        # windows系统
        # _driver = webdriver.Chrome()

        # 无界面模式
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        # chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
        # chrome_options.add_argument('--headless')
        _driver = webdriver.Chrome(options=chrome_options)


    else:
        # linux启动
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
        chrome_options.add_argument('--headless')  # 无界面

        # _driver = webdriver.Chrome()
        _driver = webdriver.Chrome(chrome_options=chrome_options)

    yield _driver
    # quit是退出浏览器
    _driver.quit()



@pytest.fixture(scope="session")
def base_url():
    return "https://lrp-test.huayinlab.com/"

@pytest.fixture(scope="session")
def login(driver, base_url):
    login = LoginPage(driver, base_url)
    return login

@pytest.fixture(scope="session")
def ludan(driver, base_url):
    ludan = LudanPage(driver, base_url)
    return ludan

@pytest.fixture(scope="session")
def fenfa(driver, base_url):
    fenfa = FenfaPage(driver, base_url)
    return fenfa