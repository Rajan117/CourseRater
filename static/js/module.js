$(document).ready(function() {

  $('.likeButton').on('click', function() {
    this.innerHTML="Liked";
    this.style.color = 'green';

    var reviewIdVar = $(this).attr('data-reviewid');

    $.get('/CourseRate/like_review/',
      {'review_id': reviewIdVar},
      function(data) {
        $('#like_count').html(data);
      });
  });

  $('.dislikeButton').on('click', function() {
    this.innerHTML="Disliked";
    this.style.color = 'red';

    var reviewIdVar = $(this).attr('data-reviewid');

    $.get('/CourseRate/dislike_review/',
      {'review_id': reviewIdVar},
      function(data) {
        $('#dislike_count').html(data);
      });
  });
});
