#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
import re
import json
import requests
from bs4 import BeautifulSoup
class getContent:
    def __init__(self, jsonName):
        with open(jsonName) as jsonFile:
            self.jsonData = json.load(jsonFile)
    
    def getContent(self, URL):
        contentList = []
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        result = soup.findAll("td", {"class":"replycontent"})
        author = soup.findAll("td", {"class":"replyinfo"})
        for i in range(len(result)):
            content = ""
            for topic in result[i].contents:
                content += re.sub(r'(\[.*\])','',str(topic))
            detial = author[i].contents
            contentList.append({
                "author":detial[1].string,
                "time":detial[3].split(":")[0].split("：")[1],
                "content":content
            })
        return contentList
    
    def getPostList(self, post):
        return self.getContent(post["url"])

    def getPost(self):
        for board in range(len(self.jsonData)):
            for post in range(len(self.jsonData[board]["topic"])):
                self.jsonData[board]["topic"][post]["content"] = self.getPostList(self.jsonData[board]["topic"][post])
        return self.jsonData
if __name__ == '__main__':
    a = getContent("next.json")
    #a.getPost()
    jsonD = a.getPost()
    with open('data.json', 'w' ) as outfile:
        json.dump(jsonD, outfile, ensure_ascii=False,indent=1)
