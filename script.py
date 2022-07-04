
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fpdf import FPDF
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
pdf = FPDF()  
pdf.add_page() 
for tl in list_key:
    print(tl)
    url=base_url+"sl=en"+"&tl="+tl+"&op=translate"
    print(url)
    driver.get(url)
    source=driver.find_element_by_class_name('er8xn')
    string=file[0]['text']
    string=string.replace('.',' ')
    print(string)
    result=source.send_keys(string)
    driver.implicitly_wait(20)
    translate=driver.find_element_by_xpath("//span[@class='Q4iAWc']")
    driver.implicitly_wait(10) 
    print(translate.text)
    
    # pdf.set_font("Arial", size = 15) 
    # pdf.multi_cell(200, 10, txt = i,  
    #      align = 'C')
    # pdf.multi_cell(200, 10, txt =translate.text, 
    #       align = 'C')

# pdf.output("PP1.pdf") 
driver.close()  

# sl="en"

# tl="bn"

# 
# print(url)
# driver.get(url)

