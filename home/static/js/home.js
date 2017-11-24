$(window).on('load',function(){
     $('.loader').fadeOut();
});

$(document).ready(function() {
	$(window).scroll(function() {
	  	if($(document).scrollTop() > 10) {
	    	$('#my-nav').addClass('scroll-navbar');
	    }
	    else {
	    $('#my-nav').removeClass('scroll-navbar');
	    }
  	});

 //  	$("#list").on("mouseover", function() {
 //  		$(this).css( "color", "red" );
	// });
});

