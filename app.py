from flask import Flask, render_template


app = Flask(__name__)

# welcome to my word of code ♥️

# products / a list individual  dictionarys 
products = [ {"name": "Red rose", "description": "Red  & organic"},
             {"name": "Mix flower ", "description": "Mix flower "},
             {"name": "Sun Flower ", "description": " Sun looking like"},
             {"name": "Pink Rose", "description": "Fresh and pike flower rose"},
             {"name": "Heart", "description": " Origin "} ]



@app.route('/') #index
def dashBorad():


    return render_template("home.html", products=products)


if __name__ == '__main__':
    app.run(debug=True)

