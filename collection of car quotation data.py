import requests
from bs4 import BeautifulSoup
import pandas as pd

# 请求URL
def get_page_content(request_url):
    # 得到页面的内容
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(request_url,headers=headers,timeout=10)
    content = html.text
    soup = BeautifulSoup(content, 'html.parser')
    return soup

#分析当前页面的投诉
def analysis(soup):
    temp = soup.find("div",class_="search-result-list")
    #创建Dataframe
    df =pd.DataFrame(columns = ['car_model', 'lowest_price', 'highest_price', 'img_address'])
    #返回一个a的列表
    a_list = temp.find_all('a')
    #a代表车型，p代表车型下面的名称、价格信息
    for a in a_list:
        #提取汽车报价信息
        temp = {}
        p_liste = a.find_all('p')
        if len(p_liste)>0:
            #获取车型名称和价格区间
            car_model,price_range = p_liste[0].text,p_liste[1].text
            lowest_price = price_range.split('-')[0]+"万"
            highest_price = price_range.split('-')[-1]
            #放到Dateframe中
            temp['car_model'], temp['lowest_price'], temp['highest_price'] = car_model, lowest_price, highest_price
        imgs = a.find_all('img')
        for img in imgs:
            url = img['src']
            temp['img_address'] = url
        df = df.append(temp, ignore_index=True)
    return df

page_num = 3
base_url = 'http://car.bitauto.com/xuanchegongju/?mid=8&page='
#创建Dataframe
result = pd.DataFrame(columns = ['car_model', 'lowest_price', 'highest_price', 'img_address'])
for i in range(page_num):
    request_url = base_url+str(i+1)
    print(request_url)
    soup = get_page_content(request_url)
    df = analysis(soup)
    print(df)
    result = result.append(df)
result.to_csv("car quotation data.csv",index=False)