$('.bg-img').scroll(function() {
    var x = $(this).scrollTop();
    $(this).css('background-position', '0% ' + parseInt(-x / 10) + 'px');
});