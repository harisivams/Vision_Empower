from flask import Flask, render_template, flash, request, session
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#from werkzeug.utils import secure_filename
from PIL import Image, ImageChops,ImageStat

import mysql.connector
import sys, fsdk, math, ctypes, time
import datetime
#verified

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

from datetime import date
start_date=date.today()

@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/Home")
def Home():
    return render_template('index.html')

@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')

@app.route("/finger")
def finger():
    return render_template('Finger.html')

@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' or request.form['password'] == 'admin':
           conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facefingdb')
           cursor = conn.cursor()
           cur = conn.cursor()
           cur.execute("SELECT * FROM regtb")
           data = cur.fetchall()
           return render_template('AdminHome.html', data=data)
       else:
        return render_template('index.html', error=error)

@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facefingdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/NewStudent")
def NewStudent():
    import LiveRecognition  as liv
    liv.att()
    del sys.modules["LiveRecognition"]
    return render_template('NewUser.html')

@app.route("/NewStudent1", methods=['GET', 'POST'])
def NewStudent1():
     if request.method == 'POST':
          regno = request.form['regno']
          name = request.form['name']
          gender = request.form['gender']
          Age = request.form['Age']
          email = request.form['email']
          pnumber = request.form['pnumber']
          address = request.form['address']
          file = request.files['file']
          file.save("static/upload/" + file.filename)
          conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facefingdb')
          cursor = conn.cursor()
          cursor.execute("insert into regtb values('"+regno+"','"+name+"','"+gender+"','"+Age+"','"+email+"','"+pnumber+"','"+address +"','"+file.filename+"')")
          conn.commit()
          conn.close()
     conn = mysql.connector.connect(user='root', password='', host='localhost', database='1facefingdb')
     cur = conn.cursor()
     cur.execute("SELECT * FROM regtb")
     data = cur.fetchall()
     return render_template('AdminHome.html', data=data)

@app.route("/searchid")
def searchid():

    #session['eid']=eid
    import LiveRecognition1  as liv1
    liv1.examvales()

    #liv1.att()

    #print(ExamName)

    del sys.modules["LiveRecognition1"]
    # import the opencv library
    from keras.models import load_model
    from time import sleep
    from keras_preprocessing.image import img_to_array
    from keras.preprocessing import image
    import cv2
    import numpy as np
    import time
    face_classifier = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
    classifier = load_model(r'model.h5')

    emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        labels = []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                prediction = classifier.predict(roi)[0]
                label = emotion_labels[prediction.argmax()]
                print(label)
                label_position = (x, y)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                from gtts import gTTS
                from playsound import playsound

                from LiveRecognition1 import ss
                mytext = label
                #  mytext = str(ss)+str(label)
                language = 'en'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("welcome.mp3")
                time.sleep(5)
                playsound('H:\emotion and face identification\emotion and face identification\welcome.mp3')

            else:
                cv2.putText(frame, 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Emotion Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



    return "Known User"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)