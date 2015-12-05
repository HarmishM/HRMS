/* helper function, check to see if value is not one of following
   [], "", undefined, null
*/

function isEmpty(value){
  return (value == null || value.length === 0);
}