from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests
import os
from functools import wraps
from flask import g, url_for
from flask import Flask, render_template, request
from flask_restful import  Api, Resource
from flask_jwt import JWT
from flask_cors import CORS # for allow-cross-origin issues
import sqlite3 as sql
#from security import authenticate, identity
#from resources.user import UserRegister
#from resources.item import Book, BookList

#from user import UserRegister
#from item import Item

import glob,os

from sqlalchemy.engine import Engine
from sqlalchemy import event

import models as dbHandler
import hashlib
from flask import send_from_directory



app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
app.secret_key = 'jose'
api = Api(app)



#@app.before_first_request
#def create_tables():
#    db.create_all()

#api.add_resource(Item, '/item/<string:name>')

def validate(username, password):
    #con = sqlite3.connect('static/user.db')
    connection = sql.connect('data.db')

    completion = False
    with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM user")
                rows = cursor.fetchall()
                for row in rows:
                    dbUser = row[1]
                    dimos = row[3]
                    nomos = row[4]
                    #dimos = row[5]
                    #print(five,fourth,third)
                    dbPass = row[2]
                    global dbId
                    global userName
                    userName = dbUser
                    dbId = row[0]
                    if dbUser==username and dbPass==password :
                        completion = True
                        print (dbId)
    return completion,dimos,nomos

#def check_password(hashed_password, user_password):
#    return hashed_password == hashlib.md5(user_password.encode()).hexdigest()

@app.route('/register')
def home():
    #if not session.get('logged_in'):
    #    return render_template('login.html')
    #else:
        #return "Hello Boss!"
        return render_template('register.html')

@app.route('/')
def first():
    #if not session.get('logged_in'):
    #    return render_template('login.html')
    #else:
        #return "Hello Boss!"
        return render_template('first.html')

@app.route('/index')
def index():

        return render_template('index.html')


@app.route('/apotelesmata')
def apotelesmata():

        return render_template('apotelesmata.html')


@app.route('/kathariotita')
def kathariotita():

        return render_template('kathariotita.html')

@app.route('/loginPage')
def loginPage():

        return render_template('login.html')

@app.route('/koinonikiPolitiki')
def koinonikiPolitiki():

        return render_template('koinonikiPolitiki.html')

@app.route('/simetoxi')
def simetoxi():

        return render_template('simetoxi.html')

