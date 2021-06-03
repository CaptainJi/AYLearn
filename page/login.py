from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.index import Index


class Login(BasePage):
    '''
    首页PO
    '''
    _base_url = 'http://auyan.21tb.com/'

    # def goto_register(self):
    #     '''
    #     点击立即注册
    #     进入到立即注册的PO
    #     :return:注册PO'''
    #     self.find(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
    #     # return Register(self._driver)
    #
    # def goto_login(self):
    #     '''
    #     点击进入登录
    #     :return:登录PO
    #     '''
    #
    #     return Login(self._driver)
    #
    # def goto_add_member(self):
    #     '''
    #     添加成员
    #     :return:通讯录PO
    #     '''
    #
    #     def add_member_condition(x):
    #         '''
    #         改写显示等待条件
    #         :param x:占位参数
    #         :return:
    #         '''
    #         elements_len = len(self.finds(By.ID, 'username'))
    #         # 如果username不出现,就会触发显示等待until中的循环
    #         if elements_len <= 0:
    #             self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
    #
    #         return elements_len > 0
    #
    #     self.find(By.CSS_SELECTOR, '#menu_contacts').click()
    #     self.wait_for_condition(add_member_condition)
    #     return AddMember(self._driver)

    def goto_index(self, username, password):
        self.find(By.ID, 'loginName').send_keys(username)
        self.find(By.ID, "password").send_keys(password)
        loginbutton = self.find(By.ID, "div4")
        loginbutton.click()
        return Index(self._driver)


if __name__ == '__main__':
    import random

    actualPrice = round(random.uniform(1, 4), 2)
    gasQty = round(random.uniform(100, 4000), 2)
    amount = round(actualPrice * gasQty, 2)
    serviceFee = round(0.3 * gasQty, 2)
    orderStatus = random.randint(2, 3)
    payType = random.choice([0, 1, 2, 11])

    if gasQty < 1000:
        rebate = 0.26
    if gasQty > 1000:
        rebate = 0.28
    else:
        rebate = 0.3
    discountAmount = round(gasQty * rebate, 2)

    print(".........")
    print(actualPrice)
    print(gasQty)
    print(amount)
    print(orderStatus)
    print(payType)
    print(rebate)
    print(".........")
