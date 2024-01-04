from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', defaults={'x' : 8, 'y' : 8, 'color' : 'red'})
def hello_checkerboard(x,y,color):
    return render_template('index.html', x=x, y=y, color=color)

@app.route('/<int:x>', defaults={'y' : 8, 'color' : 'red'})
def hello_checkerboard_2(x,y,color):
    return render_template('index.html', x=x, y=y, color=color)

@app.route('/<int:x>/<int:y>', defaults={'color' : 'red'})
def hello_checkerboard_3(x,y,color):
    return render_template('index.html', x=x, y=y, color=color)

@app.route('/<int:x>/<int:y>/<string:color>')
def hello_checkerboard_4(x,y,color):
    return render_template('index.html', x=x, y=y, color=color)

if __name__ == "__main__":
    app.run(debug=True)