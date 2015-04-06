$(function () {

    $('#loginform').ajaxForm(function(data) {
        $('#loginform_container').html(data);
        //console.log(data);
    }); //ajax form

});