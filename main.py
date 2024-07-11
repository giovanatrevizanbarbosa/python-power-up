import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

def open_google_keep():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")

    pyautogui.write('https://keep.google.com/u/0/')
    pyautogui.press("enter")
    time.sleep(3)

def add_task(title, description):
    pyautogui.click(x=667, y=203)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.write(title)
    pyautogui.press('tab')
    pyautogui.write(description)
    pyautogui.click(x=1058, y=299)

def delete_tasks(quantity):
    for _ in range(quantity):
        pyautogui.click(x=538, y=344)
        pyautogui.click(x=571, y=382)

def empty_trash():
    pyautogui.click(x=99, y=375)
    pyautogui.click(x=1003, y=194)
    pyautogui.click(x=800, y=439)

tasks = pandas.read_csv('tasks.csv')

open_google_keep()

for row in tasks.index:
    title = str(tasks.loc[row, "title"])
    description = str(tasks.loc[row, "description"])
    add_task(title, description)