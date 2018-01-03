
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

// $(document).ready(function(){
//     $("#add-task").validate({
//         rules: {
//             description: {
//                 maxlength : 200
//             }
//         },
//         messages: {
//             description : {
//                 maxlength : "Maximum description length is 200 characters"
//             }
//         },
//         submitHandler: function(form) {
//             form.submit();
//         }
//     });
// });