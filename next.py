#! /usr/bin/env python3 
#! -*- coding : utf8 -*-
import requests
from bs4 import BeautifulSoup
import json

class next:
    def __init__(self):
        self.URL = "http://next.fishome.tw/bbs/"
    def add(self, result):
        theList = []
        for i in range(len(result)): 
            theList.append(
                {
                    "title":result[i].find("a").string,
                    "url":self.URL+result[i].find("a").get("href")
                }      
            )
        return theList
    def postAdd(self, post, auth):
        theList = []
        for i in range(len(post)): 
            detail = str(auth[i].renderContents(),encoding = "utf-8")
            detail = detail.split("<br/>")

            author = detail[0].split("：")
            author = author[1]

            time = detail[1].split("：")
            time = time[1]

            theList.append(
                {
                    "title":post[i].find("a").string,
                    "url":self.URL+post[i].find("a").get("href"),
                    "author":author,
                    "time":time
                }      
            )
        return theList

    def getBoard(self):
        r = requests.get(self.URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        result = soup.findAll("span", {"class":"name"})
        
        board = self.add(result)
        return board

    def getPost(self, key):
        board = self.getBoard()
        
        r = requests.get(board[key]["url"])
        soup = BeautifulSoup(r.text, 'html.parser')
        postResult = soup.findAll("td",{"class","topiclist"})
        authResult = soup.findAll("td",{"class","topicdetail"}) 

        post = self.postAdd(postResult, authResult)
        return post
    def dumpJson(self):
        board = self.getBoard()
        for i in range(len(board)):
            board[i]["topic"] = a.getPost(i)
        print(json.dumps(board,ensure_ascii=False))


if __name__ == '__main__':
    a = next();
    #board = a.getBoard()
    #for i in range(len(board)):
    #    board[i]["topicList"] = a.getPost(i)
    #print(json.dumps(board,ensure_ascii=False))
    #print(a.getPost(0))
    
    a.dumpJson()
