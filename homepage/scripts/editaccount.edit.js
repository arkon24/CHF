$(function (){

   $('#show_delete_dialog').on('click', function() {
       $.loadmodal({
           url:'/homepage/shoppingcart/',
           title: 'Are you sure you want to delete this account?',
           width: '600px',
       });
   });//click
});