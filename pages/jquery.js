---
---
$(document).ready(function() {
  $(".navbar").hover(function() {
    $(this).css("background-color", "white");
    $(this).css("opacity", "0.5");
    $(this).css("color", "black");
  }, function() {
    $(this).css("background-color", "transparent");
    $(this).css("opacity", "1");
    $(this).css("color", "white");
  });
});
