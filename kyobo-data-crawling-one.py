from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
import csv
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) # concat 쓰라는 경고 무시

try:
  URL = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9788934972464#review'

  chrome_options = webdriver.ChromeOptions()
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
  driver.get(url=URL)

  # df 선언
  df = pd.DataFrame(columns=['part','title','rating','text'])
  part_xpath = driver.find_element(By.XPATH, '''//*[@id="container"]/div[1]/div[3]/p/span/a''')
  part = part_xpath.text
  print('part: ', part)
  title_xpath = driver.find_element(By.XPATH, '''//*[@id="container"]/div[2]/form/div[1]/h1/strong''') # 책 제목
  title = title_xpath.text
  print('title: ', title)

  driver.implicitly_wait(time_to_wait=10)

  # 페이지가 다음으로 넘어가면
  for n in range(1, 404):
    print(">>n: ",n)
    if n == 405:
      break
    try:
      sleep(1)
      for idx in range(1, 6): # 리뷰 5개씩
        rating_xpath = driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/ul/li[{idx}]/div[1]/dl/dd[3]/span''') # 별점
        text_xpath = driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/ul/li[{idx}]/div[1]/dl/dd[5]/div''') # 리뷰 글
        rating = rating_xpath.text
        text = text_xpath.text
        print('rating: ', rating)
        print('text: ', text)
        sleep(0.5)
        df = df.append({'part':part, 'title':title, 'rating':rating, 'text':text}, ignore_index=True)
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
except Exception as e:
  print("!!!---예외가 발생했습니다.--- : ", e, '-----!!!!')
  df.to_csv(f'{title}_review.csv', encoding='utf-8-sig')