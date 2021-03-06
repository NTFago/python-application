from bs4 import BeautifulSoup
import requests
import re

URL = "https://v.youku.com/v_show/id_XMzY4Mzg3Mjc1Mg==.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
# 获取网页内容
def download_page(url):
    global headers
    data = requests.get(url, headers=headers).content
    print("download finshed")
    return data

# 获取需要的信息
## 获取视频链接
def get_link(doc):
    soup = BeautifulSoup(doc, "html.parser")
    ac = soup.find("div", class_="anthology-content")
    context = []
    links = []
    link = ""
    for i in ac.find_all("a"):
        href = re.findall(r"(?<=href=\").+(?= title)", str(i))
        context.append(href[0])
    for j in context:
        for k in j:
            if k == "?":
                break
            else:
                link += k
        links.append(link)
        link = ""
    links = list(set(links))
    print("get link finshed", links)
    return links

## 获取标题
def get_title(doc):
    soup = BeautifulSoup(doc, "html.parser")
    ac = soup.find("div", class_="anthology-content")
    names = []
    titles = []
    name = ""
    for i in ac.find_all("a"):
        title = re.findall(r"(?<=title=\").+(?=\"\>)", str(i))
        names.append(title[0])
    for j in names:
        for k in j:
            if k == "\"":
                break
            else:
                name += k
        name = "".join(re.findall(r"\d", name))
        titles.append(name)
        name = ""
    print("get title finshed")
    return titles

# 下载
## api接口下载链接
def get_api_1(urls):
    download_links = []
    for i in urls:
        id_ = re.findall(r"(?<=id_).+(?=.html)", i)
        new_link = "https://vvv.yaohuaxuan.com/data/ykm3u8/{}.m3u8".format(id_[0])
        download_links.append(new_link)
    print("get download links finshed", download_links)
    return download_links

def get_api_2(urls):
    download_links = []
    for i in urls:
        new_link = "http://jx.mw0.cc/?url={}".format(i)
        download_links.append(new_link)
        with open("SCI.txt", "a+", encoding="utf-8") as f:
            f.writelines(new_link+"\n")
    print("get download links finshed", download_links)
    return download_links

## 调用 IDM 进行下载
def call_idm(down_urls, titles):
    global headers
    for url in down_urls:
        docs = requests.get(url, headers=headers).content
        html = BeautifulSoup(docs, "html.parser")
        print(html)

if __name__ == "__main__":
    data = download_page(URL)       # 获取页面树状图
    links = get_link(data)          # 获取视频链接 list
    titles = get_title(data)        # 获取标题    list
    download_links = get_api_2(links) # 获取下载链接 list
    # call_idm(download_links, titles)
