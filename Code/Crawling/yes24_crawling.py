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
  URL = 'http://www.yes24.com/Product/Goods/2312211'

  chrome_options = webdriver.ChromeOptions()
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
  driver.get(url=URL)
  sleep(3)
  driver.find_element(By.XPATH, '''//*[@id="yDetailTabNavWrap"]/div/div[2]/ul/li[2]/a''').send_keys(Keys.ENTER) #리뷰 클릭

  df = pd.DataFrame(columns=['part','title','rating','text'])
  part = '소설'
  title = '코스모스'
  print('part: ', part)
  print('title: ', title)

  driver.implicitly_wait(time_to_wait=10)
  # for i in range(1,339):
  #   if i == 338:
  #     break
  cnt = 0
  for _ in range(35):
    for num in range(4,13):
      cnt+=1
      print(f">>{cnt} 페이지")
      for idx in range(1,7):
        try:
          rating_xpath = driver.find_element(By.XPATH, f'''//*[@id="infoset_oneCommentList"]/div[3]/div[{idx}]/div[1]/div[1]/span[2]''') # 별점
        except:
          rating_xpath = driver.find_element(By.XPATH, f'''//*[@id="infoset_oneCommentList"]/div[3]/div[{idx}]/div[1]/div[1]/span''') # 별점
        text_xpath = driver.find_element(By.XPATH, f'''//*[@id="infoset_oneCommentList"]/div[3]/div[{idx}]/div[1]/div[2]/span''') # 리뷰 글
        rating_str = rating_xpath.text
        rating = rating_str[2:-1]
        text = text_xpath.text
        print(rating)
        print(text)
        df = df.append({'part':part, 'title':title, 'rating':rating, 'text':text}, ignore_index=True)
        sleep(2.5)
      print("-------------next------------")
      page_bar = driver.find_elements(By.CSS_SELECTOR, f'#infoset_oneCommentList > div:nth-child(4) > div.rvCmt_sortLft > div > a:nth-child({num})')
      # pn = len(page_bar)
      # print("pn:: ", pn)
      page_bar[0].send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, '''//*[@id="infoset_oneCommentList"]/div[2]/div[1]/div/a[12]''').send_keys(Keys.ENTER)
  # next_bar = driver.find_elements(By.CSS_SELECTOR, '#infoset_oneCommentList > div:nth-child(2) > div.rvCmt_sortLft > div > a.bgYUI.next')
  # page_bar[0].send_keys(Keys.ENTER)
    

  df.to_csv(f'./yes24_{title}.csv', encoding='utf-8-sig')
except Exception as e:
  df.to_csv(f'./yes24_{title}.csv', encoding='utf-8-sig')
  print("!!!---예외가 발생했습니다.--- : ", e, '-----!!!!')