from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def hello_dojo():
    return "Dojo!"

@app.route('/say/<whoever>') #TTT 
def hello_whoever(whoever):
    x = "Hello, " + whoever + "!"
    return x

@app.route('/repeat/<int:count>/<name>')
def repeat_this(count, name):
    x = count * name
    return x

if __name__ == "__main__":
    app.run(debug=True)