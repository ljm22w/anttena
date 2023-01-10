# 프로그래밍 목표: 안테나의 철거 필요 유무를 알려주는 프로그램
# 라이브러리 불러오기

import requests
import json

city = "Daegu" #도시
apiKey = "d4a7b6e3b0cfe65e5cb4bdc16dd3fee5"
lang = 'kr' #언어
units = 'imperial' #화씨 온도를 섭씨 온도로 변경
api = f"http://api.openweathermap.org/data/2.5/weather?q=Daegu&appid=secure&lang=en&units=metric"

result = requests.get(api)
data = json.loads(result.text)

wind = data["wind"]["speed"]
weather1 = data['weather'][0]['description']

print ("환영합니다. 대구광역시 안테나 철거 소식을 안내드립니다.")
if wind >= 14:
    print ('풍속: 강풍이 몰아치고 있습니다. 안테나 철거 권고')
else:
    print ('풍속: 정상적입니다.')

if weather1 == "Heavy rain":
    print('날씨: 강수량 시간당 7.6mm 이상. 안테나 철거 필요 없으나 주의 필요')
elif weather1 == "Violent rain":
    print("날씨: 비 매우 내림, 안테나 철거 바람")
else:
    print ('날씨: 정상적입니다.')
