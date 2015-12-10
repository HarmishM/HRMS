
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
                trButoonValue = selectedSupervisorId + supervisionType;
                var tr = '<tr><td> '+selectedSupervisor+'</td><td>'+supervisionType+'</td><td><button type="button" class="btn btn-danger" name="delete-row" id='+trButoonValue+' value='+trButoonValue+'><span class="glyphicon glyphicon-remove"></span></button></td></tr>';
                $('#reporting-table tbody').append(tr);
            },
        });

    });

    $('body').on('click', 'button[name=delete-row]', function(){
        btn_value = $(this).attr('value');
        btn_id = $(this);
        $.ajax({
            url: '/hr/api/ajax/reporting/delete/',
            type: 'POST',
            data: {
                'empl_id': getEmployeeIdFromURL(),
                'comb_str': btn_value,
            },
            success: function(data){
                $(btn_id).closest('tr').remove();
            },
            error: function (err) {
                console.log(err);
            },
        });

        //
    });
}