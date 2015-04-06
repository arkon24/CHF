$(function () {

    $('#logoutform').ajaxForm(function(data) {
       $('#jquery-loadmodal-js-body').html(data);
    });

});