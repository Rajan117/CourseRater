$(document).ready(function() {
  // Show the number of reviews on the page
  var reviews = $('.reviewsList .review').length;
  var reviewsString = "&nbsp;&nbsp;&nbsp;&nbsp; Reviews: " + reviews.toString();
  $('#reviewsNumber').html(reviewsString);

  // Show the average rating (as percentage)
  if (reviews != 0){
    total = 0;
    var revRatings = document.getElementsByClassName('reviewRating');
    for (var i=0; i<reviews; i++){
      var ratingValue = parseInt(revRatings[i].innerHTML);
      total += ratingValue;
    }
    average = parseInt(total / reviews * 10);
    var averageCourseRating = "&nbsp;&nbsp;&nbsp;&nbsp; Average rating: " + average.toString() + "%";
    $('#ratingsAverage').html(averageCourseRating);
  }


  // Like button
  $('.likeButton').on('click', function() {
    // If the like button hasn't already been pressed
    if (this.style.color != "green"){
      this.style.color = 'green';
      var likes = this.innerHTML;
      var l = parseInt(likes);
      l = l + 1;
      likes = " " + l.toString();
      this.innerHTML = likes;
      var reviewIdVar = $(this).attr('data-reviewid');
      $.get('/CourseRate/like_review/',
      {'review_id': reviewIdVar},

      function(data) {
        $('#dislike_count').html(data);
      });
    }
  });

  // Dislike button
  $('.dislikeButton').on('click', function() {
    // If the dislike button hasn't already been pressed
    if (this.style.color != "red"){
      this.style.color = 'red';
      var dislikes = this.innerHTML;
      var dl = parseInt(dislikes);
      dl = dl + 1;
      dislikes = " " + dl.toString();
      this.innerHTML = dislikes;
      var reviewIdVar = $(this).attr('data-reviewid');
      $.get('/CourseRate/dislike_review/',
      {'review_id': reviewIdVar},

      function(data) {
        $('#dislike_count').html(data);
      });
    }
  });
});
