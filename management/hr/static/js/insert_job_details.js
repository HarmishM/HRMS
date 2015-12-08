
function disable_job_detail(){

    function restore_job(){
        // assign varibles received from backend contect here.
        on_change($('#depts').val());
        alert($('#depts').val());
        // $('#depts').val(jobDesig);
        $('#desg').val(jobDesig); $('#emp-type').val(jobType);
        $('#join-date').val(joinDate); $('#job-location').val(jobLoc);

        // $("#depts option:contains(" + jobDepartment + ")").attr('selected', 'selected');
        on_change($('#depts').val());

        // disable control here while freshly loaded, hide ``save`` and ``cancel`` buttons too...
        $('#job-edit').show();
        $('#job-edit-save').hide(); $('#job-edit-cancel').hide();
        $('#depts').prop('disabled', true); $('#desg').prop('disabled', true); $('#emp-type').prop('disabled', true);
        $('#join-date').prop('disabled', true); $('#job-location').prop('disabled', true);
        $('.selectpicker').selectpicker('refresh');

    };

    $('#job-edit').on('click', function(){
        $('#job-edit').hide();
        $('#job-edit-save').show(); $('#job-edit-cancel').show();

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
					    if ($('#depst').val() == 'Engineering-Dev')
						    {
						        $.each(value, function(k, v){
							        $('#desg').append('<option value='+v+'>'+v+'</option>');
						        });
						    }
						break;
				}
			$('.selectpicker').selectpicker('refresh');
			});
		},
	});

	$('#depts').change(function(){
		//alert($('#depts option:selected').text());
        on_change()
	});
};

function on_change(element){
    if (typeof(element)==='undefined') element = $('#depts').val();
	    $.ajax({
		    type: 'POST',
		    url: '/hr/api/ajax/departments/',
		    data: {
			    'department': element,
		    },
		    success: function(data){
			    //console.log(data);
			    $('#desg').find('option:gt(0)').remove();
			    $.each(data, function(key, value){
				    $('#desg').append('<option value='+value+'>'+value+'</option>');
			    });
			$('.selectpicker').selectpicker('refresh');
		    },
	    });

};

function post_job_info(){

    $('#job-edit-save').on('click', function(){

        $('#loading').show();
        var employeeID = getEmployeeIdFromURL();
        var dep = $('#depts option:selected').text(); var desg = $('#desg option:selected').text(); var emType=$('#emp-type option:selected').text();
        var joinD = $('#join-date').text(); var jobLocation = $('#job-location option:selected').text();
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
                disable_job_detail();
            },
        });
    });
}