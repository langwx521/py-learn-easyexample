# 第一步导入webdriver 模块
from selenium import webdriver
import time
# 第二步打开火狐浏览器
driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver = webdriver.Chrome()
# 第三步打开百度首页
driver.get("https://www.baidu.com")
# 等待3秒
time.sleep(3)
# 等待3秒后刷新
driver.refresh()

driver.get("http://www.hordehome.com")

time.sleep(2)
# 返回上一页
driver.back()
time.sleep(3)
# 切换到下一页
driver.forward()

driver.set_window_size(540,960)

time.sleep(2)

driver.maximize_window()


# driver.get_screenshot_as_file("D:\\test190610\\one1.jpg")

time.sleep(5)

driver.quit()





