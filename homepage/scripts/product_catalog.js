$(function (){

   $('.add_button').on('click', function() {
    console.log($(this));

       var pid = $(this).attr('data-pid');
       var id =$(this).id;
       var qty =$("#qty"+pid).val();

       $.loadmodal({
           url:'/homepage/shoppingcart.add/' + pid + "/" + qty,
           title: 'Shopping Cart',
           width: '600px',

       });

   });//click
});

