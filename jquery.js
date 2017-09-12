$(document).ready(function () {
    $(".squares div").on({
        mouseenter: function () {
            $(this).fadeTo("slow", 0.2);
        },
        mouseleave: function () {
            $(this).fadeTo("slow", 1);
        },
        click: function () {
            $(this).fadeTo("fast", 0);
        }
    });

    $("#pinkScheme").click(function () {
        $(".squares").removeClass("blue");
        $(".squares").addClass("pink");
    });

    $("#blueScheme").click(function () {
        $(".squares").removeClass("pink");
        $(".squares").addClass("blue");
    });

});
