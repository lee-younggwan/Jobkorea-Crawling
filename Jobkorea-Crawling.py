import requests
from bs4 import BeautifulSoup

#저장하고 싶은 경로, 파일명 입력
f = open("질문.txt", "w")

#크롤링하고자 하는 회사의 url과 마지막 html 페이지 번호
for page in range(13):
    req = requests.get('http://www.jobkorea.co.kr/starter/review/view?FavorCo_Stat=0&OrderBy=0&Page=1&C_Idx=1&Half_Year_Type_Code=0&Ctgr_Code=5&VPage=' + str(page + 1))
    raw = req.text
    html = BeautifulSoup(raw, 'html.parser')
    infos = html.select('div.items')
    print(page)
    for info in infos:
        txt = info.select_one('span.tx').text
        txt = txt.lstrip().rstrip()
        f.write(txt+'\n')

f.close()
