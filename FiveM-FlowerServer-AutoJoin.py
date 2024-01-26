import requests, time, webbrowser

while True:
    response = requests.get("API_URL")
    print("서버가 온라인 인지 확인 중 . . .")
    if response.status_code == 200:
        print("서버에 접속을 시도 합니다.")
        webbrowser.open("SERVER_IP")
        break
    else:
        print("10초 뒤 접속을 재시도 합니다.")
        time.sleep(10)
