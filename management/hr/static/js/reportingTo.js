
function postReporting_details(){
    $('#save-supervisor').on('click', function(){
        var selectedSupervisor = $('#supervisor-name').val();
        var indice = employeeNameList.indexOf(selectedSupervisor)
        console.log('Indice is: '+indice);
        var selectedSupervisorId = employeeIdList[indice];
        var supervisionType = $('#reporting-type').val();

        // Fire a post request to view for feed the data....

        $.ajax({
            url: '/hr/api/ajax/reporting/update/',
            type: 'POST',
            data: {
                'empl_id': getEmployeeIdFromURL(),
                'supervisor_empl_id': selectedSupervisorId,
                'report_type': supervisionType,
            },
            success: function(data){

            },
        });

    });

    $('[name=delete-row').on('click', function(){
        $(this).parents('tr').first().remove();
    });
}