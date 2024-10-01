$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});


// call Flask API endpoint
function makePredictions() {
    console.log('logic function called')
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

    console.log(SkinCancer)

    // check if inputs are valid

    // create the payload
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
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            var prob = parseFloat(returnedData["prediction"]);

            if (prob > 0.5) {
                $("#output").text(`You had Hart Attack with probability ${prob}!`);
            } else {
                $("#output").text(`You did not have Hard Attack with probability ${prob}, sorry. :(`);
            }

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}
