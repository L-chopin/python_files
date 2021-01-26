import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://47.113.97.130:8081/dist/index.html#/login?redirect=%2Ffeatures%2Fhome")

# 定位用户名输入框，并输入‘xiaobin’
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/form/div[1]/div/div/input").send_keys("xiaobin")
time.sleep(3)

# 定位密码输入框，并输入‘123456’
driver.find_element_by_xpath("//*[@placeholder='登录密码']").send_keys("123456")
time.sleep(3)

driver.find_element_by_link_text("粤ICP备18053137号").click()

# 定位登录按钮，并点击
# driver.find_element_by_class_name("loginSubmitButton").click()
time.sleep(4)

driver.quit()
