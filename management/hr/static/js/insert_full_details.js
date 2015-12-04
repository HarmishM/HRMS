function load_personal_details() {
    // Helper function to restore details back to normal when clicked 'Cancel'

	function restore_personal()	{
		$('#personal-edit').show();
		$('#personal-edit-save, #personal-edit-cancel').hide();
		$('#firstname').val(fname);
		$('#middlename').val(mname);
		$('#lastname').val(lname);
		$('#licence-num').val(licenceNum);
		$('#drv-exp-picker').val(divingExpiry);

		$('#firstname, #middlename, #lastname, #licence-num, #drv-exp-picker').prop('disabled', true);
	};
	
	$('#personal-edit').on('click', function(){
		$('#firstname, #middlename, #lastname, #licence-num, #drv-exp-picker').prop('disabled', false);
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
        drv_lcn_number = $('#licence-num').val();
        lsn_expiry = $('#drv-exp-picker').val();
        mar_status = $('#marital-status option:selected').text();
        gender = $('input[name=optradio]:checked').attr('value');

        $.ajax({
            type: 'POST',
            url: 'api/ajax/personal/update/',
            data: {

            },

        });

    });

}