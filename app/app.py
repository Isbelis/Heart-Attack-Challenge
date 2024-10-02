from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("report.html")

@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")


@app.route("/works_cited")
def works_cited():
    # Return template and data
    return render_template("works_cited.html")

@app.route("/ml_live_form")
def ml_live_form():
    # Return template and data
    return render_template("ml_live_form.html")


@app.route("/makePrediction", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print('app route called')
    
    # Parse incoming JSON
    BMI = int(content['BMI'])
    Smoking = content['Smoking']
    AlcoholDrinking = content['AlcoholDrinking']
    Stroke = content['Stroke']
    PhysicalHealth = int(content['PhysicalHealth'])
    MentalHealth = int(content['MentalHealth'])
    DiffWalking = content['DiffWalking']
    Sex = content['Sex']
    AgeCategory = content['AgeCategory']
    Race = content['Race']
    Diabetic = content['Diabetic']
    PhysicalActivity = content['PhysicalActivity']
    GenHealth = content['GenHealth']
    SleepTime = int(content['SleepTime'])
    Asthma = content['Asthma']
    KidneyDisease = content['KidneyDisease']
    SkinCancer = content['SkinCancer']

    # Make prediction using the ModelHelper
    prediction = modelHelper.makePredictions(
        BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth, DiffWalking, Sex,
        AgeCategory, Race, Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer
    )

    # Return the prediction as JSON response
    return jsonify({"prediction": prediction})



@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
