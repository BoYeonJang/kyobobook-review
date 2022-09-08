from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
import csv
import os

URL = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791170400608#review'

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url=URL)

# df 선언
df = pd.DataFrame(columns=['part','title','date','rating','text'])

# part_xpath = driver.find_element(By.XPATH, '''//*[@id="main_contents"]/div[3]/h4''')
# part = part_xpath.text
# partName = part.split()[0]
# print('part: ', partName)
part_xpath = driver.find_element(By.XPATH, '''//*[@id="container"]/div[1]/div[3]/p/span/a''')
part = part_xpath.text
print('part: ', part)

# for book in range(1, 21): # top 20
# driver.find_element(By.XPATH, f'''//*[@id="main_contents"]/ul/li[1]/div[2]/div[2]/a/strong''').click() # 책 제목 클릭
# driver.implicitly_wait(time_to_wait=5) # 파싱이 되면 바로 다음 코드로 넘어간다 파싱이 안될 경우 최대 10초를 기다린다

title_xpath = driver.find_element(By.XPATH, '''//*[@id="container"]/div[2]/form/div[1]/h1/strong''') # 책 제목
title = title_xpath.text
print('title: ', title)

# driver.find_element(By.XPATH, '''//*[@id="event_info"]/li[3]/a''').click() # 리뷰 클릭
# driver.switch_to.frame(driver.find_element(By.XPATH, '''//*[@id="event_info"]/li[3]/a''')).click() # 리뷰 클릭
driver.implicitly_wait(time_to_wait=10)

# 페이지가 다음으로 넘어가면
for n in range(1, 300): # 59페이지까지만 수집
  try:
    sleep(1)
    for idx in range(1, 6): # 리뷰 5개씩
      rating_xpath = driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/ul/li[{idx}]/div[1]/dl/dd[3]/span''') # 별점
      text_xpath = driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/ul/li[{idx}]/div[1]/dl/dd[5]/div''') # 리뷰 글
      date_xpath = driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/ul/li[{idx}]/div[1]/dl/dd[1]''') # 날짜
      
      rating = rating_xpath.text
      text = text_xpath.text
      date = date_xpath.text
      print('date: ', date)
      print('rating: ', rating)
      print('text: ', text)
      sleep(0.5)

      df = df.append({'part':part, 'title':title, 'date':date, 'rating':rating, 'text':text}, ignore_index=True)
      sleep(1)

    page_bar = driver.find_elements(By.CSS_SELECTOR, '#box_detail_review > div.list_paging.align_center > div >*')
    pn = len(page_bar)

    if n%10 != 0:
        print(f'============= {n} 페이지의 리뷰 5개 =============')
        page_bar[pn-2].click()
        sleep(1)
  except:
    print('============= 다음 페이지가 없습니다 =============')
    sleep(1)
    break

driver.back()
driver.back()

# print("df확인-------\n", df)
df.to_csv(f'{title}_review.csv', encoding='utf-8-sig')