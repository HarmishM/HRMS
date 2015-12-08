
function on_change(element){
    //var element = $('#depts option:selected').text();
    if(typeof element === undefined) {
        alert('not defined');
    }
    // alert('element is: '+ element);
	    $.ajax({
		    type: 'POST',
		    url: '/hr/api/ajax/departments/',
		    data: {
			    'department': element,
		    },
		    success: function(data){
			    //console.log(data);
			    //$('#desg').find('option:gt(0)').remove();
			    // $('#desg').empty();
			    $('#desg').find('option:gt(0)').remove();
			    // alert('data is:'+ data);
			    $.each(data, function(key, value){
				    $('#desg').append('<option value='+value+'>'+value+'</option>');
			    });
			// $('#desg').prepend('<option value="None">Not Selected Yet</option>');
			$('#depts').val(jobDepartment);
			alert(jobType);
            $('#desg').val(jobDesig); $('#emp-type').val(jobType); $('#join-date').val(joinDate); $('#job-location').val(jobLoc);
			$('.selectpicker').selectpicker('refresh');
		    },
	    });

};

function on_change_new(element){
    //var element = $('#depts option:selected').text();
    if(typeof element === undefined) {
        alert('not defined');
    }
    // alert('element is: '+ element);
	    $.ajax({
		    type: 'POST',
		    url: '/hr/api/ajax/departments/',
		    data: {
			    'department': element,
		    },
		    success: function(data){
			    //console.log(data);
			    //$('#desg').find('option:gt(0)').remove();
			    // $('#desg').empty();
			    $('#desg').find('option:gt(0)').remove();
			    // alert('data is:'+ data);
			    $.each(data, function(key, value){
				    $('#desg').append('<option value='+value+'>'+value+'</option>');
			    });
			// $('#desg').prepend('<option value="None">Not Selected Yet</option>');
			$('.selectpicker').selectpicker('refresh');
		    },
	    });

};

function disable_job_detail(){

    function restore_job(){
        alert('caleeddd second');
        // assign varibles received from backend contect here.
        $('#job-edit').show(); $('#job-edit-save').hide(); $('#job-edit-cancel').hide();
        // alert(jobDepartment+' / '+jobDesig);
        // $('#depts').val(jobDepartment);
        //alert($('#depts').text());
        // $("#depts option:contains("+jobDepartment+")").attr('selected', 'selected');
        // $('#emp-type').val(jobType);

        $('.selectpicker').selectpicker('refresh');
        on_change(jobDepartment.toString());
		$('#depts, #desg').prop('disabled', true);

        // $("#depts option:contains(" + jobDepartment + ")").attr('selected', 'selected');

        // disable control here while freshly loaded, hide ``save`` and ``cancel`` buttons too...

        $('#depts').prop('disabled', true); $('#desg').prop('disabled', true); $('#emp-type').prop('disabled', true);
        $('#join-date').prop('disabled', true); $('#job-location').prop('disabled', true);

    };

    $('#job-edit').on('click', function(){
        $('#job-edit').hide();
        $('#job-edit-save').show(); $('#job-edit-cancel').show();
        alert('callllllleeeedddd');
        $('#depts').prop('disabled', false); $('#desg').prop('disabled', false); $('#emp-type').prop('disabled', false);
        $('#join-date').prop('disabled', false); $('#job-location').prop('disabled', false);
        $('.selectpicker').selectpicker('refresh');

    });

    $('#job-edit-cancel').on('click', function(){
        restore_job();
    });
    return restore_job();
};

function fill_departments_designations() {
    // alert('first caleedddddddddd');
    // $("#depts option:contains(" + jobDepartment + ")").attr('selected', 'selected');
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
			// alert($('#depts').text());
			});
		},
	});

	$('#depts').change(function(){
		var elementSelected = $('#depts option:selected').text();
        on_change_new(elementSelected);
	});
	disable_job_detail();
};


function post_job_info(){

    $('#job-edit-save').on('click', function(){

        $('#loading').show();
        var employeeID = getEmployeeIdFromURL();
        var dep = $('#depts option:selected').text(); var desg = $('#desg option:selected').text(); var emType=$('#emp-type option:selected').text();
        var joinD = $('#join-date').val(); var jobLocation = $('#job-location option:selected').text();
        // alert(joinD);
        $.ajax({
            url: '/hr/api/ajax/job/update/',
            type: 'POST',
            data: {
                'empl_id': employeeID,
                'dept': dep, 'desg': desg, 'emp_type': emType,
                'join_date': joinD, 'job_loc': jobLocation,
            },
            success: function(data){
                jobDepartment = dep; jobDesig = desg; jobType = emType;
                joinDate = joinD; jobLoc = jobLocation;
                $('#loading').hide();
                $('#job-edit').show(); $('#job-edit-save').hide(); $('#job-edit-cancel').hide();
                // $('#depts, #desg').prop('disabled', true);
                $('#depts').prop('disabled', true); $('#desg').prop('disabled', true); $('#emp-type').prop('disabled', true);
                $('#join-date').prop('disabled', true); $('#job-location').prop('disabled', true);
            },
        });
    });
}