@app.route('/erwtiseis')
def erwtiseis():

        return render_template('taxis.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        print(completion)
        print(completion[2])
        print(completion[1])
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
            print (error)
        else:
            #session['logged_in'] = True
            return render_template('index.html',nomos = completion[2],dimos = completion[1] )
        return render_template('login.html', error=error)


@app.route('/quest', methods = ['GET', 'POST'])
def quest():
   if request.method == 'POST':

         questId = 1
         value1=request.form['example1']
         value2=request.form['example2']
         value3=request.form['example3']


         print(value1,value2,value3)

         connection = sql.connect('data.db')
         cursor = connection.cursor()

         print ("Opened database successfully")
         query = "INSERT INTO results(value1,value2,value3,questId) VALUES(?,?,?,?)"
         cursor.execute(query, (value1, value2, value3,questId))

         connection.commit()

         connection.row_factory = sql.Row

         cursor.execute("select * from results")

         rows = cursor.fetchall();
         print(cursor.fetchall())
         for row in rows:
            print(row)

         print('Record was successfully added')
         return render_template('kathariotita.html')


   return render_template('kathariotita.html')


@app.route('/chart/', methods = ['GET', 'POST'])
def chart():
   if request.method == 'GET':

         print('Hola')
         connection = sql.connect('data.db')
         print(connection)
         cursor = connection.cursor()

         print ("Opened database successfully")
         #query = "INSERT INTO results(value1,value2,value3,questId) VALUES(?,?,?,?)"
         #cursor.execute(query, (value1, value2, value3,questId)
         connection.commit()

         connection.row_factory = sql.Row

         cursor.execute("select * from results where questId=1")

         rows = cursor.fetchall();
         print(cursor.fetchall())
         results = []
         question1 =[]
         question2 =[]
         question3 =[]
         q1 =0
         q2 =0
         q3 =0
         q4 =0
         q5=0
         q6 =0
         q7 =0
         q8 =0
         q9 =0
         q10=0
         q11 =0
         q12 =0
         q13 =0
         q14 =0
         q15=0


         for row in rows:
            #print(row[1])
            print(row)
            question1.append(row[1])
            #print(question1)
            question2.append(row[2])
            question3.append(row[3])
            results.append(row)


         print("first question results",question1)

         for item in question1:
             if(item ==1):
                 q1 = q1 +1
             elif(item ==2):
                q2 = q2 +1
             elif(item ==3):
                 q3 = q3 +1
             elif(item ==4):
                 q4 = q4 +1
             elif(item ==5):
                 q5 = q5 +1


         #print(q1,q2,q3,q4,q5)

         percent1quest1 = (q1/len(question1))*100
         percent2quest1 = (q2/len(question1))*100
         percent3quest1 = (q3/len(question1))*100
         percent4quest1 = (q4/len(question1))*100
         percent5quest1 = (q5/len(question1))*100

         #print(percent1quest1,percent2quest1,percent3quest1,percent4quest1,percent5quest1)


         jsonFirst ={
            "first1":percent1quest1,
            "first2":percent2quest1,
            "first3":percent3quest1,
            "first4":percent4quest1,
            "first5":percent5quest1,

         }

         print(jsonFirst)

         print("second question results",question2)

         for item in question2:
             if(item ==1):
                 q6 = q6 +1
             elif(item ==2):
                q7 = q7 +1
             elif(item ==3):
                 q8 = q8 +1
             elif(item ==4):
                 q9 = q9 +1
             elif(item ==5):
                 q10 = q10 +1


         #print(q1,q2,q3,q4,q5)

         percent1quest2 = (q6/len(question1))*100
         percent2quest2 = (q7/len(question1))*100
         percent3quest2 = (q8/len(question1))*100
         percent4quest2 = (q9/len(question1))*100
         percent5quest2 = (q10/len(question1))*100

         #print(percent1quest1,percent2quest1,percent3quest1,percent4quest1,percent5quest1)


         jsonSecond ={
            "first1":percent1quest2,
            "first2":percent2quest2,
            "first3":percent3quest2,
            "first4":percent4quest2,
            "first5":percent5quest2,

         }

         print(jsonSecond)


         print("third question results",question3)

         for item in question3:
             if(item ==1):
                 q11 = q11 +1
             elif(item ==2):
                q12 = q12 +1
             elif(item ==3):
                 q13 = q13 +1
             elif(item ==4):
                 q14 = q14 +1
             elif(item ==5):
                 q15 = q15 +1


         #print(q1,q2,q3,q4,q5)

         percent1quest3 = (q11/len(question1))*100
         percent2quest3 = (q12/len(question1))*100
         percent3quest3 = (q13/len(question1))*100
         percent4quest3 = (q14/len(question1))*100
         percent5quest3 = (q15/len(question1))*100

         #print(percent1quest1,percent2quest1,percent3quest1,percent4quest1,percent5quest1)


         jsonThird ={
            "first1":percent1quest3,
            "first2":percent2quest3,
            "first3":percent3quest3,
            "first4":percent4quest3,
            "first5":percent5quest3,

         }

         print(jsonThird)


         print(results)
         print('Record was successfully added')

         return render_template('newChart.html',jsonfirst=jsonFirst,jsonSecond=jsonSecond,jsonThird=jsonThird)

   return render_template('newChart.html')


@app.route('/social', methods = ['GET', 'POST'])
def social():
   if request.method == 'POST':

         questId = 2
         value1=request.form['example1']
         value2=request.form['example2']
         value3=request.form['example3']


         print(value1,value2,value3)

         connection = sql.connect('data.db')
         cursor = connection.cursor()

         print ("Opened database successfully")
         query = "INSERT INTO results(value1,value2,value3,questId) VALUES(?,?,?,?)"
         cursor.execute(query, (value1, value2, value3,questId))

         connection.commit()

         connection.row_factory = sql.Row

         cursor.execute("select * from results")

         rows = cursor.fetchall();
         print(cursor.fetchall())
         for row in rows:
            print(row)

         print('Record was successfully added')

         return render_template('kathariotita.html')


   return render_template('kathariotita.html')


@app.route('/registerUser', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      print('HI')
      if not request.form['userName'] or not request.form['userPass']:
         print('Please enter all the fields', 'error')
         return render_template('register.html')
      else:
         userName=request.form['userName']

         print(userName)
         userPass=request.form['userPass']
         lastName=request.form['lastname']
         firstName=request.form['firstname']
         daddy=request.form['daddy']
         mommy=request.form['mommy']
         birthdate=request.form['birthdate']

         print(userName,lastName,firstName,daddy,mommy,birthdate)
         connection = sql.connect('data.db')
         cursor = connection.cursor()

         print ("Opened database successfully")


         browser = webdriver.Firefox()

         #session_requests = requests.session()
         browser.get(('http://www.ypes.gr/services/eea/dimos/eea.htm'))


         Eponymo = lastName
         etos_gen = birthdate
         MfcISAPICommand = "Search",
         on_mht =mommy
         on_pat = daddy
         Onoma=firstName

         elem = browser.find_element_by_name("Eponymo")#j_username -- OAED
         elem.send_keys(Eponymo)
         time.sleep(1)

         elem = browser.find_element_by_name("on_pat")#j_password -- OAED
         elem.send_keys(on_pat)
         time.sleep(1)


         elem = browser.find_element_by_name("etos_gen")#j_username -- OAED
         elem.send_keys(etos_gen)
         time.sleep(1)

         elem = browser.find_element_by_name("on_mht")#j_password -- OAED
         elem.send_keys(on_mht)
         time.sleep(1)


         elem = browser.find_element_by_name("Onoma")#j_password -- OAED
         elem.send_keys(Onoma)
         time.sleep(1)

         elem = browser.find_element_by_xpath("//input[@value='Αναζήτηση']");
         elem.click()
         time.sleep(1)

         soup = BeautifulSoup(browser.page_source, "lxml")

         print(soup)


         my_headers = []

         for item in soup.find_all("td", class_="t2"):
             my_headers.append(item.text)

         print (my_headers)
         length = len(my_headers)

         code = my_headers[length-1]

         print(code)
         nomos = my_headers[length-2]

         print(nomos)

         dimos = my_headers[length-3]

         print(dimos)

         print(firstName,userPass,dimos,nomos,code)

         #cursor = connection.cursor()
         query = "INSERT INTO user(userName,userPass,dimos, nomos,code) VALUES(?,?,?,?,?)"
         cursor.execute(query, (userName, userPass, dimos, nomos,code))

         connection.commit()


         connection.row_factory = sql.Row

         cursor.execute("select * from user")

         rows = cursor.fetchall();
         print(cursor.fetchall())
         for row in rows:
             print(row)

         print('Record was successfully added')


         return render_template('index.html')


   return render_template('register.html')


if __name__ == "__main__":

    app.run(port=5000, debug=True)
