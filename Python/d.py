import time
import pyautogui

my_file = open("dd.txt", "r")

content = my_file.read()
content.replace('\n',',')

content_list = content.split("\n")
print(content_list)
my_file.close()
time.sleep(2)

for palavra in content_list:
    pyautogui.write(palavra)
    pyautogui.press('enter')

