from pathlib import Path

path = input('Enter the path to the folder with screenshots: ')

folder_path = Path(path)

file_count = len([f for f in folder_path.iterdir() if f.is_file()])

x = path.split('/')

f = open(f"{'/'.join(x)}/main.py", 'ч')

f.write('''
import pyautogui as pg
import time
import random
        ''')

for i in range(1, file_count + 1):
    f.write(f'''
s{i} = None
while not s{i}:
    try:
        s{i} = pg.locateCenterOnScreen('screens/{i}.png')
    except:
        continue
pg.click(s{i})
time.sleep(1)
            ''')
