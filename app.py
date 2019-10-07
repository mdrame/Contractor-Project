from flask import Flask, render_template
from pymongo import MongoClient


app = Flask(__name__)

# welcome to my word of code ♥️

client = MongoClient()
db = client.Pure
listings = db.listings

# products / a list individual  dictionarys 
# products = [ {"name": "Red rose", "price": " $5.00 "},
#              {"name": "Mix flower ", "price": "$10.00 "},
#              {"name": "Sun Flower ", "price": "$20.00"},
#              {"name": "Pink Rose", "price": "$15.00"},
#              {"name": "Heart", "price": "$12.00"} ]



@app.route('/') #index
def dashBorad():


    return render_template("base.html")

@app.route('/listingForm')
def createListing():

    return render_template('listingForm.html')

@app.route('/home')
def viewItem():

    return render_template('home.html', listings=listings.find())


if __name__ == '__main__':
    app.run(debug=True)

