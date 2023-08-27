import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser_driver_path = 'C:/Study/c4k/sellenium/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome()

# 수집 대상 사이트
target_base_URL = 'https://likms.assembly.go.kr/bill/billVoteResult.do#21_________10_1'
driver.get(target_base_URL)