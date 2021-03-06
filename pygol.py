from github import Github
import os
import time
from time import sleep
from blessings import Terminal
from datetime import datetime
import sys
f = open('key.key','r')
key = f.read()
f.close()

key = key.replace("\n","")
print("key" +key)

input = sys.argv
f = open(str(input[1]) +'.txt','r')
std_data = f.read()
f.close()

std_data = std_data.splitlines()
stdlist =[]

g = Github(key)

for std in std_data:
    std = std.split()
    stdlist.append(std)
 
term = Terminal()
#print(term.home + term.clear)
for std in stdlist:
        try:
            repo = g.get_repo(std[3])
            commit = repo.get_commit(repo.get_commits()[0].sha).raw_data['commit']['message']
            std.append(repo)
            std.append(commit)
        except Exception as e:
            print(std[3])
            print(e)
            exit()

for i in range(len(stdlist)):
            with term.location(0, i+2):          
                print(stdlist[i][1] + "     ")

while True:
    sleep(30)
    try:
        for i in range(len(stdlist)):
            with term.location(20, i+2):
                if(stdlist[i][5] == stdlist[0][5]):
                    print(term.green + stdlist[i][5][0:31] + "     " + term.normal)
                else:
                    print(term.red + stdlist[i][5][0:31]  + "     "+ term.normal)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with term.location(0,len(stdlist)+3):
            print("last update : " , dt_string)

        for std in stdlist:
            
            commit = std[4].get_commit(std[4].get_commits()[0].sha).raw_data['commit']['message']
            std[5] = commit
    except KeyboardInterrupt :
        exit()
    except Exception as e:
        print(e)
        exit()