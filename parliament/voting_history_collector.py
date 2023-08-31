import selenium
from selenium import webdriver

from selenium.webdriver.common.by import By

import time

import re

browser_driver_path = 'C:/Study/c4k/sellenium/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome()

# 수집 페이지 범위
page_from = 1
page_to = 10

# 댓글 개수 패턴
reply_reg_filter = re.compile(r'\[\d\]$')

# 수집 대상 사이트
base_URL = 'https://gall.dcinside.com/board/lists/?id=agony&list_num=100&page='

for page in range(page_from, page_to):
    target_url = base_URL + str(page)
    driver.get(target_url)
    time.sleep(1)

    # table
    list_table = driver.find_element(By.XPATH,'//*[@id="container"]/section[1]/article[2]/div[2]/table/tbody')

    # contents
    trs = list_table.find_elements(By.CSS_SELECTOR,'.us-post')
    for tr in trs:
        #number
        number = tr.get_attribute('data-no')

        #title
        title = tr.find_element(By.CLASS_NAME,'gall_tit').text

        #reply
        reply_cnt = "#"
        replay_open_idx = title.rfind('[')
        if title[-1]!=']' and replay_open_idx<0:
            reply_cnt="0"
        else:
            reply_cnt = title[replay_open_idx+1:-1]
            title = title[:replay_open_idx]
  
        #writer
        writer = tr.find_element(By.CLASS_NAME,'gall_writer').text

        #date
        date = tr.find_element(By.CLASS_NAME,'gall_date').get_attribute('title')

        #count
        count = tr.find_element(By.CLASS_NAME,'gall_count').text

        #recommend
        recommend = tr.find_element(By.CLASS_NAME,'gall_recommend').text

        #tr
        tr_string = number+"|"+title+"|"+reply_cnt+"|"+writer+"|"+date+"|"+count+"|"+recommend

        #print
        print(tr_string)
    