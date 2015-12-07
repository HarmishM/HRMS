
function disable_job_detail(){

    function restore_personal(){
        // assign varibles received from backend contect here.


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
        restore_personal();
    });
    return restore_personal();

}