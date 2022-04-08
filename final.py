
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

# 지역별 거리두기 단계
def distance_level():
    browser.find_element_by_link_text("거리두기단계").click()
    soup = BeautifulSoup(browser.page_source, "lxml")
    local_infos = soup.find_all("div",attrs={"class":"local_info"})

    print("[지역별 거리두기 단계]")
    for local_info in local_infos[1:]:
        local_name = local_info.find("strong").get_text().strip()
        level = int(local_info.find("p").get_text().strip())
        if level >= 4:
            print("*",local_name, ":",level)
            continue
        print(local_name,":",level)

# 확진자 수 
def confirmed_number():
    browser.find_element_by_link_text("국내현황").click() 
    browser.find_element_by_link_text("일별 신규 확진자수").click()
    time.sleep(1)
    soup = BeautifulSoup(browser.page_source, "lxml")
    confirmed_numbers_by_date = soup.find("div", attrs={"class":"confirmed_status new"}).find_all("div", attrs={"class":re.compile("^column _column")}) #
    print("[최근 확진자 수]")

    prev_number = 0

    for confirmed_number_by_date in confirmed_numbers_by_date:
        date = confirmed_number_by_date.find("dt", attrs={"class":"x_axis_value"}).get_text()
        confirmed_number = int(str(confirmed_number_by_date.find("span",attrs={"class":"text"}).get_text()).replace(",",""))
        increase_number = confirmed_number- prev_number
        #print(f"[{date} : {confirmed_number}명] ")
        if increase_number >= 0:
            print(f"[{date} : {confirmed_number}명] + {increase_number}")
        else:
            print(f"[{date} : {confirmed_number}명]  {increase_number}")
        prev_number = confirmed_number

# 코로나 관련 상위 5개 뉴스
def show_news():
    browser.find_element_by_xpath("//*[@id='lnb']/div[1]/div/ul/li[7]/a").click()
    time.sleep(1)
    soup = BeautifulSoup(browser.page_source, "lxml")
    news_lists = soup.find("ul", attrs={"class":"list_news"}).find_all("li", attrs={"class":"bx"})
    print("코로나 관련 상위 5개 뉴스")
    for news in news_lists[:5]:
        title = news.find("a", attrs={"class":"news_tit"}).get_text()
        link = news.find("a", attrs={"class":"news_tit"})["href"]
        print(f"{title} -> {link}")
        


if __name__ == "__main__": #해당 모듈이 임포트된 경우가 아니라 인터프리터에서 직접 실행된 경우에만실행
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")

    browser = webdriver.Chrome(options=options)
    #browser.maximize_window()

    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98%ED%99%95%EC%A7%84%EC%9E%90"
    browser.get(url)
    
    time.sleep(1)
    
    confirmed_number()
    print("===================")
    distance_level()
    print("===================")
    show_news()
