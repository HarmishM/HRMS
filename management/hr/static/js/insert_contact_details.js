
function load_contacts_details(){

    function restore_contacts(){
        // load input controls with backend context variales and disable controls

        $('#curr-add-1').val(addr1); $('#curr-add-2').val(addr2); $('#curr-city').val(city);
        $('#curr-state').val(state); $('#curr-country').val(country); $('#curr-zip-code').val(zip);
        $('#curr-home-phone').val(homePhone); $('#curr-mobile').val(mobile); $('#pri-email').val(primEmail);

        $('#curr-add-1,#curr-add-2,#curr-country,#curr-state,#curr-city,#curr-zip-code').prop('disabled', true);
        $('#curr-home-phone,#curr-mobile,#pri-email').prop('disabled', true);
        $('#contact-edit-save,#contact-edit-cancel').fadeOut(400); $('#contact-edit').fadeIn(500);
    };

    $('#contact-edit').on('click', function(){
        $('#contact-edit').fadeOut(500); $('#contact-edit-save,#contact-edit-cancel').fadeIn(400);
        $('#curr-add-1,#curr-add-2,#curr-country,#curr-state,#curr-city,#curr-zip-code').prop('disabled', false);
        $('#curr-home-phone,#curr-mobile,#pri-email').prop('disabled', false);
    });

    $('#contact-edit-cancel').on('click', function(){
        restore_contacts();
    });
    return restore_contacts();
}

// load contries,states & cities from json response received from backend

function load_countries(){
    var jsonCountries = []; var jsonStates = []; var jsonCities = [];
  $.getJSON('/static/json/countries.json', function(data){
    $.each(data, function(key, value){
        jsonCountries.push(value);
    });
  });
  $.getJSON('/static/json/states.json', function(data){
    $.each(data, function(key, value){
        jsonStates.push(value);
    });
  });
  $.getJSON('/static/json/cities.json', function(data){
    $.each(data, function(key, value){
        jsonCities.push(value);
    });
  });
  $("#curr-country").typeahead({
    name: 'countries',
    source: jsonCountries,
   });
  $("#curr-state").typeahead({
    name: 'states',
    source: jsonStates,
   });
  $("#curr-city").typeahead({
    name: 'cities',
    source: jsonCities,
   });
};


function post_contact_info(){
 $('#contact-edit-save').on('click', function(){
    $('#loading').show();
    var empl_id = getEmployeeIdFromURL();
    var addLine1 = $('#curr-add-1').val(); var addLine2 = $('#curr-add-2').val();
    var addrCity = $('#curr-city').val(); var addrState = $('#curr-state').val(); var addrCountry = $('#curr-country').val();
    var addrZipCode = $('#curr-zip-code').val(); var homePhoneNumber = $('#curr-home-phone').val(); var mobilePhone = $('#curr-mobile').val();
    var priEmailAddress = $('#pri-email').val();

    $.ajax({
        url: '/hr/api/ajax/contacts/update/',
        type: 'POST',
        data: {
            'empl_id': empl_id,
            'add_line1': addLine1, 'add_line2': addLine2,
            'city': addrCity, 'state': addrState, 'country': addrCountry,
            'zip': addrZipCode, 'home_phone': homePhoneNumber, 'mobile': mobilePhone,
            'pri_email': priEmailAddress
        },
        success: function(data){
            addr1 = addLine1; city = addLine2; city = addrCity;; state = addrState; coutry = addrCountry;
            zip = addrZipCode; homePhone = homePhoneNumber; mobile = mobilePhone; primEmail = priEmailAddress;
            $('#loading').hide();
            load_contacts_details();
        }

    });
  });
}