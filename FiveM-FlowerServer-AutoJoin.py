import configparser
import requests, time, webbrowser, psutil, os
from discord_webhook import DiscordWebhook


config = configparser.ConfigParser()


def checkFiveM():
    for proc in psutil.process_iter():
        ps_name = proc.name()
        if ps_name == 'FiveM.exe':
            return True
    return False


def logPrint(text):
    print(text)
    if config['USER_CONFIG']['WEBHOOK_URL'] != "NONE":
        print(config['USER_CONFIG']['WEBHOOK_URL'])
        webhook = DiscordWebhook(
            url=config['USER_CONFIG']['WEBHOOK_URL'], 
            content=f"{text}"
        )
        response = webhook.execute()
        print("전송 완료")


logPrint(f"{config.read('Config.ini')[0]}의 읽기가 완료 되었습니다.")
logPrint("FLOWER 접속기가 자동으로 접속 되었습니다.")


while True:
    response = requests.get(str(config['ADMIN_CONFIG']['API_IP']))
    if response.status_code == 200:
        resultCheckFiveM = checkFiveM()
        if resultCheckFiveM == False:
            logPrint("서버에 접속을 시도 합니다.")
            webbrowser.open(str(config['ADMIN_CONFIG']['SERVER_IP']))
            time.sleep(10)
            continue
        
        else:
            continue

    else:
        logPrint(f"{config['USER_CONFIG']['RECONNECT_TIME']}초 뒤 재접속을 시도 합니다.")
        time.sleep(float(config['USER_CONFIG']['RECONNECT_TIME']))