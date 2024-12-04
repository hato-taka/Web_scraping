# ① HTMLデータの取得
import requests

url = "https://example.com"
response = requests.get(url)
html_content = response.text

# HTMLの解析
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content, 'html.parser')
title = soup.title.string
paragraphs = soup.find_all('p')

#  動的コンテンツの処理
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.yahoo.co.jp/")
dynamic_content = driver.find_element(By.ID, "tabTopics").text
print(dynamic_content)
driver.quit()