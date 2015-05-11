# encoding: utf-8
#-*- coding=utf-8 -*-
import urllib, urllib2, cookielib, re, json, time
import xml.etree.ElementTree as ET
from pyquery import PyQuery as pyq
import requests

def request_weixin(query ,qtype=1):
  url = 'http://weixin.sogou.com/weixin?type=%d&query=%s'
  doc = pyq(url=(url % (qtype, query)))
  weixin_list = doc(".results>div").items()
  for item in weixin_list:
    openid = item.attr['href'][12:]
    name = item(".txt-box>h3").text()
    weixin_num = item(".txt-box>h4>span").text()[4:]
    print(name + ": " + weixin_num + " " + openid)

def request_articles(openid,page=1):
  url = 'http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=%s&page=%d&t=%d'
  now = int(time.time())
  content = requests.get(url % (openid, page, now)).text

  json_data = re.findall(r'\nsogou.weixin.gzhcb\((\{.+\})\)', content)[0]
  items = json.loads(json_data)['items']
  for item in items:
    item = item.encode("utf-8")
    item = item.replace('<?xml version="1.0" encoding="gbk"?>','<?xml version="1.0" encoding="utf-8"?>')
    root = ET.fromstring(item)
    title = root.find("./item/display/title").text
    url = root.find("./item/display/url").text
    date = root.find("./item/display/date").text
    print title
    print url
    print date

request_weixin("1")
request_articles("oIWsFt4VA51ZzVFr-upBr8Qx9d4w")