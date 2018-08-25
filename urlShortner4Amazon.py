
"""
クリップボードのamazonのURLから不要な部分を削除する
"""
# -*- coding: utf-8 -*-

import re
import pyperclip as clip
from urllib.parse import urlparse

#print(clip.paste())

def urlShortner():
#    text = "https://www.amazon.co.jp/Jupyter-Cookbook-Dan-Toomey/dp/1788839447/ref=sr_1_5?s=books&ie=UTF8&qid=1535164277&sr=1-5&keywords=Jupyter"

    if clip.paste():
        text = clip.paste()
        o = urlparse(text)
#        print(o.scheme)

        if not (o.scheme == 'http' or o.scheme == 'https') :
            print("This is not url.")
            return 1

    newUrl = "https://www.amazon.co.jp"

    urlLen = len(text)
    #print(urlLen)

    matchObj = re.search(r'https://www.amazon.co.jp', text)
    matchObjDp = re.search(r'/dp/', text)
    matchObjRef = re.search(r'/ref', text)

    """"
    if matchObjRef:
        print (matchObjDp.start()) # マッチした文字列の開始位置： 3

    print(type(matchObj.start()))
    print(type(matchObj.end()))

    """

    if matchObjDp and matchObjRef:
        i:int = matchObjDp.start()
        #print("2ndStart:" + str(i) )
        while i <  matchObjRef.start():
            newUrl = newUrl + text[i]
            i= i+1

        shortUrl = newUrl.replace("www","")

        print ("shortUrl:" + shortUrl)

        clip.copy(shortUrl)

    else:
        print ("This url is not an introduction page of books on the amazon website.")


urlShortner()
