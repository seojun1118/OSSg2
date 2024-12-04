from weather import get_weather

def main():
    api_key = "5f71899dc25c26a4e075c9fdd21aa034"  # OpenWeatherMap에서 받은 API 키 입력
    city = input("날씨를 확인할 도시를 입력하세요: ")  # 사용자 입력 받기
    
    weather_info = get_weather(city, api_key)  # 날씨 정보 가져오기
    print(weather_info)  # 날씨 정보 출력

if __name__ == "__main__":
    main()
    
def main():
    api_key = "YOUR_API_KEY"
    city = input("Enter the city name: ")

    if not city.strip():  # 입력값이 비었는지 확인
        print("Error: City name cannot be empty. Please enter a valid city name.")
        return

    weather_info = get_weather(city, api_key)
    print(weather_info)
