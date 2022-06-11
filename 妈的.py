# 创建人:王森
# 创建时间：2022/5/27 17:06
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=options)

web.get("https://www.taobao.com")

web.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()

time.sleep(5)

web.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys("17639408710") #账号
web.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys("ws19990108") #密码

time.sleep(2)
web.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()

'''span = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
action = ActionChains(web)
action.click_and_hold(span).perform()
action.drag_and_drop_by_offset(span, 400, 0).perform()'''


