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
  URL = 'http://www.yes24.com/Product/Goods/8157957/#review'

  chrome_options = webdriver.ChromeOptions()
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
  driver.get(url=URL)

  df = pd.DataFrame(columns=['part','title','rating','text'])
  part = '소설'
  title = '나미야 잡화점의 기적'
  print('part: ', part)
  print('title: ', title)

  driver.implicitly_wait(time_to_wait=10)

  # 페이지가 다음으로 넘어가면
  for n in range(1, 173):
    print(">>n: ",n)
    if n == 172:
      break
    sleep(1)
    for idx in range(2, 7): # 리뷰 5개씩
        rating_xpath = driver.find_element(By.XPATH, f'''//*[@id="infoset_reviewContentList"]/div[{idx}]/div[1]/div/span/span[1]''') # 별점
        text_xpath = driver.find_element(By.XPATH, f'''//*[@id="infoset_reviewContentList"]/div[{idx}]/div[2]/a/div''') # 리뷰 글
        rating = rating_xpath.text
        text = text_xpath.text
        print(rating)
        print(text)
        df = df.append({'part':part, 'title':title,'rating':rating, 'text':text},ignore_index=True)
        sleep(1)

    print("--------------------next----------------------------------")
    # 다음 페이지 넘기기
    # page_bar = driver.find_elements(By.CSS_SELECTOR,'#kloverReviewList > div > div > a.next')
    # page_bar[0].send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, '''//*[@id="infoset_reviewContentList"]/div[7]/div[1]/div/a[12]''').send_keys(Keys.ENTER)


  df.to_csv(f"./yes24_{title}.csv", encoding='utf-8-sig')
except Exception as e:
  print("!!!---예외가 발생했습니다.--- : ", e, '-----!!!!')
  df.to_csv(f"./yes24_{title}.csv", encoding='utf-8-sig')