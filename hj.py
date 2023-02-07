#小沐同学 除yaohuo外 禁止分享 一切后果与本人无关

#小沐同学 除yaohuo外 禁止分享 一切后果与本人无关

import random
import json
import hashlib
import requests
import base64,re
from flask import Flask
from flask import render_template
app = Flask(__name__)
#


@app.route("/%7Burl%7D", methods=["GET"])
@app.route("//favicon.ico", methods=["GET"])
def main3():
    print("0")
    return "/aa"

@app.route("/<url>", methods=["GET"])

def main(url):

    #url = 'http://hjfdf.com/post/details?pid=446352'
    #pid = url.split("=")[1]
    #print(url)
    pid= url
    url_new = 'http://hjfdf.com/api/topic/'+pid
    HEADERS = {
        'Host': 'hjfdf.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Referer': url,
        'Cookie': 'token=bc9347774ae04b23994ebffe4776d8df; uid=5336321; user=%7B%22id%22%3A5336321%2C%22nickname%22%3A%221024_%u8349%u69B4_5336321%22%2C%22avatar%22%3A%2250%22%2C%22description%22%3A%22%u6D77%u89D2%u793E%u533A%u5185%u5BB9%u5F88%u68D2%uFF0C%u795D%u6D77%u89D2%u793E%u533A%u8D8A%u529E%u8D8A%u597D%u3002%22%2C%22topicCount%22%3A0%2C%22commentCount%22%3A0%2C%22fansCount%22%3A0%2C%22favoriteCount%22%3A0%2C%22status%22%3A0%2C%22sex%22%3A0%2C%22vip%22%3A0%2C%22vipExpiresTime%22%3A%222021-09-01%2000%3A00%3A00%22%2C%22certified%22%3Afalse%2C%22certVideo%22%3Afalse%2C%22certProfessor%22%3Afalse%2C%22famous%22%3Afalse%2C%22forbidden%22%3Afalse%2C%22tags%22%3Anull%2C%22role%22%3A0%2C%22diamondConsume%22%3A0%2C%22title%22%3A%7B%22id%22%3A0%2C%22name%22%3A%22%22%2C%22consume%22%3A0%2C%22consumeEnd%22%3A0%2C%22icon%22%3A%22%22%7D%2C%22friendStatus%22%3Afalse%2C%22voiceStatus%22%3Afalse%2C%22videoStatus%22%3Afalse%2C%22voiceMoneyType%22%3A0%2C%22voiceAmount%22%3A0%2C%22videoMoneyType%22%3A0%2C%22videoAmount%22%3A0%2C%22depositMoney%22%3A0%2C%22phone%22%3A%22%22%2C%22userBank%22%3Anull%2C%22parentId%22%3A0%2C%22gold%22%3A3000%2C%22diamond%22%3A0%2C%22passwordSet%22%3Atrue%2C%22payPasswordSet%22%3Afalse%2C%22popularity%22%3A10%2C%22topicLikeNum%22%3A0%2C%22bindUser%22%3A%22%22%2C%22username%22%3A%221024_%u62B1%u64CD%u59D0%u59D0mua%22%2C%22email%22%3A%221024_%u62B1%u64CD%u59D0%u59D0mua@hj.com%22%2C%22emailVerified%22%3Afalse%2C%22createTime%22%3A%222021-06-01%2004%3A17%3A38%22%2C%22lastLoginTime%22%3A%222022-08-20%2016%3A15%3A27%22%2C%22lastLoginIp%22%3A%222607%3Af130%3A0%3A156%3A%3Aea6b%3A5da5%22%2C%22certifiedExpired%22%3Afalse%2C%22certProfessorExpired%22%3Afalse%2C%22certVideoExpired%22%3Afalse%7D'
    }

    result = requests.get(url_new)
    result_body = json.loads(str((base64.b64decode(base64.b64decode(base64.b64decode(result.json()["data"])))),'utf-8'))
    #print(result_body)
    url_all = result_body["attachments"]
    title = result_body["title"]
    url_num = len(url_all)
    url_video = str(url_all[url_num-1]["remoteUrl"])
    url_cover = str(url_all[url_num-1]["coverUrl"])
    url_duan = url_video.split("/")
    time = url_duan[5]
    tag = url_duan[6]
    txt  = str(requests.get(url_video).content.decode("utf-8"))
    #print(txt)
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, txt)
    if url == []:
        tag2= txt.split("#EXTINF:1.250000,")[1].replace("0.ts",".m3u8").replace("\n","")
    else:
        url_0 = url[0][0]
    #print(url_0)
        txt2 = url_0.split("/")
        tag2 = txt2[7].replace("i0.ts","i.m3u8")
    url = "https://p.hjcfcf.com/hjstore/video/"+time+"/"+tag+"/"+tag2
    return render_template('hj.html',url=url,cover = url_cover,title = title)

