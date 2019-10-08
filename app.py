from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
# this under help change Mongodb _id to an object 
from bson.objectid import ObjectId


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

    
    return render_template('listingForm.html', playlist={}, listingTitle='Create Listing')

# this function / route is appendig the listing to my local mongo db
@app.route('/listings', methods=['POST'])
def listing_submit():

    ''' create a dictionary of listing 
    form name and price & inseart it into listings db '''

    # testing to see if infos from form was sent correctly
    # print(request.form.to_dict())

    itemList = {'title': request.form.get('itemName'),
                'price': request.form.get("itemPrice")}

    listing_id = listings.insert_one(itemList).inserted_id
    return redirect(url_for('viewProduct', listing_id=listing_id))

# route to view individual listing | Read in CRUD
@app.route('/<listing_id>')
def viewProduct(listing_id):

    listing = listings.find_one({'_id': ObjectId(listing_id)})
    return render_template('viewProduct.html', listing=listing)

@app.route('/<listing_id>/edit')
def listing_edit(listing_id):
    listing = listings.find_one({'_id': ObjectId(listing_id)})
    return render_template('listingForm.html', listing=listing, listingTitle="Edit Listing")

# update_listing
@app.route('/<listing_id>', methods=['POST'])
def update_listing(listing_id):

    updated_listing = {
        'title': request.form.get('itemName'),
        'price': request.form.get('itemPrice')
    }

    listings.update_one(
        {'_id': ObjectId(listing_id)}, 
        {'$set': updated_listing})

    return redirect(url_for('viewProduct', listing_id=listing_id))

# delete listing route 
@app.route('/<listing_id>/delete', methods=['POST'])
def delete_listing(listing_id):

    listings.delete_one({'_id': ObjectId(listing_id)})
    return redirect(url_for('dashBoard'))

if __name__ == '__main__':
    app.run(debug=True)

