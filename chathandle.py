import requests
import multiprocessing
import time
from threading import Thread

# Headers for faking Edge
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__test=4faa7f989f0c6ceed9d03e6a3a53ef64',
    'Host': 'relayjuicebox.rf.gd',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

# Long polling endpoint URL
long_polling_url = 'http://relayjuicebox.rf.gd/long_polling.php'

# Data handling endpoint URL
data_url = 'http://relayjuicebox.rf.gd/data_handler.php'

# Function to listen for long polling updates
def listen_for_long_polling():
    while True:
        response = requests.get(long_polling_url, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            print("Received:", response_json)
        else:
            print("Request failed with status code:", response.status_code)

# Function to send data to the server
def send_data(param1, param2):
    data = {
        'param1': param1,
        'param2': param2
    }
    response = requests.post(data_url, data=data, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        print("Response JSON:", response_json)
    else:
        print("Request failed with status code:", response.status_code)

# Main loop to handle user input
def main():
    user = input("Enter target username: ")
    while True:
        param1 = sendto
        param2 = input("Send: ")
        send_data(param1, param2)

t1 = Thread(target = listen_for_long_polling)
t2 = Thread(target = main)

t1.start()
t2.start()

#listen_for_long_polling()
#main()
