from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return "<html><body><h1 style='color:red'>Hello world!</h1></body></html>"

@app.route('/products')
def drink():
    return "<html><body><h1 style='color:green'>Here is yo coffee!</h1></body></html>"

if __name__ == "__main__":
   app.run(host='0.0.0.0')