@app.route("/", methods=["GET"])
def main2():
    url = 'http://hjfdf.com/post/details?pid=267410'
    #pid = url.split("=")[1]
    #print(url)
    pid= '267410'
    url_new = 'http://hjfdf.com/api/topic/'+pid
    HEADERS = {
        'Host': 'hjfdf.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Referer': url,
        'Cookie': 'token=bc9347774ae04b23994ebffe4776d8df; uid=5336321; user=%7B%22id%22%3A5336321%2C%22nickname%22%3A%221024_%u8349%u69B4_5336321%22%2C%22avatar%22%3A%2250%22%2C%22description%22%3A%22%u6D77%u89D2%u793E%u533A%u5185%u5BB9%u5F88%u68D2%uFF0C%u795D%u6D77%u89D2%u793E%u533A%u8D8A%u529E%u8D8A%u597D%u3002%22%2C%22topicCount%22%3A0%2C%22commentCount%22%3A0%2C%22fansCount%22%3A0%2C%22favoriteCount%22%3A0%2C%22status%22%3A0%2C%22sex%22%3A0%2C%22vip%22%3A0%2C%22vipExpiresTime%22%3A%222021-09-01%2000%3A00%3A00%22%2C%22certified%22%3Afalse%2C%22certVideo%22%3Afalse%2C%22certProfessor%22%3Afalse%2C%22famous%22%3Afalse%2C%22forbidden%22%3Afalse%2C%22tags%22%3Anull%2C%22role%22%3A0%2C%22diamondConsume%22%3A0%2C%22title%22%3A%7B%22id%22%3A0%2C%22name%22%3A%22%22%2C%22consume%22%3A0%2C%22consumeEnd%22%3A0%2C%22icon%22%3A%22%22%7D%2C%22friendStatus%22%3Afalse%2C%22voiceStatus%22%3Afalse%2C%22videoStatus%22%3Afalse%2C%22voiceMoneyType%22%3A0%2C%22voiceAmount%22%3A0%2C%22videoMoneyType%22%3A0%2C%22videoAmount%22%3A0%2C%22depositMoney%22%3A0%2C%22phone%22%3A%22%22%2C%22userBank%22%3Anull%2C%22parentId%22%3A0%2C%22gold%22%3A3000%2C%22diamond%22%3A0%2C%22passwordSet%22%3Atrue%2C%22payPasswordSet%22%3Afalse%2C%22popularity%22%3A10%2C%22topicLikeNum%22%3A0%2C%22bindUser%22%3A%22%22%2C%22username%22%3A%221024_%u62B1%u64CD%u59D0%u59D0mua%22%2C%22email%22%3A%221024_%u62B1%u64CD%u59D0%u59D0mua@hj.com%22%2C%22emailVerified%22%3Afalse%2C%22createTime%22%3A%222021-06-01%2004%3A17%3A38%22%2C%22lastLoginTime%22%3A%222022-08-20%2016%3A15%3A27%22%2C%22lastLoginIp%22%3A%222607%3Af130%3A0%3A156%3A%3Aea6b%3A5da5%22%2C%22certifiedExpired%22%3Afalse%2C%22certProfessorExpired%22%3Afalse%2C%22certVideoExpired%22%3Afalse%7D'
    }

    result = requests.get(url_new)
    result_body = json.loads(str((base64.b64decode(base64.b64decode(base64.b64decode(result.json()["data"])))),'utf-8'))
    #print(result_body)
    url_all = result_body["attachments"]
    title = result_body["title"]
    url_num = len(url_all)
    url_video = str(url_all[url_num-1]["remoteUrl"])
    url_cover = str(url_all[url_num-1]["coverUrl"])
    url_duan = url_video.split("/")
    time = url_duan[5]
    tag = url_duan[6]
    txt  = str(requests.get(url_video).content.decode("utf-8"))
    #print(txt)
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, txt)
    if url == []:
        tag2= txt.split("#EXTINF:1.250000,")[1].replace("0.ts",".m3u8").replace("\n","")
    else:
        url_0 = url[0][0]
    #print(url_0)
        txt2 = url_0.split("/")
        tag2 = txt2[7].replace("i0.ts","i.m3u8")
    url = "https://p.hjcfcf.com/hjstore/video/"+time+"/"+tag+"/"+tag2
    return render_template('hj.html',url=url,cover = url_cover,title = title)

if __name__ == '__main__':
    #main(1)
    app.run(host="0.0.0.0", port="666", debug=True)
