
$(()=> {

    $(".carousel-item:first-of-type").addClass('active')
    $(".cards-wrapper .card:first-of-type").removeClass('d-none')
    $(".cards-wrapper .card:first-of-type").removeClass('d-md-block')
    
    $("#search-button-search").on('click', () => {
        window.location.href = `/landscape?q=${$("#query").val()}`
    })

    $(window).on('resize', () => {
        carouselView()
        if ($(window).width() > 500) {
            carouselView()
        }
        else {
            location.reload()
        }
    })
    const carouselView = () => {
        if ($(window).width() > 500) {
            let count = 0;
            let slider_count = 0;
            let max_slider_count = 3;
            $(".visited .card").each((i,element) => {
                if(count % max_slider_count === 0) {
                    slider_count ++
                    if ($('.visited .carousel-item').length < slider_count) {
                        let carouselItem = $(
                            "<div class = 'carousel-item'></div>"
                        )
                        let cardWrapper = $(
                            "<div class = 'cards-wrapper'></div>"
                        )
                        carouselItem.append(cardWrapper)
                        $('.visited').append(carouselItem)
                    }
                }  
                $(".visited .carousel-item .cards-wrapper").eq(slider_count - 1).append(element);
                count ++
            });    
            console.log(slider_count)
            const length = $(".visited .carousel-item").length
            console.log(length)
            for (let i =  slider_count ;i <= length - 1 ;i++ ){
                $('.visited .carousel-item').eq(slider_count).remove();
            }
        }
    }
    carouselView()


    $(".rating").each((i,element) => {
        $(`#${element.id}`).starRating({
            initialRating: $(element).attr('value'),
            readOnly: true,
        })
    })

})