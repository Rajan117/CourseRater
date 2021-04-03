$(document).ready(function() {
  $('.likeButton').on('click', function() {
    //  If the like button hasn't already been pressed
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

  $('.dislikeButton').on('click', function() {
    //  If the dislike button hasn't already been pressed
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
