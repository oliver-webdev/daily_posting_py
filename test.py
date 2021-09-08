import os
from datetime import datetime
import pytz


print(os.environ['MARKETSTACK_ACCESS_KEY'])
print(os.environ['TISTORY_ACCESS_TOKEN'])

now = datetime.utcnow()
print(now)

KST = pytz.timezone('Asia/Seoul')
now_kst = now.astimezone(KST)
print(now_kst.strftime("%Y-%m-%d %H:%M:%S %Z%z"))


print(now_kst.strftime("%Y"))
print(now_kst.strftime("%m"))
print(now_kst.strftime("%d"))

