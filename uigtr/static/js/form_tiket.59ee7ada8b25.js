$(document).ready(function() {
	// Wait for the DOM to be ready
	
	var total_price = 0;
	var calculate_ipa = function() {
		var lokasi = document.getElementById("lokasi-TO").value;
		var ticket_price = 30000;
		if (lokasi === "Pekanbaru") {
			ticket_price = 32000;
		}
	    total_price += document.getElementById("tiket-ipa").value * ticket_price;
	    show_total_price(total_price);
	}

	var calculate_ips = function() {
		var lokasi = document.getElementById("lokasi-TO").value;
		var ticket_price = 30000;
		if (lokasi === "Pekanbaru") {
			ticket_price = 32000;
		}
	    total_price += document.getElementById("tiket-ips").value * ticket_price;
	    show_total_price(total_price);
	}

	var show_total_price = function(amount) {
		$("#total-amount").append("<p>Total harga: " + amount + "</p>")
	}

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
						maxlength: 40
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
					required: "Field ini harus diisi",
					maxlength: "Maksimum 40 karakter",
					email: "Harap masukkan email",
					number: "Harap masukkan angka",
					min: "Tiket tidak boleh negatif"

					// user_name: {
					// 	required: "Field ini harus diisi",
					// 	maxlength: "Maksimum 40 karakter"
					// },
					// user_email: {
					// 	required: "Field ini harus diisi",
					// 	email: "Harap masukkan email"
					// },
					// user_school: {
					// 	required: "Field ini harus diisi",
					// 	maxlength: "Maksimum 40 karakter"
					// },
					// tiket_ipa : {
					// 	required: "Field ini harus diisi",
					// 	number: "Harap masukkan angka",
					// 	min: "Tiket tidak boleh negatif"
					// },
					// tiket_ips : {
					// 	required: "Field ini harus diisi",
					// 	number: "Harap masukkan angka",
					// 	min: "Tiket tidak boleh negatif"
					// }
			},
			submitHandler: function(form) {
				form.submit();
			}
		});
	});
});