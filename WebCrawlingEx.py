import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from itertools import count
import io

def rednooby_cralwler(input_search, filename):

    url = 'https://search.naver.com/search.naver'

    post_dict = OrderedDict() #OrderedDict를 사용하여, key에 url 입력

    text = io.open(filename, 'w', encoding="utf-8")

    for page in count(1): #1부터 무한대로 시작(break or return이 나올때까지)
        params = {
            'query' : input_search, #검색어를 사용자로부터 받아옴
            'sm'    : 'tab_jum',
            'where' : 'news',
            'start' : (page-1)*10+1,
        }
        print(page)
        response = requests.get(url, params =params)
        html = response.text

        #뷰티플소프의 인자값 지정
        soup = BeautifulSoup(html, 'html.parser')

        #쪼개기
        title_list = soup.select('._sp_each_url._sp_each_title')

        for tag in title_list:
            #if tag['href'] in post_dict: #현재 저장할 링크(key)가 이미 post_dict에 있으면
            #    return post_dict #작업종료
            print(tag.text)
            text.write(tag.text)
            post_dict[tag['href']] = tag.text
    text.close()
    return post_dict

def main() :
    rednooby_cralwler('바이오산업', 'd:\\aihhi.txt')

if __name__ == "__main__":
    main()
