$(document).ready(function() {
	$(function() {
		$("#form-upload").validate({
			errorElement: 'div',
			rules: {
				bukti_foto: {
					required: true,
				}
			},
			submitHandler: function(form) {
				form.submit();
			}
		});
	});
});