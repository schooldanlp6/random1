#!/bin/python

#Copyright DanLP6@v1.0
#This tool is written and tested with python3 but can be used with any version
from time import sleep
import random
#import interface-needed-for-your-usecase

#set output to low if not already done
print("0")
n1=20
n2=random.randrange(1,40)
while (n2 != 20):
    n2=random.randrange(1,40)
    sleep(0.5)
    if (n1 == n2):
        print(1)
sleep(2)
print(0)
exit
