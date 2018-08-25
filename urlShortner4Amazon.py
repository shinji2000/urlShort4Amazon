"""
amazonのURLから不要な部分を削除する
"""

import re

def urlShortner():
    text = "https://www.amazon.co.jp/Jupyter-Cookbook-Dan-Toomey/dp/1788839447/ref=sr_1_5?s=books&ie=UTF8&qid=1535164277&sr=1-5&keywords=Jupyter"
    newUrl = "https://www.amazon.co.jp"

    urlLen = len(text)
    #print(urlLen)

    matchObj = re.search(r'https://www.amazon.co.jp', text)
    matchObjDp = re.search(r'/dp/', text)
    matchObjRef = re.search(r'/ref', text)

    """"
    if matchObj:
        print (matchObj.group()) # マッチした文字列： abc
        print (matchObj.start()) # マッチした文字列の開始位置： 3
        print (matchObj.end())   # マッチした文字列の終了位置： 6
        print (matchObj.span())  # マッチした文字列の開始位置と終了位置： (3, 6)

    if matchObjDp:
        print (matchObjDp.group()) # マッチした文字列： abc
        print (matchObjDp.start()) # マッチした文字列の開始位置： 3
        print (matchObjDp.end())   # マッチした文字列の終了位置： 6
        print (matchObjDp.span())  # マッチした文字列の開始位置と終了位置： (3, 6)

    if matchObjRef:
        print (matchObjDp.start()) # マッチした文字列の開始位置： 3

    print(type(matchObj.start()))
    print(type(matchObj.end()))

    """

    """
    i:int = 1

    while i  < matchObj.end():
        newUrl = newUrl + text[i]
        print (newUrl)
        i= i+1
    """

    i:int = matchObjDp.start()
    #print("2ndStart:" + str(i) )
    while i <  matchObjRef.start():
        newUrl = newUrl + text[i]
    #    print (newUrl)
        i= i+1

    shortUrl = newUrl.replace("www","")
    print (shortUrl)

    return shortUrl

urlShortner()
