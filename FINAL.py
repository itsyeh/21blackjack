#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import pandas as pd
import numpy as np


# In[2]:


hard_deck = np.array([[0,'A',2,3,4,5,6,7,8,9,10],
             [1,0,0,0,0,0,0,0,0,0,0],
             [2,0,0,0,0,0,0,0,0,0,0],
             [3,0,0,0,0,0,0,0,0,0,0],
             [4,'h','h','h','h','h','h','h','h','h','h'],
             [5,'h','h','h','h','h','h','h','h','h','h'],
             [6,'h','h','h','h','h','h','h','h','h','h'],
             [7,'h','h','h','h','h','h','h','h','h','h'],
             [8,'h','h','h','h','h','h','h','h','h','h'],
             [9,'h','h','dh','dh','dh','dh','h','h','h','h'],
             [10,'h','dh','dh','dh','dh','dh','dh','dh','dh','h'],
             [11,'dh','dh','dh','dh','dh','dh','dh','dh','dh','dh'],
             [12,'h','h','h','s','s','s','h','h','h','h'],
             [13,'h','s','s','s','s','s','h','h','h','h'],
             [14,'h','s','s','s','s','s','h','h','h','h'],
             [15,'rh','s','s','s','s','s','h','h','h','rh'],
             [16,'rh','s','s','s','s','s','h','h','rh','rh'],
             [17,'rs','s','s','s','s','s','s','s','s','s'],
             [18,'s','s','s','s','s','s','s','s','s','s'],
             [19,'s','s','s','s','s','s','s','s','s','s'],
             [20,'s','s','s','s','s','s','s','s','s','s'],
             [21,'s','s','s','s','s','s','s','s','s','s']])
soft_deck = np.array([[0,'A',2,3,4,5,6,7,8,9,10],
             [1,0,0,0,0,0,0,0,0,0,0],
             [2,0,0,0,0,0,0,0,0,0,0],
             [3,0,0,0,0,0,0,0,0,0,0],
             [4,0,0,0,0,0,0,0,0,0,0],
             [5,0,0,0,0,0,0,0,0,0,0],
             [6,0,0,0,0,0,0,0,0,0,0],
             [7,0,0,0,0,0,0,0,0,0,0],
             [8,0,0,0,0,0,0,0,0,0,0],
             [9,0,0,0,0,0,0,0,0,0,0],
             [10,0,0,0,0,0,0,0,0,0,0],
             [11,0,0,0,0,0,0,0,0,0,0],
             [12,0,0,0,0,0,0,0,0,0,0],
             [13,'h','h','h','h','dh','dh','h','h','h','h'],
             [14,'h','h','h','h','dh','dh','h','h','h','h'],
             [15,'h','h','h','dh','dh','dh','h','h','h','h'],
             [16,'h','h','h','dh','dh','dh','h','h','h','h'],
             [17,'h','h','dh','dh','dh','dh','s','s','h','h'],
             [18,'h','ds','ds','ds','ds','ds','s','s','h','h'],
             [19,'s','s','s','s','s','ds','s','s','s','s'],
             [20,'s','s','s','s','s','s','s','s','s','s'],
             [21,'s','s','s','s','s','s','s','s','s','s']])
split_deck = np.array([[0,'A',2,3,4,5,6,7,8,9,10],
              ['AA','p','p','p','p','p','p','p','p','p','p'],
              [22,'h','ph','ph','p','p','p','p','h','h','h'],
              [33,'h','ph','ph','p','p','p','p','h','h','h'],
              [44,'h','h','h','h','ph','ph','h','h','h','h'],
              [55,'h','dh','dh','dh','dh','dh','dh','dh','dh','h'],
              [66,'h','ph','p','p','p','p','h','h','h','h'],
              [77,'h','p','p','p','p','p','p','h','h','h'],
              [88,'rp','p','p','p','p','p','p','p','p','p'],
              [99,'s','p','p','p','p','p','s','p','p','s'],
              [1010,'s','s','s','s','s','s','s','s','s','s']])


# In[3]:


