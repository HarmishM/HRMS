/* helper function, check to see if value is not one of following
   [], "", undefined, null
*/

function isEmpty(value){
  return (value == null || value.length === 0);
}

function getEmployeeIdFromURL(){
    var pathname = window.location.pathname;
    var intermediate = pathname.split('/hr/full-employee-info/')[1];
    var calling_empl_id = intermediate.slice('/')[0];
    return calling_empl_id
}