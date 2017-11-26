$(window).on('load',function(){
	$('.loader').fadeOut();
	
	//Welcoming text
	var str= "Selamat Datang di Website UIGTR 2018!";
	var split = str.split("");
	var counter = 0;
	
	$(window).on("blur focus", function(e) {
		var prevType = $(this).data("prevType");

		if (prevType != e.type) { //reduce double fire issues
			switch (e.type) {
				case "blur":
					break;
				case "focus":
					break;
			}
		}

		$(this).data("prevType", e.type);
	});

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

	$(".slide-section").click(function(){
		alert("klik!");
	});

});

