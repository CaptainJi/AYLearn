from selenium.common.exceptions import NoSuchFrameException, NoSuchElementException
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class Myclass(BasePage):
# 我的课程页面
    def select_class(self):
        # 筛选必修、选修、未学习、进行中的课程
        self.find(By.XPATH,'//*[@id="loadStudyTask"]/span').click()
        self.find(By.XPATH,'//*[@id="studyTaskIndexFilter"]/div/dl[2]/dd[2]/label').click()
        self.find(By.XPATH,'//*[@id="studyTaskIndexFilter"]/div/dl[2]/dd[3]/label').click()
        self.find(By.XPATH,'//*[@id="studyTaskIndexFilter"]/div/dl[4]/dd[2]/label').click()
        self.find(By.XPATH,'//*[@id="studyTaskIndexFilter"]/div/dl[4]/dd[3]/label').click()
        self.wait_for_condition(lambda x: x.find_element_by_id("studyTaskList"))
        print('1')
        try:
            ay_class=self.finds(By.XPATH, "//*[@id='studyTaskList']//a[contains(text(),'')]")
            self._driver.implicitly_wait(5)
            ay_class[0].click()
        except NoSuchElementException as e:
            print(e)
        self.wait_for_condition(lambda x: x.find_element_by_id("goNextStep"))
        print('3')
        self.find(By.XPATH, "//*[@id='goNextStep']").click()
