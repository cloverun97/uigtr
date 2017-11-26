$(window).on('load',function(){
	$('.loader').fadeOut();
	
	//Welcoming text
	var str= "Selamat Datang di Website UIGTR 2018!";
	var split = str.split("");
	var counter = 0;

	var SI = setInterval(function(){
		var h1 = $("#welcome");
		h1.append(split[counter]);
		counter++;
		if (counter==str.length) {
			clearInterval(SI)
			$('#cursor').addClass("blinking-cursor");
		}
	}, 120); 

});

$(document).ready(function() {
	//navbar scrolling 
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

	//smooth scroll
	$(".slide-section").click(function(e){
		var linkHref = $(this).attr('href');
		$("html, body").animate({
			scrollTop: $(linkHref).offset().top
		}, 700);
		e.preventDefault();
	});

});

