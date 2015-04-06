$(function (){

   $('#show_delete_dialog').on('click', function() {
       $.loadmodal({
           url:'/homepage/logoutform/',
           title: 'Are you sure you want to change your password?',
           width: '600px',
       });
   });//click
});
