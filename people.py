from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import pandas as pd

def first():
    url = 'https://movie.douban.com/top250'
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    req = urllib.request.Request(url=url,headers=header)
    s = ask_url(req)
    # print(s)
    a = get_data(s)
    # print(a)
    for i in a:
        print(i)
    save_path = '.\\people.xls'
    # save_data(save_path)
def ask_url(req):
    try:
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        # print(res.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print('time out!')
        print(e)
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html
#1.爬取页面
findTittle = re.compile(r'<span class="title">(.*)</span>')
findUrl = re.compile(r'<a.*href="(.*?)">')
findImg = re.compile(r'<img.*src="(.*?)"',re.S)
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findPeople = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
def get_data(url):
    data = []

    #2、逐一解析数据U
    soup = BeautifulSoup(url,'html.parser')
    for item in soup.find_all('div',class_='item'):
        # print(item)
        datalist = []
        item = str(item)
        tittle = re.findall(findTittle,item)

        if len(tittle) > 1:
            datalist.append(tittle[0])
            en = tittle[1].replace('/','')
            en = en.replace('\xa0', '')
            datalist.append(en)
        else:
            datalist.append(tittle[0])
            datalist.append('无外文名')

        url = re.findall(findUrl,item)[0]
        datalist.append(url)
        img = re.findall(findImg, item)[0]
        datalist.append(img)
        rating = re.findall(findRating, item)[0]
        datalist.append(rating)
        people = re.findall(findPeople, item)[0]
        datalist.append(people)
        inq = re.findall(findInq, item)[0]
        datalist.append(inq)
        bd = re.findall(findBd, item)[0]
        bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)
        bd = re.sub('/', " ", bd)
        bd = re.sub('\xa0', " ", bd)
        datalist.append(bd.strip())
        # break
        data.append(datalist)

    return data

#3、保存数据
def save_data(path):
    pass


if __name__ == '__main__':
    first()
