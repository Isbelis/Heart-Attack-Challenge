$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});


// call Flask API endpoint
function makePredictions() {
    var sex_flag = $("#gender").val();
    var BMI = $("#BMI").val();
    var SmokerStatus = $("#SmokerStatus").val();
    var GeneralHealth = $("#GeneralHealth").val();
    var AgeCategory = $("#AgeCategory").val();
    // var race
   
    // check if inputs are valid

    // create the payload
    var payload = {
        "sex_flag": sex_flag,
        "BMI": BMI,
        "SmokerStatus": SmokerStatus,
        "GeneralHealth": GeneralHealth,
        "AgeCategory": AgeCategory,
        // "Race"
        
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
