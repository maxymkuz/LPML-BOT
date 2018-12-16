import json
import requests
import time
import urllib
import datetime


TOKEN = "744130670:AAGOOI_656XxcK46n7IHNpZTXvWW2OjSmfY"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def minus(a, b):
    result = a - b
    return result

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    #text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def echo_all(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        now = datetime.datetime.now()
        day_of_week = now.isoweekday()
        time = now.time
        hour = now.hour
        minute = now.minute
        second = now.second

        def write_msg(x, y, z):
            format_list = [x, y, z]
            msg_txt = "time to next lesson:{} H and {} M and {} S".format(*format_list)
            chat_id = chat
            send_message(msg_txt, chat_id)
            print(x, y, z)
            print("works")

        if True:
            if True:
                if hour*100 + minute < 845 or hour*100 + minute >= 1540:
                        h = minus(8, hour)
                        m = minus(44, minute)
                        s = minus(60, second)
                        if h < 0:
                            h = 24 + h
                        if m < 0:
                            m = m + 60
                            h = h - 1
                        write_msg(h, m, s)
                elif hour * 100 + minute < 930:
                    h = minus(9, hour)
                    m = minus(30, minute)
                    s = minus(60, second)
                    if m < 0:
                        m = m + 60
                        h = h - 1
                        write_msg(h, m, s)
                elif hour * 100 + minute < 1025:
                    h = minus(10, hour)
                    m = minus(25, minute)
                    s = minus(60, second)
                    if m < 0:
                        m = m + 60
                        h = h - 1
                        write_msg(h, m, s)
                elif hour * 100 + minute < 1120:
                    h = minus(11, hour)
                    m = minus(20, minute)
                    s = minus(60, second)
                    if m < 0:
                        m = m + 60
                        h = h - 1
                    write_msg(h, m, s)
                elif hour * 100 + minute < 1225:
                    h = minus(9, hour)
                    m = minus(12, minute)
                    s = minus(25, second)
                    if m < 0:
                        m = m + 60
                        h = h - 1
                    write_msg(h, m, s)
                elif hour * 100 + minute < 1335:
                    h = minus(13, hour)
                    m = minus(35, minute)
                    s = minus(60, second)
                    if m < 0:
                        m = m + 60
                        h = h - 1
                    write_msg(h, m, s)
                elif hour * 100 + minute < 1445:
                    h = minus(14, hour)
                    m = minus(45, minute)
                    s = minus(60, second)
                    if m < 0:
                        m = m + 60
                        h = h - 1
                    write_msg(h, m, s)
        #send_message(text, chat)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()