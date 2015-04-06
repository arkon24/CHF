$(function (){

   $('#show_delete_dialog').on('click', function() {
       $.loadmodal({
           url:'/homepage/shoppingcart/',
           title: 'Are you sure you want to delete this account?',
           width: '600px',
       });
   });//click
});

$(function (){

   $('#show_logout_dialog').on('click', function() {
       $.loadmodal({
           url:'/homepage/logoutform/',
           title: 'Do you want to logout?',
           width: '600px',
       });
   });//click
});

$(function (){

   $('#show_cart_dialog').on('click', function() {
       $.loadmodal({
           url:'/homepage/shoppingcart/',
           title: 'Shopping Cart',
           width: '600px',
       });
   });//click
});

$(function (){

   $('#show_login_dialog').on('click', function() {
       $.loadmodal({
           url:'/homepage/index2.loginform/',
           title: 'Login Please',
           width: '600px',
       });
   });//click
});