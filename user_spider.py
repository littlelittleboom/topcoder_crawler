#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Utils import *
import json
import xlwt

begin = 30055549
end = 30095032
def getRegistrant():
    for challengeId in range(begin, end + 1, 1):
        chaReg = Challeng_Registrant(challengeId)  # list
        for i in range(0, len(chaReg)):
            if type(chaReg[i]) == dict and chaReg != None:
                with open('usernamme.txt', 'a') as f:
                    f.write(str(chaReg[i]['handle']))
                    f.write('\n')
def getUser():
    user_index = ['handle', 'country', 'memberSince']
    count = 0
    with open('user.json', 'w') as d:
        d.write('{' + '\n')
        d.write('  "RECORDS": [' + '\n')
    with open("usernamme.txt", "r") as f:
        for line in f.readlines():
            username = line.strip('\n')
            if count % 10 == 0:
                print('count:', count, 'handle:', username)
            count += 1
            # print(username)
            user_base = User(username)
            if user_base != None and type(user_base) == 'dict':
                # print(user_base)
                user = {}
                skill = getUserSkill(username)
                if type(skill['result']['content']) == 'dict':
                    skill_dict = skill['result']['content']['skills']
                    skills = []
                    for key in skill_dict:
                        user_skill = skill_dict[key]['tagName']
                        skills.append(user_skill)
                        # print(user_skill)
                    for i in user_index:
                        user[i] = user_base[i]
                    user['skills'] = skills
                    with open('user.json', 'a') as d:
                        json.dump(user, d, indent=4)
                        d.write(',')
                        d.write('\n')
    with open('user.json', 'a') as d:
        d.write(']' + '\n')
        d.write('}')


if __name__ == '__main__':
    getUser()
    # getRegistrant()