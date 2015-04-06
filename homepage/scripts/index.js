$(function () {

    $('#loginform').ajaxForm(function(data) {
        $('#loginform_container').html(data);
        //console.log(data);
    }); //ajax form

});


$(function () {

    $('#logoutform').ajaxForm(function(data) {
       $('#jquery-loadmodal-js-body').html(data);
    });

});