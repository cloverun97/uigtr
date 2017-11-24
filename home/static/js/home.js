$(window).on('load',function(){
     $('.loader').fadeOut();
});

$(document).ready(function() {
	$(window).scroll(function() {
		var scroll = $(window).scrollTop();
	  	if(scroll > 1) {
	    	$('.my-navbar').css("background", "rgba(0, 0, 0, 0.5)");
	    	$('.my-navbar').css("transition","all 0.5s");
	    }
	    else {
	    $('.my-navbar').css("background", "none");
	    }
  	});
	console.log(scroll);
 //  	$("#list").on("mouseover", function() {
 //  		$(this).css( "color", "red" );
	// });
});

