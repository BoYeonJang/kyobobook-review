from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
import csv
import os
from selenium.webdriver.common.keys import Keys
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) # concat 쓰라는 경고 무시

try:
  URL = 'https://digital.kyobobook.co.kr/digital/ebook/ebookDetail.ink?selectedLargeCategory=001&barcode=4801188331797&orderClick=LEa&Kc=#tab_content_06'

  chrome_options = webdriver.ChromeOptions()
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
  driver.get(url=URL)
  # driver.find_element(By.XPATH, '''//*[@id="neo_conbody"]/div/div[2]/div[4]/div[1]/ul/li[6]/a''').send_keys(Keys.ENTER) # 리뷰 클릭 나미야
  driver.find_element(By.XPATH, '''//*[@id="neo_conbody"]/div/div[2]/div[5]/div[1]/ul/li[6]/a''').send_keys(Keys.ENTER) # 리뷰 클릭 돈의 속성
  # df 선언
  df = pd.DataFrame(columns=['part','title','rating','text'])
  part = '경제/경엉'
  title = '돈의 속성'
  print('part: ', part)
  print('title: ', title)

  driver.implicitly_wait(time_to_wait=10)

  # 페이지가 다음으로 넘어가면
  for n in range(1, 20000):
    print(">>n: ",n)
    if n == 20000:
      break
    sleep(1)
    for idx in range(1, 11): # 리뷰 5개씩
        rating_xpath = driver.find_element(By.XPATH, f'''//*[@id="kloverReviewList"]/ul/li[{idx}]/div[1]/dl/dd[3]/span''') # 별점
        # print("rating_xpath:: ", rating_xpath ,"::", rating_xpath.text)
        text_xpath = driver.find_element(By.XPATH, f'''//*[@id="kloverReviewList"]/ul/li[{idx}]/div[1]/dl/dd[5]/div''') # 리뷰 글
        # print("text_xpath:: ", text_xpath ,"::", text_xpath.text)
        rating = rating_xpath.text
        text = text_xpath.text
        print(rating)
        print(text)
        df = df.append({'part':part, 'title':title,'rating':rating, 'text':text},ignore_index=True)
        sleep(1)

    print("--------------------next----------------------------------")
    #
    page_bar = driver.find_elements(By.CSS_SELECTOR,'#kloverReviewList > div > div > a.next')
    page_bar[0].send_keys(Keys.ENTER)

  df.to_csv(f"./ebook_돈의속성.csv", encoding='utf-8-sig')
except Exception as e:
  print("!!!---예외가 발생했습니다.--- : ", e, '-----!!!!')
  df.to_csv(f"./ebook_돈의속성.csv", encoding='utf-8-sig')
