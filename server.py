from distutils.log import debug
from flask import Flask, render_template
app = Flask(__name__)



@app.route('/play')
def lvl1():
    container = '<div class="container box m-1 flex"></div>'
    return  render_template("index.html", id = 3, container = container, color = "blue")


@app.route('/play/<int:id>')
def lvl2(id):
    container = '<div class="container box m-1 flex"></div>'
    return  render_template("index.html", id = id , container = container, color = "blue")



@app.route('/play/<int:id>/<color>')
def lvl3(id,color):
        container = '<div class="container box m-1 flex"></div>'
        return  render_template("index.html", id = id,color = color , container = container)





if __name__=="__main__":
    app.run(debug=True)