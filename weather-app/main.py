import os
from weather import get_weather

def main():
    api_key = "5f71899dc25c26a4e075c9fdd21aa034"  # OpenWeatherMap API 키 입력
    city = os.getenv('CITY_NAME', 'Seoul')  # 환경 변수 CITY_NAME에서 도시 이름을 읽고, 없으면 'Seoul'을 기본값으로 사용
    
    print(f"날씨를 확인할 도시: {city}")

    weather_info = get_weather(city, api_key)
    print(weather_info)

if __name__ == "__main__":
    main()

    
def main():
    api_key = "5f71899dc25c26a4e075c9fdd21aa034"
    city = input("Enter the city name: ")

    if not city.strip():  # 입력값이 비었는지 확인
        print("Error: City name cannot be empty. Please enter a valid city name.")
        return

    weather_info = get_weather(city, api_key)
    print(weather_info)

def main():
    api_key = "5f71899dc25c26a4e075c9fdd21aa034"
    while True:
        city = input("Enter the city name (type 'exit' to quit): ")

        if city.lower() == "exit":  # 사용자가 'exit' 입력 시 프로그램 종료
            print("Exiting the program. Goodbye!")
            break

        weather_info = get_weather(city, api_key)
        print(weather_info)
