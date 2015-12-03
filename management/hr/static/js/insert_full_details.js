function load_personal_details() {
	function restore_personal()	{
		$('#personal-edit').show();
		$('#personal-edit-save, #personal-edit-cancel').hide();
		$('#firstname').val(fname);
		$('#middlename').val(mname);
		$('#lastname').val(lname);
		$('#firstname, #middlename, #lastname').prop('disabled', true);
	};
	
	$('#personal-edit').on('click', function(){
		$('#firstname, #middlename, #lastname').prop('disabled', false);
		$('#personal-edit').hide();
		$('#personal-edit-save').fadeIn(500);
		$('#personal-edit-cancel').fadeIn(500);
	});
	$('#personal-edit-cancel').on('click', function(){
		restore_personal();
	});
	return restore_personal();
};