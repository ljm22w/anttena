# 프로그래밍 목표: swr에 따라 변화하는 이론적인 출력 수를 보여주는 프로그램
import os #clear를 위한 모듈

print ('출력 와트 수를 입력하세요.')
print ('본 값들은 모두 이론적인 값으로 실제 출력과는 어느정도 차이가 있을 수 있습니다.')
print ('-본 프로그램은 맥, 리눅스, 파워셸에 최적화 되어있습니다.-')

#전압 변수 저장
volts = float(input ('출력 전압: '))

print ('VSWR (전압 정재파비)를 입력하세요.')

#swr 변수 저장
vswr = float(input ('vswr 수: '))

#모든 출력값 삭제
os.system ('clear')

#반사 계수
bunsu = (vswr-1) / (vswr+1)
#돌아오는 전압
turnvolts = volts * bunsu
#출력 전압
govolts = volts - turnvolts

#결과 값 출력
print ("돌아오는 전압: (v)")
print (round(turnvolts,3))
print ('출력 전압: (v)')
print (round(govolts, 3))
print ('반사 계수: ')
print (round(bunsu,3))





