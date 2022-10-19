import sys
import os

COMMANDS = ("pwd", "cd", "touch", "cat", "ls", "rm")

def pwd(path: str):
    print(path)

def cd(path: str):
    try:
        os.chdir(path)
    except:
        print("can`t do it")

def touch(path: str):
    try:
        open(path, 'x')
    except:
        print("can`t do it")

def cat(path: str):
    try:
        file = open(path, 'r')
        print(*file)
    except:
        print("can`t do it")

def ls():
    for obj in os.listdir():
        print(obj)

def rm(path: str):
    try:
        os.remove(path)
    except:
        print("can`t do it")

while True:
    current_path = os.getcwd()
    print(current_path + '>', end='')
    try:
        querry = input().split(' ')
    except:
        print("incorrect usage")
        exit(1)
    if querry[0] not in COMMANDS:
        print("unknown command")
        continue

    if querry[0] == COMMANDS[0]:
        pwd(current_path)
    elif querry[0] == COMMANDS[1]:
        cd(querry[1])
    elif querry[0] == COMMANDS[2]:
        touch(querry[1])
    elif querry[0] == COMMANDS[3]:
        cat(querry[1])
    elif querry[0] == COMMANDS[4]:
        ls()
    elif querry[0] == COMMANDS[5]:
        rm(querry[1])


