from flask import Flask, render_template,request,send_file,send_from_directory
from advanced_apriori import *
from data_preparation import *
from keyword_extractor import *
from working_utilities import *
from diag_helper import *



app=Flask(__name__,static_folder='static')
@app.route("/")
def home():
   return render_template("index.html")

@app.route('/<path:filename>')  
def send_file(filename):  
    return send_from_directory(app.static_folder, filename)

@app.route("/diagnose", methods=["POST"])
def show_diagnosis():

    f_name = request.form['firstname']
    l_name = request.form['lastname']
    gender = request.form['gender']
    symptoms= request.form['symptoms'] 

    result_string= diagnose(symptoms)
    return render_template('result.html', results=result_string)

if __name__ == "__main__":
    app.run(debug=True)