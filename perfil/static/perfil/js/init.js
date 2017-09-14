$(document).ready(function () {
    $('ul.tabs').tabs();


    $('.carousel').carousel();

     $('.carousel.carousel-slider').carousel({fullWidth: true});

    Materialize.scrollFire(options);

    $('.tap-target').tapTarget('open');
    $('.tap-target').tapTarget('close');

    Materialize.toast('I am a toast!', 4000) // 4000 is the duration of the toast


    var options = [ {selector: '#sala', offset: 0, callback: function(el) { Materialize.toast("This is our ScrollFire Demo!", 1500 ); } }, {selector: '#banheiro', offset: 205, callback: function(el) { Materialize.toast("Please continue scrolling!", 1500 ); } }, {selector: '#staggered-test', offset: 400, callback: function(el) { Materialize.showStaggeredList($(el)); } }, {selector: '#image-test', offset: 500, callback: function(el) { Materialize.fadeInImage($(el)); } } ]; Materialize.scrollFire(options);



});
