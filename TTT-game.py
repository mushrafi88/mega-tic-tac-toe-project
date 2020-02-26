#!/usr/bin/env python
# coding: utf-8

import numpy as np
import sys
tic = [['---','---','---'], 
       ['---','---','---'],
       ['---','---','---']]
tac = [[0,0,0], 
       [0,0,0],
       [0,0,0]]

def primary_screen(tic):
    for row in tic:
        for elem in row:
            print(elem, end=" ")
        print()   

def instructions():
    print('hello')
    print('welcome')
    print('Here are the rules')
    print('1.   2 players can play at a time')
    print('2.   One player can input one value at a time')
    print('3.   The first digit of the input refers to the row in the 3*3 board and the second digit column')
    print('     for example if you type in 12 in the input box')
    print('     the program will place your designated x or o in the first row,second column element')
    print("4.   The one who gets the first diagonal,horizontal,vertical set of same 'x' or 'o' wins")

instructions()

print('hello players')
p1=input('Name of first player : ')
p1s=input('X or O ? ')
p2=input('Name of second player : ')
if p1s=='x' or p1s=='X':
    p1v=' X '
    p2v=' O '
if p1s=='o' or p1s=='O':
    p1v=' O '
    p2v=' X '
primary_screen(tic)    

from random import seed
from random import randint
value=randint(1,2)

def result(c,r,d,di):
    for i in range(0,3):
        if c[i]==30 or r[i]==30:
            if p1v==' X ':
                print(f'{p1} nigga you win')
                sys.exit()
            if p2v==' X ':
                print(f'{p2} you win')
                sys.exit()        
        if c[i]==300 or r[i]==300:
            if p1v==' O ':
                print(f'{p1} nigga you win')
                sys.exit()
            if p2v==' O ':
                print(f'{p2} you win')
                sys.exit()
        if d==300:
            if p1v==' O ':
                print(f'{p1} nigga you win')
                sys.exit()
            if p2v==' O ':
                print(f'{p2} you win')
                sys.exit()
        if d==30:
            if p1v==' X ':
                print(f'{p1} nigga you win')
                sys.exit()
            if p2v==' X ':
                print(f'{p2} you win')
                sys.exit()
        if di==30:
            if p1v==' X ':
                print(f'{p1} nigga you win')
                sys.exit()
            if p2v==' X ':
                print(f'{p2} you win')
                sys.exit()   
        if d==300:
            if p1v==' O ':
                print(f'{p1} nigga you win')
                sys.exit()
            if p2v==' O ':
                print(f'{p2} you win')
                sys.exit()   
        else :
            pass

def calc(tac):
    c=np.sum(a=tac,axis=0)
    r=np.sum(a=tac,axis=1)
    d=tac[0][0]+tac[1][1]+tac[2][2]
    di=tac[0][2]+tac[1][1]+tac[2][0]
    result(c,r,d,di)

if value==1:
    fp=p1
    fpv=p1v
    if fpv==' X ':
        fnpv=10
    else :
        fnpv=100
    sp=p2
    spv=p2v
    if spv==' X ':
        snpv=10
    else :
        snpv=100
else:
    fp=p2
    fpv=p2v
    if fpv==' X ':
        fnpv=10
    else :
        fnpv=100       
    sp=p1
    spv=p1v
    if spv==' X ':
        snpv=10
    else :
        snpv=100
count=0
while count <8:
    a=int(input(f'enter row and column {fp} :'))
    j=int((a%10))
    i=int((a-j)/10)
    k=i-1
    l=j-1
    tic[k][l]=fpv
    tac[k][l]=fnpv
    calc(tac)
    primary_screen(tic)
    count=count+1
    b=int(input(f'enter row and column {sp} :'))
    j=int((b%10))
    i=int((b-j)/10)
    k=i-1
    l=j-1
    count=count+1
    tic[k][l]=spv
    tac[k][l]=snpv
    calc(tac)
    primary_screen(tic) 

calc(tac)
for i in range(0,3):
    for j in range(0,3):
        if tac[i][j]==0:
            tic[i][j]=fpv
            tac[i][j]=fnpv
            calc(tac)
print(' ')
primary_screen(tic)
print('guess no one won')
