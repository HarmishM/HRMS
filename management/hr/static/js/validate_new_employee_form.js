
function validateNewEmployeeForm() {

$.validator.addMethod(
    "australianDate",
    function(value, element) {
        return value.match(/^(0?[1-9]|1[0-2])[/.](0?[1-9]|[12][0-9]|3[0-1])[/.](19|20)?\d{2}$/);
    },
    '<h6><br/><div class="alert alert-danger" role="alert">Please enter a date in the format dd/mm/yyyy !</div></h6>'
);
	$('#newempform').validate({ 
		rules: {
			firstname: 'required',
			middlename: 'required',
			lastname: 'required',
			dob: 'required',

		},

		messages: {
			firstname: '<h6><br/><div class="alert alert-danger" role="alert">Employee must have Firstname !</div></h5>',
			middlename: '<h6><br/><div class="alert alert-danger" role="alert">Employee must have Middlename !</div></h6>',
			lastname: '<h6><br/><div class="alert alert-danger" role="alert">Employee must have Lastname !</div></h6>',
			dob: '<h6><br/><div class="alert alert-danger" role="alert">Date of Birth required !</div></h6>',
		},

	});
}

function fill_departments_designations() {
	$.ajax({ 
		type: 'GET',
		url: '/hr/api/ajax/departments/',
		success: function(data){
			//console.log(data);
			$.each(data, function(key, value){
				switch(key){
					case 'depts':
						$.each(value, function(k, v){ 
							$('#depts').append('<option value='+v+'>'+v+'</option>');
						});
						break;
					case 'desgs':
						$.each(value, function(k, v){ 
							$('#desg').append('<option value='+v+'>'+v+'</option>');
						});
						break;
				}

			$('.selectpicker').selectpicker('refresh');
			});
		},

	});

	$('#depts').change(function(){
		//alert($('#depts option:selected').text());

	$.ajax({ 
		type: 'POST',
		url: '/hr/api/ajax/departments/',
		data: {
			'department': $('#depts option:selected').text(),
		},
		success: function(data){
			//console.log(data);
			$('#desg').empty();
			$.each(data, function(key, value){
				$('#desg').append('<option value='+value+'>'+value+'</option>');
			});
			$('.selectpicker').selectpicker('refresh');
		},

	});

	});

}