def calculate(x, y ,z):
    total = 0
    x = int(x)
    y = int(y)
    z = int(z)
    if x == 1:
        total = total - 1
    elif 1 < x < 7:
        total = total + 1
    elif 6 < x < 10:
        total = total
    elif x == 10:
        total = total - 1
    if y == 1:
        total = total - 1
    elif 1 < y < 7:
        total = total + 1
    elif 6 < y < 10:
        total = total
    elif y == 10:
        total = total - 1
    if z == 1:
        total = total - 1
    elif 1 < z < 7:
        total = total + 1
    elif 6 < z < 10:
        total = total
    elif z == 10:
        total = total - 1
    result = '此輪算牌的結果為:', total
    label_result = tk.Label(win, text = result, font=("Courier", 12, "italic"))
    label_result.place(x = 65, y = 300)
    label_rules = tk.Label(win, text = '(算牌結果越大則下輪玩家越有利，反之則表示莊家有利)', font=('Arial', 10))
    label_rules.place(x = 65, y = 325)


# In[4]:


def response():
    x = first_card.get().strip()
    y = second_card.get().strip()
    z = banker_card.get().strip()
    if x == y:
        position_y = x
        position_x = z
        position_x = int(position_x)
        position_y = int(position_y)
        out = split_deck[position_y, position_x]
        advice_1 = '---->建議的策略為', out
        label_split = tk.Label(win, text = advice_1, font=("Courier", 12, "italic"))
        label_split.place(x = 65, y = 250)
        if out == 'h':
            out_2 = '請拿牌                        '
        elif out == 's':
            out_2 = '請停牌                        '
        elif out == 'dh':
            out_2 = '若可以雙倍加注則加注，否則拿牌   '
        elif out == 'ds':
            out_2 = '若可以雙倍加注則加注，否則停牌   '
        elif out == 'p':
            out_2 = '請分牌                         '
        elif out == 'ph':
            out_2 = '若分牌後可以加注則分牌，否則拿牌'
        elif out == 'rh':
            out_2 = '若可以投降則投降，否則拿牌       '
        elif out == 'rs':
            out_2 = '若可以投降則投降，否則停牌      '
        elif out == 'rp':
            out_2 = '若可以投降則投降，否則分牌      '
        else:
            out_2 = '輸入有誤'
        label_decision = tk.Label(win, text = out_2, font=("Courier", 12, "italic"))
        label_decision.place(x = 60, y = 275)
    elif x == '1' :
        x = 1 + 10
        a = np.array([x, y, z])
        a_int = a.astype(int)
        b = np.array([[1, 0], [1, 0], [0, 1]])
        position_y, position_x = np.dot(a_int,b)
        position_x = int(position_x)
        position_y = int(position_y)
        out = soft_deck[position_y, position_x]
        advice_2 = '---->建議的策略為', out
        label_soft = tk.Label(win, text = advice_2, font=("Courier", 12, "italic"))
        label_soft.place(x = 65, y = 250)
        if out == 'h':
            out_2 = '請拿牌                        '
        elif out == 's':
            out_2 = '請停牌                        '
        elif out == 'dh':
            out_2 = '若可以雙倍加注則加注，否則拿牌  '
        elif out == 'ds':
            out_2 = '若可以雙倍加注則加注，否則停牌  '
        elif out == 'p':
            out_2 = '請分牌                        '
        elif out == 'ph':
            out_2 = '若分牌後可以加注則分牌，否則拿牌'
        elif out == 'rh':
            out_2 = '若可以投降則投降，否則拿牌      '
        elif out == 'rs':
            out_2 = '若可以投降則投降，否則停牌      '
        elif out == 'rp':
            out_2 = '若可以投降則投降，否則分牌      '
        else:
            out_2 = '輸入有誤'
        label_decision = tk.Label(win, text = out_2, font=("Courier", 12, "italic"))
        label_decision.place(x = 60, y = 275)
    elif y == '1':
        y = 1 + 10
        a = np.array([x, y, z])
        a_int = a.astype(int)
        b = np.array([[1, 0], [1, 0], [0, 1]])
        position_y, position_x = np.dot(a_int,b)
        position_x = int(position_x)
        position_y = int(position_y)
        out = soft_deck[position_y, position_x]
        advice_4 = '---->建議的策略為', out
        label_soft_2 = tk.Label(win, text = advice_4, font=("Courier", 12, "italic"))
        label_soft_2.place(x = 65, y = 250)
        if out == 'h':
            out_2 = '請拿牌                        '
        elif out == 's':
            out_2 = '請停牌                        '
        elif out == 'dh':
            out_2 = '若可以雙倍加注則加注，否則拿牌  '
        elif out == 'ds':
            out_2 = '若可以雙倍加注則加注，否則停牌  '
        elif out == 'p':
            out_2 = '請分牌                        '
        elif out == 'ph':
            out_2 = '若分牌後可以加注則分牌，否則拿牌'
        elif out == 'rh':
            out_2 = '若可以投降則投降，否則拿牌      '
        elif out == 'rs':
            out_2 = '若可以投降則投降，否則停牌     '
        elif out == 'rp':
            out_2 = '若可以投降則投降，否則分牌      '
        else:
            out_2 = '輸入有誤'
        label_decision = tk.Label(win, text = out_2, font=("Courier", 12, "italic"))
        label_decision.place(x = 60, y = 275)
    elif x != y:
        a = np.array([x, y, z])
        a_int = a.astype(int)
        b = np.array([[1, 0], [1, 0], [0, 1]])
        position_y, position_x = np.dot(a_int,b)
        position_x = int(position_x)
        position_y = int(position_y)
        out = hard_deck[position_y, position_x]
        advice_3 = '---->建議的策略為', out
        label_hard = tk.Label(win, text = advice_3, font=("Courier", 12, "italic"))
        label_hard.place(x = 65, y = 250)
        if out == 'h':
            out_2 = '請拿牌                        '
        elif out == 's':
            out_2 = '請停牌                        '
        elif out == 'dh':
            out_2 = '若可以雙倍加注則加注，否則拿牌  '
        elif out == 'ds':
            out_2 = '若可以雙倍加注則加注，否則停牌  '
        elif out == 'p':
            out_2 = '請分牌                        '
        elif out == 'ph':
            out_2 = '若分牌後可以加注則分牌，否則拿牌'
        elif out == 'rh':
            out_2 = '若可以投降則投降，否則拿牌      '
        elif out == 'rs':
            out_2 = '若可以投降則投降，否則停牌      '
        elif out == 'rp':
            out_2 = '若可以投降則投降，否則分牌       '
        else:
            out_2 = '輸入有誤'
        label_decision = tk.Label(win, text = out_2, font=("Courier", 12, "italic"))
        label_decision.place(x = 60, y = 275)
    calculate(x, y ,z)
    return 0


