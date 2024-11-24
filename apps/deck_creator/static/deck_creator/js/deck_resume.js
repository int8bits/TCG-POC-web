$(document).ready(function() {
    console.log("ready!");

    $(".proffer-card").click(function() {
        console.log("click!");
        var card_id = $(this).attr("id");
        console.log(card_id);

        $("#div_id_id_k").hide();
        $("#id_id_k").prop("readonly", true);
        $("#id_id_k").val(card_id);
    });
});