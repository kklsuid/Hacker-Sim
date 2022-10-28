import curses
from time import sleep

def str_onebyone(y=0, x=0, string="Hello, World!", wait=0.35):
    if type(string) != str:
        string = str(string)
    for ch in string:
        curses.addstr(y,x,ch)
        x += 1
        sleep(wait)