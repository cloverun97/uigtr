function calculate() {
	var total_price = 0;
	total_price = calculate_ipa(total_price);
	total_price = calculate_ips(total_price);
	var ipa = $("#tiket-ipa").val()
	var ips = $("#tiket-ips").val()
	if (ipa >= 0 && ips >= 0) {
		show_total_price(total_price);
	}
}

function calculate_ipa(total_price) {
	var lokasi = $("#lokasi-TO").val();
	var ticket_price = 30000;
	if (lokasi === "Pekanbaru") {
		ticket_price = 32000;
	}
	total_price += $("#tiket-ipa").val() * ticket_price;
	return total_price;
}

function calculate_ips(total_price) {
	var lokasi = $("#lokasi-TO").val();
	var ticket_price = 30000;
	if (lokasi === "Pekanbaru") {
		ticket_price = 32000;
	}
	total_price += $("#tiket-ips").val() * ticket_price;
	return total_price;
}

var show_total_price = function(amount) {
	$("#total-amount").html("<p>Total harga: Rp " + amount + "</p>")
}

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
			submitHandler: function(form) {
				form.submit();
			}
		});
	});
});