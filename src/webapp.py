import os, sys, csv, cv2, subprocess, numpy
from subprocess import call
#import video_emotion_color_demo_rahul as veg
#import speech_recognition as sr
from flask import Flask, render_template, request
from werkzeug import secure_filename
#import searchresults as searchresults
import test_trained_webcam as face_reco
from flask_sqlalchemy import SQLAlchemy
import unicodedata
#from DB import Actor



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site1.db'
app.config['UPLOAD_FOLDER']='/home/yash/Desktop/Final/Face reco KNN/src/uploadfolder'
db=SQLAlchemy(app)



class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    actorname = db.Column(db.String(50))
    frameno = db.Column(db.Integer)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    z = db.Column(db.Integer)
    w = db.Column(db.Integer)

    def __repr__(self):
        #return "Actor('{self.actorname}', '{self.frameno}', '{self.image_file}','{self.x}','{self.y}','{self.z}','{self.w}')"
        return "Actor('{}', '{}', '{}','{}','{}','{}','{}')".format(self.actorname,self.frameno,self.image_file,self.x,self.y,self.z,self.w)

db.create_all()



APP_ROOT = os.path.dirname(os.path.abspath(__file__))


mypath = '/home/'
videofiles = []
csvfiles = []
d = []
e = []
frame_no = []
thumbnail_time = []
files = os.listdir(mypath)
sep = '.'


@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/upload", methods=['POST'])
def upload():
    for file in request.files.getlist("file"):
        filename = secure_filename(file.filename)
        print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        destination=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(destination)
        face_reco.faceRec(destination)
  
    return render_template("complete.html", value = destination)


actor_dict={}

@app.route("/search", methods=['GET', 'POST'])
def search():

    Query=request.form['query']
    Query=Query.split(" ")
    Actorss=Actor.query.all()
    print(Actorss)
    for act in Actorss:
        if act.actorname in actor_dict.keys():
            actor_dict[act.actorname].append(act.frameno)
        else:
            actor_dict[act.actorname]=[]
            actor_dict[act.actorname].append(act.frameno)

    print(actor_dict)
    #Query=['salmankhan','amitabhbachchan']
    for i in actor_dict.keys():
        actor_dict[i]=set(actor_dict[i])
    print(actor_dict[Query[0]].intersection(actor_dict[Query[1]]))

    return render_template("complete.html")

            
            

    
# with open(win.csvname, 'rt') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         for element in row[4].split(" "):
#             #print('Entering for loop')
#             if row[4] in actordic.keys():
#                 actordic[row[4]].append(row[1])
#             else:
#                 actordic[row[4]]=[]
#                 actordic[row[4]].append(row[1])


# @app.route("/search", methods=['GET', 'POST'])
# def search():
    # for file in os.listdir(mypath):
    #     if file.endswith(".csv"):
    #         a = file.split(sep, 1)[0]
    #         t = file.split('.')
    #         #e = e + t
    #         e.append(t[0])
    #         e.append(t[1])
    #         csvfiles.append(a)


    # for file in os.listdir(mypath):
    #     if file.endswith((".mp4", ".mkv", ".flv", ".wmv", ".avi", ".mpg", ".mpeg")):
    #         b = file.split(sep, 1)[0]
    #         t = file.split('.')
        
    #         videofiles.append(b)

    # print(e)
    # c = list(set(videofiles).intersection(set(csvfiles)))

    # destination = []
    # j=0
    # for j in range(len(e)):
    #     for i in range(len(c)):
    #         if(c[i]==e[j]):
    #             c[i]=c[i] + '.' + e[j+1]
    #             exe=c[i]
    #             print(os.path.abspath(c[i]))
    #             #i = i + 1
    #             #j = j + 2
    #     j=j+1
    # name = []
    # name = request.form['Query']
    # filepath = os.path.abspath(c[i])
    # frame_no = searchresults.process(filepath, name)

##    cap = cv2.VideoCapture(filepath)
##    fps = cap.get(cv2.CAP_PROP_FPS)
##    for p in range(len(frame_no)):
##        cap.set(1, float(frame_no[p]))
##        ret, frame = cap.read()
##        cv2.imwrite('trial%d.jpg' % float(frame_no[p]), frame)     
##        thumbnail_time[p] = float(frame_no[p]/fps)
##
##
##    return render_template("thumbnail.html", filepathvalue = filepath, thumbnailvalue = thumbnail_time  )


if __name__ == "__main__":
    app.run(debug = True)

##    cap = cv2.VideoCapture('joined-all.mp4')
##    for p in range(len(frame_no)):
##        vdo.vpl(fra)
##        print("Video number "+ str(p+1) +" has ended.")
##
        
##        print(" Entering the for loop")
##        cap.set(1, float(frame_no[p]))
##        
##        print(" The frame with the required actor and the object is : " + frame_no[p])
##        ret, frame = cap.read()
##        cv2.imshow('window_name', frame)
##        while True:
##            ch = 0xFF & cv2.waitKey(1)
##            if ch == 27:
##                break 
