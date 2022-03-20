 $(document).ready(function () {
            
    $(".social-share").jsSocials({ 
        showLabel: false,
        text: "Check out our landscape at viewforyou.tech",
        url: window.location.href,
        showCount: false,       
        shares: ["twitter", "facebook", "linkedin","whatsapp"]
    });

            $('.content').click(function () {

                const url = new URL(window.location.href)
                const slug = _.last(url.pathname.split('/').filter((path) =>!_.isEmpty(path)))
                const liked = $(".content").hasClass('heart-active') ? false: true;
                $.ajax({
                    url: `/landscape/${slug}/like`,
                    method: "PUT",
                    dataType: "json",
                    contentType : 'application/json',
                    data : JSON.stringify({
                        liked,
                    }),
                    error: (xhr, status, error) => {},
                    success: (data) => {
                        $('.content').toggleClass("heart-active")
                        $('.text').toggleClass("heart-active")
                        $('.numb').toggleClass("heart-active")
                        $('.heart').toggleClass("heart-active")
                      }
                  });
               
            });
        });