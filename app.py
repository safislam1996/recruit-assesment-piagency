from fnmatch import translate
from msilib.schema import File
from flask import render_template,Flask
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json

base_url = "https://translate.google.com/?"
driver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("headless")
app = Flask(__name__)
#  list_key=[]
#                 for i in file_language:
#                     i=i.lower()
#                     for x,y in languages.items():
#                         if(x==i):
#                             list_key.append(y)
l=open('languages.json')
languages=json.load(l)

def match_lang_tl(n,languages):
    list_key=[]

    tot=[x.lower() for x in n]
    # tot=['bangla', 'hindi', 'chinese', 'japanese']
    for i in tot:
        for x,y in languages.items():
                
                if(x==i):
                    list_key.append(y)
    return list_key
translate_list=[]
def url_scrape(tl,text):
                url=base_url+"sl=en"+"&tl="+tl+"&op=translate"
                driver.get(url)
                source=driver.find_element_by_class_name('er8xn')
                string=text.replace('.',' ')
                # string=string.replace('.',' ')
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
    
                return translate_list


def extract_languages(file):
            with open(file,'r') as xy:
                json_decode=json.load(xy)
            for item in json_decode:
                translate_dict={}
                translate_dict['text']=item.get('text')
                translate_dict['languages']=item.get('languages')
                # print(translate_dict['languages'])
                # print(translate_dict['text'])
                tl=match_lang_tl(translate_dict['languages'],languages)
                for t in tl:
                    # print(t)
                    translate=url_scrape(t,translate_dict['text'])
                    # print(translate)
                
                return translate

#this is a list             
the_dict=extract_languages('data.json')


driver.close()
@app.route("/")
def hello_world():
    text=the_dict[0].get('translated_text')
    languages=the_dict[0].get('languages')
    print(text)
    print(languages)
    
    return render_template('index.html', text=text,languages=languages,lang_len=len(languages))