
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
}
