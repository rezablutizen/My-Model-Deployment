from flask import Flask, render_template, request

import pengunjung as p

app = Flask(__name__)
@app.route("/", methods = ["GET","POST"] )
def pengunjung():
    mk = None
    if request.method == "POST":
        hrs = request.form["hrs"]
        pengunjung_pred = p.pengunjung_prediction(int(hrs))
        mk = pengunjung_pred
    return render_template("index.html", my_pengunjung = mk)



"""
@app.route("/sub", methods = ["POST"])
def submit():
    if request.method == "POST":
        name = request.form["username"]
    return render_template("sub.html", n = name)
"""  

if __name__ =="__main__":
    app.run(debug=True)
