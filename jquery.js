$(document).ready(function () {
                $("div").on({
                    mouseenter: function () {
                        $(this).fadeTo("fast", 0.5);
                    },
                    mouseleave: function () {
                        $(this).fadeTo("fast", 1);
                    },
                    click: function () {
                        $(this).fadeTo("slow", 0);
                    }
                    
                });
            });
