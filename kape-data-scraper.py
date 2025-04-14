from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

TARGET_URL = "https://www.ekapepia.com/web/main.do?menuSn=&boardInfoNo=&bbsSn=&userGroupType=39"

driver.get(TARGET_URL)
time.sleep(5)

# 한우(전국) 도매 가격
ko_cow_wholesale_price = driver.find_element(By.CSS_SELECTOR, "#secondOnePrice").text
# 한우(전국) 도매 전일 대비
ko_cow_wholesale_price_diff = driver.find_element(By.CSS_SELECTOR, "#secondOneTrate").text
# 돼지(전국) 도매 가격
ko_pig_wholesale_price = driver.find_element(By.CSS_SELECTOR, "#secondTwoPrice").text
# 돼지(전국) 도매 전일 대비
ko_pig_wholesale_price_diff = driver.find_element(By.CSS_SELECTOR, "#secondTwoTrate").text
# 육계(1마리) 도매 가격
ko_chicken_wholesale_price = driver.find_element(By.CSS_SELECTOR, "#secondThreePrice").text
# 육계(1마리) 도매 전일 대비
ko_chicken_wholesale_price_diff = driver.find_element(By.CSS_SELECTOR, "#secondThreeTrate").text
# 계란(특란 30구) 도매 가격
ko_egg_wholesale_price = driver.find_element(By.CSS_SELECTOR, "#secondFourPrice").text
# 계란(특란 30구) 도매 전일 대비
ko_egg_wholesale_price_diff = driver.find_element(By.CSS_SELECTOR, "#secondFourTrate").text

# 한우(전국) 소매 가격
ko_cow_retail_price = driver.find_element(By.CSS_SELECTOR, "#thirdOnePrice").text
# 한우(전국) 소매 전일 대비
ko_cow_retail_price_diff = driver.find_element(By.CSS_SELECTOR, "#thirdOneTrate").text
# 돼지(전국) 소매 가격
ko_pig_retail_price = driver.find_element(By.CSS_SELECTOR, "#thirdTwoPrice").text
# 돼지(전국) 소매 전일 대비
ko_pig_retail_price_diff = driver.find_element(By.CSS_SELECTOR, "#thirdTwoTrate").text
# 육계(1마리) 소매 가격
ko_chicken_retail_price = driver.find_element(By.CSS_SELECTOR, "#thirdThreePrice").text
# 육계(1마리) 소매 전일 대비
ko_chicken_retail_price_diff = driver.find_element(By.CSS_SELECTOR, "#thirdThreeTrate").text
# 계란(특란 30구) 소매 가격
ko_egg_retail_price = driver.find_element(By.CSS_SELECTOR, "#thirdFourPrice").text
# 계란(특란 30구) 소매 전일 대비
ko_egg_retail_price_diff = driver.find_element(By.CSS_SELECTOR, "#thirdFourTrate").text

# print all
print("한우(전국) 도매 가격: ", ko_cow_wholesale_price)
print("한우(전국) 도매 전일 대비: ", ko_cow_wholesale_price_diff)
print("돼지(전국) 도매 가격: ", ko_pig_wholesale_price)
print("돼지(전국) 도매 전일 대비: ", ko_pig_wholesale_price_diff)
print("육계(1마리) 도매 가격: ", ko_chicken_wholesale_price)
print("육계(1마리) 도매 전일 대비: ", ko_chicken_wholesale_price_diff)
print("계란(특란 30구) 도매 가격: ", ko_egg_wholesale_price)
print("계란(특란 30구) 도매 전일 대비: ", ko_egg_wholesale_price_diff)
print("한우(전국) 소매 가격: ", ko_cow_retail_price)
print("한우(전국) 소매 전일 대비: ", ko_cow_retail_price_diff)
print("돼지(전국) 소매 가격: ", ko_pig_retail_price)
print("돼지(전국) 소매 전일 대비: ", ko_pig_retail_price_diff)
print("육계(1마리) 소매 가격: ", ko_chicken_retail_price)
print("육계(1마리) 소매 전일 대비: ", ko_chicken_retail_price_diff)
print("계란(특란 30구) 소매 가격: ", ko_egg_retail_price)
print("계란(특란 30구) 소매 전일 대비: ", ko_egg_retail_price_diff)

data = [
    ["가격" , "전일대비"],
    [ko_cow_wholesale_price, ko_cow_wholesale_price_diff],
    [ko_pig_wholesale_price, ko_pig_wholesale_price_diff],
    [ko_chicken_wholesale_price, ko_chicken_wholesale_price_diff],
    [ko_egg_wholesale_price, ko_egg_wholesale_price_diff],
    [ko_cow_retail_price, ko_cow_retail_price_diff],
    [ko_pig_retail_price, ko_pig_retail_price_diff],
    [ko_chicken_retail_price, ko_chicken_retail_price_diff],
    [ko_egg_retail_price, ko_egg_retail_price_diff]
]

with open("data.csv", "w",newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerows(data)

print("data.csv 파일이 생성되었습니다.")