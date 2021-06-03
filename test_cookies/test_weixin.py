import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWorkWeiXin():

    def test_lonin(self):
        pass

    def test_click_addres(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#apps')
        time.sleep(10)
        self.driver.find_element_by_css_selector('#menu_contacts > span').click()
