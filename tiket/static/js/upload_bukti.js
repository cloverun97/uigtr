
$(document).ready(function() {
	$(function() {
		$("#form-upload").validate({
			errorElement: 'div',
			rules: {
				bukti_foto: {
					required: true,
					extension: "png|jpe?g|gif"
				}
			},
			submitHandler: function(form) {
				form.submit();
			}
		});
	});
});