# In[5]:


win = tk.Tk()
win.title('BLACK JACK策略建議')
win.geometry('450x450')

label_1 = tk.Label(win, text='你的第一張手牌是:', font=('Arial', 12))
label_2 = tk.Label(win, text='你的第二張手牌是:', font=('Arial', 12))
label_3 = tk.Label(win, text='莊家的明牌是:', font=('Arial', 12))
label_4 = tk.Label(win, text='請依敘輸入您的手牌，若為A請輸入1', font=('Arial', 14))
label_5 = tk.Label(win, text='若為J，Q，K則輸入10', font=('Arial', 14))


label_1.place(x = 85, y = 85)
label_2.place(x = 85, y = 115)
label_3.place(x = 85, y = 145)
label_4.place(x = 60, y = 10)
label_5.place(x = 110, y = 45)

first_card = tk.StringVar()
entry_1 = tk.Entry(win, textvariable=first_card, width = 20)
entry_1.place(x = 225, y = 85)

second_card = tk.StringVar()
entry_2 = tk.Entry(win, textvariable=second_card, width = 20)
entry_2.place(x = 225, y = 115)

banker_card = tk.StringVar()
entry_2 = tk.Entry(win, textvariable=banker_card, width = 20)
entry_2.place(x = 225, y = 145)

button = tk.Button(win, text = '查詢建議策略', font = ('Arial', 12), command = response)
button.place(x = 60, y = 180, width = 330, height = 50)


# In[6]:


win.mainloop()


# In[ ]:




