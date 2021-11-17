from selenium import webdriver
import os,time
chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe' #这里写本地的chromedriver 的所在路径
os.environ['webdriver.Chrome.driver'] = chromedriver #调用chrome浏览器
driver = webdriver.Chrome(chromedriver)
driver.get('http://rsc.njucm.edu.cn/manage/login.aspx') #该处为具体网址
driver.refresh() #刷新页面
driver.maximize_window() #浏览器最大化

driver.find_elements_by_class_name('input')[0].send_keys('admin')
driver.find_elements_by_class_name('input')[1].send_keys('1233456')
driver.find_element_by_class_name('input')[2].click()