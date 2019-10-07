from flask import Flask, render_template, request, redirect, url_for
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
def dashBoard():


    return render_template("base.html", listings=listings.find())

@app.route('/listingForm')
def listing():

    
    return render_template('listingForm.html')

@app.route('/listings', methods=['POST'])
def listing_submit():

    # testing to see if infos from form was sent correctly
    print(request.form.to_dict())

    itemList = {'title': request.form.get('itemName'),
                'price': request.form.get("itemPrice" + '$')}

    listings.insert_one(itemList)
    return redirect(url_for('dashBoard'))



if __name__ == '__main__':
    app.run(debug=True)

