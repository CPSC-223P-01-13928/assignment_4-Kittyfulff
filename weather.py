from dataclasses import dataclass
import json
from re import X

def read_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
            return{}

def write_data(data,filename):
    with open(filename, 'w') as f:
        json.dump(data,f)

def max_temperature(data,date):
    x=0
    for key in data:
        if date == key[0:8]:
            if date[key]['t']>x:
                x=data[key]['t']
    return X

def min_temperature(data,date):
    x=9999
    for key in data:
        if date == key[0:8]:
            if date[key]['t']<x:
                x=data[key]['t']
    return X

def max_humidity(data,date):
    x=0
    for key in data:
        if date == key[0:8]:
            if date[key]['h']>x:
                x=data[key]['h']
    return X
def min_humidity(data,date):
    x=9999
    for key in data:
        if date == key[0:8]:
            if date[key]['h']<x:
                x=data[key]['h']
    return X
def tot_rain(data,date):
    sum=0
    for key in data:
        if date ==key[0:8]:
            sum=+ date['r']
    return sum
display = "========================= DAILY REPORT ========================"
display =+ "Date                      Time  Temperature  Humidity  Rainfall"
display =+ "====================  ========  ===========  ========  ========"
def report_daily(data,date):
    display = "========================= DAILY REPORT ========================\n"
    display2 = "Date                      Time  Temperature  Humidity  Rainfall\n"
    display3 = "====================  ========  ===========  ========  ========\n"
    print(display)
    print(display2)
    print(display3)
    for key in data:
        if date == key[0:8]:
            m = calender.month_name[int(date[4:6])] + str(int(data[6:8])),"," + str(int(date[0:4]))
            tm = key[8:10] + ":" + key[10:12] + ":" + key [12:14]
            t=data[key][t]
            h=data[key][h]
            r=data[key][r]

            display += f'{m:22}{tm:8}{t:13}{h:10}{r:10.2f}'+"\n"
            print(m)
def report_historical(data)

