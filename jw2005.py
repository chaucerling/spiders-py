#!/usr/bin/env python
# encoding: utf-8
#-*- coding=utf-8 -*-
import urllib, urllib2, cookielib, re, json, time
import xml.etree.ElementTree as ET
from pyquery import PyQuery as pyq
import requests
# for item in cookie:
# header response.info()

def request(url, values={}, headers={}, get_cookie=False, set_cookie=None):
  if set_cookie is None:
    response_cookie = cookielib.CookieJar()
  else:
    response_cookie = set_cookie
  urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(response_cookie))
  post_data = urllib.urlencode(values)
  request = urllib2.Request(url, post_data, headers)
  response = urlOpener.open(request)
  if get_cookie == False:
    return response
  else:
    return response, response_cookie

def login():
  #get_login_url
  jw2005_url = 'http://jw2005.scuteo.com/'
  response = request(url=jw2005_url)
  #http://222.201.132.117/(nouuvu55yi1bpk45tz3rhkjy)/default2.aspx

  array = response.geturl().split("/")
  array[4] = "default6.aspx"
  login_url = "/".join(array)
  #http://222.201.132.117/(nouuvu55yi1bpk45tz3rhkjy)/default6.aspx

  doc = pyq(url=login_url)
  viewstate = doc("#Form1 input")[0].value

  id = 123
  passowrd = 123
  values = {
  '__VIEWSTATE' : viewstate,
  # tname:
  # tbtns:
  'tnameXw':"yhdl",
  'tbtnsXw':"yhdl|xwxsdl",
  'txtYhm':id,
  # txtXm:
  'txtMm':passowrd,
  "rblJs":"",
  "btnDl":""#.decode('gbk').encode('gbk'),
  }
  headers = {}
  response, response_cookie = request(login_url, values, headers, True)
  return response.geturl()

# if "xs_main.aspx" in login():
#   print "login successful"

