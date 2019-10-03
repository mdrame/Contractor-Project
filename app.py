from flask import Flask, render_template


app = Flask(__name__)

# welcome to my word of code ♥️

@app.route('/') #index
def dashBorad():

    message = ' Welcome to the Pure '

    return(message)


if __name__ == '__main__':
    app.run(debug=True)

