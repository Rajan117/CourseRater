$(document).ready(function(){

  $("#uniSearch").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".searchResults .uni").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      $(".searchResults .course").hide();
      $(".searchResults .dep").hide();
    });
  });

  $("#uniSearch").on("blur", function() {
    $(".searchResults .course").show();
    $(".searchResults .dep").show();
    $(".searchResults .uni").show();
  });

  $("#depSearch").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".searchResults .dep").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      $(".searchResults .course").hide();
      $(".searchResults .uni").hide();
    });
  });

  $("#depSearch").on("blur", function() {
    $(".searchResults .course").show();
    $(".searchResults .dep").show();
    $(".searchResults .uni").show();
  });

  $("#courseSearch").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".searchResults .course").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      $(".searchResults .dep").hide();
      $(".searchResults .uni").hide();
    });
  });

  $("#courseSearch").on("blur", function() {
    $(".searchResults .course").show();
    $(".searchResults .dep").show();
    $(".searchResults .uni").show();
  });

});
