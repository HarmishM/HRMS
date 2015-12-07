


function load_personal_details() {
    // Helper function to restore details back to normal when clicked 'Cancel'

	function restore_personal()	{
		$('#personal-edit').show();
		$('#personal-edit-save, #personal-edit-cancel').hide();
		$('#firstname').val(fname); $('#middlename').val(mname); $('#lastname').val(lname);
		$('#licence-num').val(licenceNum); $('#drv-exp-picker').val(divingExpiry == 'None' ? ' Not Entered Yet' : divingExpiry);
		$('#marital-status').val(marStatus);
		if(gender === 'Male') {$('#marradio-male').prop('checked', true)};
		if(gender === 'Female') {$('#marradio-female').prop('checked', true)}
		$('#marital-status').prop('disabled', true);
		$('.selectpicker').selectpicker('refresh');

		$('#firstname, #middlename, #lastname, #licence-num, #drv-exp-picker').prop('disabled', true);
		$('#marradio-male, #marradio-female').prop('disabled', true);

	};
	
	$('#personal-edit').on('click', function(){
		$('#firstname, #middlename, #lastname, #licence-num, #drv-exp-picker').prop('disabled', false);
		$('#marradio-male, #marradio-female').prop('disabled', false);
		$('#marital-status').prop('disabled', false);
		$('#marital-status').selectpicker('refresh');

		$('#personal-edit').hide();
		$('#personal-edit-save').fadeIn(500);
		$('#personal-edit-cancel').fadeIn(500);
	});
	$('#personal-edit-cancel').on('click', function(){
		restore_personal();
	});
	return restore_personal();
};

function edit_and_save_personal_details(){

    $('#personal-edit-save').on('click', function(){
        $('#loading').show();
        var pathname = window.location.pathname;
        var intermediate = pathname.split('/hr/full-employee-info/')[1];
        var calling_empl_id = intermediate.slice('/')[0];
        var first_name = $('#firstname').val(); var middle_name = $('#middlename').val(); var last_name = $('#lastname').val();
        var drv_lcn_number = $('#licence-num').val(); var lsn_expiry = $('#drv-exp-picker').val();
        var mar_status = $('#marital-status option:selected').val();
        var gender = $('input[name=optradio]:checked').attr('value');

        $.ajax({
            type: 'POST',
            url: '/hr/api/ajax/personal/update/',
            data: {
                'empl_id': calling_empl_id, 'fname': first_name, 'mname': middle_name,
                'lname': last_name, 'drv_lcn_number': drv_lcn_number, 'lsn_expiry': lsn_expiry,
                'mar_status': mar_status, 'gender': gender,
            },
            success: function(data){
                fname = first_name; mname = middle_name; lname = last_name;
                licenceNum = drv_lcn_number; divingExpiry = lsn_expiry;
                marStatus = mar_status;
                load_personal_details();
                $('#loading').hide();
            },

        });

    });

}