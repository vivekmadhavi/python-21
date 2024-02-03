from pyrebase import * 

firebaseConfig = {
  "apiKey": "AIzaSyCYhvbcS4FE3-2qepb2JcY1bpnqphjmmTo",
  "authDomain": "feedback30dec23-42c78.firebaseapp.com",
  "databaseURL": "https://feedback30dec23-42c78-default-rtdb.firebaseio.com",
  "projectId": "feedback30dec23-42c78",
  "storageBucket": "feedback30dec23-42c78.appspot.com",
  "messagingSenderId": "604759817357",
  "appId": "1:604759817357:web:487aa5fee362ed02e676c4"
}

fb = initialize_app(firebaseConfig)

db = fb.database()
name = input("enter name ")
feedback = input("enter feedback ")
info = {"name":name , "feedback" : feedback}
db.child("fb").push(info)
print("thanks u for ur feedback")