$(document).ready(function() {
	// Wait for the DOM to be ready
$(function() {
		$("#form-tiket").validate({
			errorElement: 'div',
			rules: {
				user_name: {
					required: true,
					maxlength: 40
				},
				user_email: {
					required: true,
					email: true
				},
				user_school: {
					required: true,
				},
				tiket_ipa : {
					required: true,
					number: true,
					min: 0
				},
				tiket_ips : {
					required: true,
					number: true,
					min: 0
				}
			},
			messages: {
				user_name: {
					required: "Field ini harus diisi",
					maxlength: "Maksimum 40 karakter"
				},
				user_email: {
					required: "Field ini harus diisi",
					email: "Harap masukkan email"
				},
				user_school: {
					required: "Field ini harus diisi"
				},
				tiket_ipa : {
					required: "Field ini harus diisi",
					number: "Harap masukkan angka",
					min: "Tiket tidak boleh negatif"
				},
				tiket_ips : {
					required: "Field ini harus diisi",
					number: "Harap masukkan angka",
					min: "Tiket tidak boleh negatif"
				}
		},
		submitHandler: function(form) {
			form.submit();
		}
	});
});
});