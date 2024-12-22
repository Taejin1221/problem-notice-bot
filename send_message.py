import json
import locale
import os
from datetime import datetime

import requests
from solved_ac_api import get_random_defence, get_problem_info

WEBHOOK_ID = os.environ.get("WEBHOOK_ID")
WEBHOOK_TOKEN = os.environ.get("WEBHOOK_TOKEN")

URL = f"https://discord.com/api/webhooks/{WEBHOOK_ID}/{WEBHOOK_TOKEN}"

locale.setlocale(locale.LC_TIME, 'ko_KR.UTF-8')
today = datetime.today()
weekday_name = today.strftime('%A')

content = f"# '{today.year % 100}. {today.month}. {today.day}.({weekday_name[:-2]}) 오늘의 문제\n"

with open("handle_list/gold_handle_list.json", "rt") as f:
    gold_handles = json.load(f)["handles"]

with open("handle_list/silver_handle_list.json", "rt") as f:
    silver_handles = json.load(f)["handles"]

problem = get_random_defence(gold_handles, "g")[0]
problem_info = get_problem_info(problem)
content += f"골드: [BOJ {problem}: {problem_info['titleKo']}](https://www.acmicpc.net/problem/{problem})\n"

problem = get_random_defence(silver_handles, "s")[0]
problem_info = get_problem_info(problem)
content += f"실버: [BOJ {problem}: {problem_info['titleKo']}](https://www.acmicpc.net/problem/{problem})\n"

response = requests.post(URL, {
    "content": content
})

print(response.status_code)
