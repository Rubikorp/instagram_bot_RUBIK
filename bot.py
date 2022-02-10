from instamn import InstaLOGIN
from pathlib import Path
import time
import random

l = []
with open('users.txt') as f:
    l = f.read().splitlines()
print(l)

dat = []
with open('data.txt') as f:
    dat = f.read().splitlines()
print(dat)


if __name__ == '__main__':
    # Auto login
    insta = InstaLOGIN(username='login', password='pass', headless=False)
    # перебор по списку и отправка сообщения
    i = 0
    while i<len(l):
        insta.sendMessage(user=l[i], message=dat )
        i+=1
        if i == i % 20 == 0:
            time.sleep(1200)
            print('достигнут лимит в час, пауза 30 минут')

