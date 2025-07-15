import requests #url get 요청
import csv # csv로 저장
import os # 폴더 생성
from datetime import datetime # 시간변환

API_KEY = os.getenv("API_KEY_W")
if not API_KEY:
    raise ValueError("API_KEY_W 환경 변수가 설정되지 않았습니다.")

city = "seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
result = response.json()

temp = result["main"]["temp"]
humidity = result["main"]["humidity"]
weather = result["weather"][0]["main"]
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

# csv
header = ["curren_time", "weather", "temp", "humidity"]

# 만약 seoul_weather.csv 없으면 만들고 있으면 덮어쓰기
csv_exist = os.path.exists("seoul_weather.csv")
with open("seoul_weather.csv","a") as file:
    writer = csv.writer(file)

    if not csv_exist: # csv가 한번도 안 만들어 졌다면, 헤어 추가
        writer.writerow(header)

    writer.writerow([current_time, weather, temp, humidity])
    print("서울 기온 저장완료")
