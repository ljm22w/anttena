# 프로그래밍 목표: 안테나의 철거 필요 유무를 알려주는 프로그램
# 라이브러리 불러오기

import requests
from bs4 import BeautifulSoup
import urllib.request as urlr
import clipboard


print('오늘의 안테나 철거 관련 정보를 요약해 드리겠습니다.')
#url 열기
open = urlr.urlopen('http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2717065000')
read1 = BeautifulSoup(open, "html.parser")
read2 = BeautifulSoup(open, "html.parser")

print(read1.find('r12').string)
print(read2.find('pop').string)