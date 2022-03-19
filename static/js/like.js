 $(document).ready(function () {
            
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