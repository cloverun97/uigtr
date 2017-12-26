function initProgress(){
	var activeDist = $(".slide a.active").position();
	activeDist = activeDist.left;
	$(".after").stop().animate({width: activeDist + "px"});
}
initProgress();
$("a").click(function(e){
	e.preventDefault();
	$(".slide a").removeClass("active");
	$(this).addClass("active");
	initProgress();
});
$(window).resize(function(){
	initProgress();	
});