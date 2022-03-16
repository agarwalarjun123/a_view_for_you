jQuery(function($) {
    jQuery(document).ready(function(){  
       $('.slider').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        prevArrow: "<a class='carousel-control-prev' id='prev' role='button' data-slide='prev'><span class='carousel-control-prev-icon' aria-hidden='true'></span></a>",
        nextArrow: "<a class='carousel-control-next' id='next' role='button' data-slide='next'><span class='carousel-control-next-icon' aria-hidden='true'></span></a>",
    
        });
    }); 
});
