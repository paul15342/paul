
import time
import unittest
import os
import sys
from selenium import webdriver


# 继承unittest类
class testClass(unittest.TestCase):

    def __init__(self):
        print ("setup")
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        time.sleep(3)


    def testsearch2(self):
        input=self.driver.find_element_by_id('kw')
        search=self.driver.find_element_by_id('su')
        input.send_keys("byebye")
        search.click()

    def testsearch(self):
        input=self.driver.find_element_by_id('kw')
        search=self.driver.find_element_by_id('su')
        input.send_keys("hello")
        search.click()
        print ("assertion")
        self.assertTrue(search.is_displayed(),"baidu yixia should display")

    def tearDown(self):
        print ('test down...')
        #driver.quit()
        self.driver.close()

if __name__ == '__main__':
    # unittest.main()， 这里要说明一下， 如果测试方法是以test开头的，那么unittest可以识别出来，这里就可以直接调用它
    # 的main方法来执行所有测试方法了，运行顺序就是按测试方法的名字排序
    # unittest.TestCase.assertTrue()
    # testsuite = unittest.TestSuite()
    # testsuite.addTest(testClass("testsearch"))
    # f=open("./result.HTML","wb")
    # runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='report',description='demo')
    # runner.run(testsuite)
    # f.close()
    a = testClass()
    a.testsearch()
    a.tearDown()