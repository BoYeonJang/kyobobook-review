from errno import ESTALE
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# URL = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?mallGb=KOR&linkClass=B&range=1&kind=2&orderClick=DAd'
URL = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?mallGb=KOR&linkClass=c&range=1&kind=2&orderClick=DAd' #자기계발
URL = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?mallGb=KOR&linkClass=a&range=1&kind=2&orderClick=DAd' # 요리/와인


# driver = webdriver.Chrome('/Users/boyeonjang/git/kyobobook-review/chromedriver')
driver = webdriver.Chrome('C:/Users/eunho/Workspace/kyobobook-review/chromedriver.exe')


driver.get(url=URL)

for book in range(1, 21): # top 20
  driver.find_element(By.XPATH, f'''//*[@id="main_contents"]/ul/li[{book}]/div[2]/div[2]/a/strong''').click() # 책 제목 클릭
  driver.implicitly_wait(time_to_wait=5) # 파싱이 되면 바로 다음 코드로 넘어간다 파싱이 안될 경우 최대 10초를 기다린다

  title_xpath = driver.find_element(By.XPATH, '''//*[@id="container"]/div[2]/form/div[1]/h1/strong''') # 책 제목
  title = title_xpath.text
  print('title: ', title)

  driver.find_element(By.XPATH, '''//*[@id="event_info"]/li[3]/a''').click() # 리뷰 클릭
  driver.implicitly_wait(time_to_wait=5)

  # try:
  # 페이지가 다음으로 넘어가면
  for n in range(1, 300):
    try:
      sleep(1)
      for idx in range(1, 6): # 리뷰 5개씩
        rating_xpath = driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/ul/li[{idx}]/div[1]/dl/dd[3]/span''') # 별점
        text_xpath = driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/ul/li[{idx}]/div[1]/dl/dd[5]/div''') # 리뷰 글
        date_xpath = driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/ul/li[{idx}]/div[1]/dl/dd[1]''') # 날짜
        
        rating = rating_xpath.text
        text = text_xpath.text
        date = date_xpath.text
        print('rating: ', rating)
        print('text: ', text)
        print('date: ', date)
        driver.implicitly_wait(time_to_wait=5)
    # except:
    #   break
      page_bar = driver.find_elements(By.CSS_SELECTOR,'#box_detail_review > div.list_paging.align_center > div >*')
      pn = len(page_bar)

      if n%10 != 0:
          print("++++++++")
          # page_bar[n%10+1].click()
          page_bar[pn-2].click()
          sleep(1)
    except:
      print("페이지가 없습니다")
      break

    # if n == 10 :
    #     print("=========")
    #     nn = pn-2
    #     driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/div[3]/div/a[{nn}]''').click() 
    #     page_bar[pn-2].click()
    #     sleep(1)

    # elif n%10 != 0:
    #     print("++++++++")
    #     page_bar[n%10+1].click()
    #     sleep(1)

    # 현재 페이지(n)가 5의 배수인 경우 다음페이지 버튼을 클릭
    
    # if n ==  12:
    #     print("========="*20)
    #     page_bar[12].click()
    #     sleep(1)
    #     break
    
    # if n == 10 or n == 11:
    #   print("n이 10이거나 11이다")
    #   break

    # elif n%10 != 0:
    #     print("++++++++")
    #     page_bar[n%10+1].click()
    #     sleep(1)

    # 현재 페이지(n)가 5의 배수인 경우 다음페이지 버튼을 클릭
    
        #box_detail_review > div.list_paging.align_center > div > a:nth-child(13) > img
  
    # paging_num_xpath = driver.find_element(By.XPATH, '''//*[@id="box_detail_review"]/div[3]/div''')
    # paging_num = paging_num_xpath.text
    
    # print("paging_num 확인==============", paging_num)
    # print("paging_num 타입 확인==============", type(paging_num))
    # if page%10 != 0:
    #   paging_num[page%10+1].click()
    # else:
    #   paging_num[11].click()

    # 다음페이지 넘기기
    # driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/div[3]/div/a[10]''').click()
    # driver.implicitly_wait(time_to_wait=5)
    # sleep(3)
    # driver.find_element(By.XPATH, f'''//*[@id="box_detail_review"]/div[3]/div/a[12]''').click()
    # driver.implicitly_wait(time_to_wait=5)
    # sleep(3)

  driver.back()
  driver.back()
  # continue

  # 4개 열을 가진 pandas DataFrame으로 바꿔준 뒤 엑셀 파일로 저장
  # df = pd.DataFrame({'title':title, 'rating':rating, 'text':text, 'date':date})
  # df.to_csv("best_books.csv", mode='w', encoding='utf-8-sig')
  
# driver.quit()
