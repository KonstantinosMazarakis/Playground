from distutils.log import debug
from flask import Flask, render_template
app = Flask(__name__)



@app.route('/play')
def lvl1():
    return  render_template("index.html", id = 3)


@app.route('/play/<int:id>')
def lvl2(id):
    return  render_template("index.html", id = id)



@app.route('/play/<int:id>/<color>')
def lvl3(id,color):
    return  render_template("index.html", id = id,color = color)





if __name__=="__main__":
    app.run(debug=True)