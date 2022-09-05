from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request



# webdriver가 위치한 경로로 설정
driver = webdriver.Chrome('/Users/boyeonjang/git/kyobobook-review/chromedriver')

#(추가) 분야별로 for문
driver.get("http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?mallGb=KOR&linkClass=c&range=1&kind=0&orderClick=DAb")

for i in range(1,21): # top 20
    driver.find_element(By.XPATH, f'''//*[@id="main_contents"]/ul/li[{i}]/div[2]/div[2]/a/strong''').click() # 책 제목 클릭

    time.sleep(3)

    driver.find_element(By.XPATH, '''//*[@id="event_info"]/li[3]/a''').click() # 리뷰 클릭

    time.sleep(3)

    for idx in range(1,6): # 리뷰 5개씩

        # one_review = driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/ul/li[{idx}]/div[1]''')

        rating_xpath = driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/ul/li[{idx}]/div[1]/dl/dd[3]/span''')
        text_xpath = driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/ul/li[{idx}]/div[1]/dl/dd[5]/div''')
        
        #(추가)csv로 저장
        rating = rating_xpath.text
        text = text_xpath.text
        print("rating: ", rating)
        print("text: ", text)
        time.sleep(5)

        #(추가) 다음페이지 넘기기

    driver.close()

    driver.back()
    time.sleep(2)
