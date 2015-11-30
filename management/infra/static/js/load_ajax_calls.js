function load_monitors() {
	
	$.ajax({ 
		type: 'GET',
		url: '/infra/monitors/',
		success: function(data) { 
			//console.log(data);
			$.each(data, function(key, value) {
				var entity = key;
				switch(entity){
					case 'monitor_brand':
					$.each(value, function(index, val) {
						$('#mon_brand').append('<option value=' + val + '>' + val + '</option>');
					});
					break;
					case 'monitor_size':
					$.each(value, function(index, val) {
						$('#mon_size').append('<option value=' + val + '>' + val + '</option>')
					});
					break;
					case 'monitor_type':
					$.each(value, function(index, val) {
						$('#mon_type').append('<option value=' + val + '>' + val + '</option>')
					});
					break;
				}

			});
		$('.selectpicker').selectpicker('refresh');
		}
	});

$('#monitor_check').click(function() {
	$.ajax({
		type: 'POST',
		url: '/infra/monitors-count/',
		data: {
			'mon_brand': $('select[id=mon_brand]').val(),
			'mon_size': $('select[id=mon_size]').val(),
			'mon_type': $('select[id=mon_type]').val(),
		},
		success: function(data) {
			if($('#monitor_check').has('#mon_cnt')) {
				$('#mon_cnt').remove();
			}
			$('#monitor_check').append('<span class="badge" id="mon_cnt">' + data +'<span>');
		},
	});
});

}

