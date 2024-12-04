import requests

def get_weather(city, api_key):
    # OpenWeatherMap API의 기본 URL
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # 요청 URL 생성 (city, api_key, 단위 설정)
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"  # 섭씨 온도로 받기 위해 units=metric 추가
    
    # API에 요청을 보내고 응답을 받음
    response = requests.get(complete_url)
    
    # 응답 데이터 JSON으로 파싱
    data = response.json()
    
    # 응답 코드가 404인 경우(도시를 찾을 수 없음)
    if data["cod"] == "404":
        return f"도시 {city}를 찾을 수 없습니다."
    else:
        # 날씨 정보 파싱
        main = data["main"]  # 온도 및 습도 정보
        weather = data["weather"][0]  # 날씨 상태 정보 (예: 맑음, 흐림 등)
        
        # 온도, 습도, 날씨 상태를 변수에 저장
        temperature = main["temp"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        
        # 날씨 정보를 사용자에게 보기 좋게 출력
        return f"{city}의 날씨:\n" \
               f"온도: {temperature}°C\n" \
               f"습도: {humidity}%\n" \
               f"날씨: {weather_description.capitalize()}"
