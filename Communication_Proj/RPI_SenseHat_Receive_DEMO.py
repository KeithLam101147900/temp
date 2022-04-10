import pyrebase
import random
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

# Create new Firebase config and database object
config = {
  "apiKey": "AIzaSyAmHtdWuIyvGzFkxE_NNc7hMBMIDZ4eG7s",
  "authDomain": "sysc3010-project-l1g3.firebaseapp.com",
  "databaseURL": "https://sysc3010-project-l1g3-default-rtdb.firebaseio.com/",
  "storageBucket": "sysc3010-project-l1g3.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

RpiData = db.child("RPI_Display").get()
x = RpiData.each()
    
print(x[0].val())
print(x[1].val())
print(x[2].val())
print(x[3].val())