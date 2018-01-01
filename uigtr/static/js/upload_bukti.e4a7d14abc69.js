$(document).ready(function() {
	$(function() {
		$("#form-upload").validate({
			errorElement: 'div',
			rules: {
				bukti-foto: {
					required: true,
				}
			},
			submitHandler: function(form) {
				form.submit();
			}
		});
	});
});