$(document).ready(function(){
	$.get("/navbar", function(data){
		$("#navbar_field").replaceWith(data);
	});
});
// <a href="http://apply-973.appspot.com/apply-pin.html" target="_blank">Apply Now</a> 