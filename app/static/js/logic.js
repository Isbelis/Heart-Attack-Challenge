$(document).ready(function() {
    console.log("Page Loaded");

    // Attach event handler
    $("#filter").click(function() {
        makePredictions();  // Calls the prediction function
    });
});


function makePredictions() {
    console.log('logic function called');
    var BMI = $("#BMI").val();
    var Smoking = $("#Smoking").val();
    var AlcoholDrinking = $("#AlcoholDrinking").val();
    var Stroke = $("#Stroke").val();
    var PhysicalHealth = $("#PhysicalHealth").val();
    var MentalHealth = $("#MentalHealth").val();
    var DiffWalking = $("#DiffWalking").val();
    var Sex = $("#Sex").val();
    var AgeCategory = $("#AgeCategory").val();
    var Race = $("#Race").val();
    var Diabetic = $("#Diabetic").val();
    var PhysicalActivity = $("#PhysicalActivity").val();
    var GenHealth = $("#GenHealth").val();
    var SleepTime = $("#SleepTime").val();
    var Asthma = $("#Asthma").val();
    var KidneyDisease = $("#KidneyDisease").val();
    var SkinCancer = $("#SkinCancer").val();

    // Create the payload
    var payload = {
        'BMI' : BMI,
        'Smoking' : Smoking,
        'AlcoholDrinking' : AlcoholDrinking,
        'Stroke' : Stroke,
        'PhysicalHealth' : PhysicalHealth,
        'MentalHealth' : MentalHealth,
        'DiffWalking' : DiffWalking,
        'Sex' : Sex,
        'AgeCategory' : AgeCategory,
        'Race' : Race,
        'Diabetic' : Diabetic,
        'PhysicalActivity' : PhysicalActivity,
        'GenHealth' : GenHealth,
        'SleepTime' : SleepTime,
        'Asthma' : Asthma,
        'KidneyDisease' : KidneyDisease,
        'SkinCancer' : SkinCancer
    };

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePrediction", // Correct endpoint
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // Handle success
            var prediction = returnedData["prediction"];
            $("#output").text(`Prediction Result: ${prediction}`);
        },
        error: function(xhr, status, error) {
            // Handle error
            $("#output").text(`An error occurred: ${error}`);
        }
    });
}

