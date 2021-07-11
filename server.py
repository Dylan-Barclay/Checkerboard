from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', coloum = 8, row = 8)

@app.route('/<int:row>')
def row(row):
    return render_template('index.html', coloum = 8, row=row)

@app.route('/<int:row>/<int:coloum>')
def row_coloum(row,coloum):
    return render_template('index.html', coloum = coloum, row=row)

@app.route('/<int:row>/<int:coloum>/<string:color1>/<string:color2>')
def color(row,coloum,color1,color2):
    return render_template('color.html', coloum = coloum, row=row, color1 = color1, color2 = color2)

if __name__=="__main__":
    app.run(debug=True)