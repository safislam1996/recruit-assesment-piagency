#!/usr/bin/env python
# -*- coding: utf8 -*-
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from flask import render_template,Flask

app=Flask()
l=open('languages.json')
f=open('data.json')
languages=json.load(l)

file=json.load(f)
base_url = "https://translate.google.com/?"
driver = webdriver.Chrome(ChromeDriverManager().install())

file_language=list(file[0]['languages'])

list_key=[]
for i in file_language:
    i=i.lower()
    for x,y in languages.items():
        if(x==i):
            list_key.append(y)
# print(list_key)
translate_list=[]

 
for tl in list_key:
    # print(tl)
    url=base_url+"sl=en"+"&tl="+tl+"&op=translate"
    # print(url)
    driver.get(url)
    source=driver.find_element_by_class_name('er8xn')
    string=file[0]['text']
    string=string.replace('.',' ')
    # print(string)
    result=source.send_keys(string)
    driver.implicitly_wait(20)
    translate=driver.find_element_by_xpath("//span[@class='Q4iAWc']")
    driver.implicitly_wait(10)
    
    translate_dict={
    'language':tl,
    'translated_text':translate.text
        }
    translate_list.append(translate_dict)
    
print(translate_list)
@app.route('/')
def index():
    return 
driver.close()  
