$(document).ready( function() {
   $('.likes').click(function(){
    var comid;
    comid = $(this).attr("data-comid");
    $.get('/RateRestaurant/like_comment/', {comment_id: comid}, function(data){
               $('#like_count'+comid).html(data);
    });
});
});