$(document).ready(function(){
	let oPeriods = JSON.parse(localStorage.getItem('periods'));
	$.each(oPeriods, function(i, value) {
		$('#periods').append('<li>' + value[0] + ' - ' + value[1] + '</li>');
	});
});

$(function() {
	$('#btnSubmit').click(function() {
		let oPeriods = [];
		let sForm = $("#formPeriod").serializeArray();
		
		if (localStorage.periods != null)
			oPeriods = JSON.parse(localStorage.getItem('periods'));
		
		oTemp = [];
		
		try {
			$.each(sForm, function(i, field) {
					//console.log(field.name + ':' + field.value);
					//oPeriods.push({[field.name]: field.value});
					d = new Date(field.value);
					if (isNaN(d)) {
						alert("Zły format daty.");
						oTemp = [];
						throw 'Break';
					} else {
						oTemp.push(d.toISOString().split('T')[0]);
					}
			});
		} catch(e){
			if (e !== 'Break') throw e;
		}
		
		if(oTemp.length > 0) {
			oPeriods.push(oTemp);
			// Put the object into storage
			localStorage.setItem('periods', JSON.stringify(oPeriods));
			
			$("#periods").append('<li>' + oTemp[0] + ' - ' + oTemp[1] + '</li>');
			
			$("#periodsContinous").empty();
		}
		
		// Retrieve the object from storage
		// var retrievedObject = localStorage.getItem('periods');
		//console.log('Periods: ', JSON.parse(retrievedObject));
		
		/*$.ajax({
				url: '/addPeriod',
				data: $('form').serialize(),
				type: 'POST',
				success: function(response) {
						<!-- console.log(response); -->
						oResponse = JSON.parse(response);
						$( "#periods" ).append('<li>' + oResponse.html + '</li>');
				},
				error: function(error) {
						console.log(error);
						alert('error');
				}
		});*/
	});
});

$(function() {
	$('#btnCount').click(function() {
		let data = {'data':localStorage.getItem('periods')};
		$.ajax({
			url: '/countPeriods',
			data: data,
			type: 'POST',
			success: function(response) {
				console.log(response);
				oResponse = JSON.parse(response);
				$("#periodsContinous").empty();
				$.each(oResponse.html, function(i, value) {
					$('#periodsContinous').append('<li>' + value[0] + ' - ' + value[1] + '</li>');
				});
			},
			error: function(error) {
				console.log(error);
				alert('error');
			}
		});
	});
});

$(function(){
	$('#btnClear').click(function(){
		$("#periods").empty();
		$("#periodsContinous").empty();
		localStorage.clear();
	});
});