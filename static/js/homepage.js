$(() => {
  $(".carousel-item:first-of-type").addClass("active");
  $(".cards-wrapper .card:first-of-type").removeClass("d-none");
  $(".cards-wrapper .card:first-of-type").removeClass("d-md-block");

  $("#search-button-search").on("click", () => {
    window.location.href = `/landscape?q=${$("#query").val()}`;
  });
  $(".landscape").on("click", function () {
    window.location.href = "/landscape/" + $(this).attr("value");
  });

  $(window).on("resize", () => {
    if ($(window).width() > 500) {
      carouselView();
      locationCarouselView();
    } else {
      location.reload();
    }
  });
  const locationCarouselView = () => {
    if ($(window).width() > 500) {
      let count = 0;
      let slider_count = 0;
      let max_slider_count = 3;
      $(".location .card").each((i, element) => {
        if (count % max_slider_count === 0) {
          slider_count++;
          if ($(".location .carousel-item").length < slider_count) {
            let carouselItem = $("<div class = 'carousel-item'></div>");
            let cardWrapper = $("<div class = 'cards-wrapper'></div>");
            carouselItem.append(cardWrapper);
            $(".location").append(carouselItem);
          }
        }
        $(".location .carousel-item .cards-wrapper")
          .eq(slider_count - 1)
          .append(element);
        count++;
      });
      let length = $(".location .carousel-item").length;
      for (let i = slider_count; i <= length - 1; i++) {
        $(".location .carousel-item").eq(slider_count).remove();
      }
      length = $(".location .card").length;
      let incomplete_slide = Math.floor(length / max_slider_count);
      let counter = 0;
      for (let i = length % max_slider_count; i < 3; i++) {
        let card = $(".location .card").eq(counter).clone();
        $(".location .carousel-item .cards-wrapper")
          .eq(incomplete_slide)
          .append(card);
        counter++;
      }
      $(".landscape").on("click", function () {
        window.location.href = "/landscape/" + $(this).attr("value");
      });
    }
  };
  const carouselView = () => {
    if ($(window).width() > 500) {
      let count = 0;
      let slider_count = 0;
      let max_slider_count = 3;
      $(".visited .card").each((i, element) => {
        if (count % max_slider_count === 0) {
          slider_count++;
          if ($(".visited .carousel-item").length < slider_count) {
            let carouselItem = $("<div class = 'carousel-item'></div>");
            let cardWrapper = $("<div class = 'cards-wrapper'></div>");
            carouselItem.append(cardWrapper);
            $(".visited").append(carouselItem);
          }
        }
        $(".visited .carousel-item .cards-wrapper")
          .eq(slider_count - 1)
          .append(element);
        count++;
      });
      let length = $(".visited .carousel-item").length;
      for (let i = slider_count; i <= length - 1; i++) {
        $(".visited .carousel-item").eq(slider_count).remove();
      }
      length = $(".visited .card").length;
      let incomplete_slide = Math.floor(length / max_slider_count);
      let counter = 0;
      for (let i = length % max_slider_count; i < 3; i++) {
        let card = $(".visited .card").eq(counter).clone();
        $(".visited .carousel-item .cards-wrapper")
          .eq(incomplete_slide)
          .append(card);
        counter++;
      }
      $(".landscape").on("click", function () {
        window.location.href = "/landscape/" + $(this).attr("value");
      });
    }
  };
  carouselView();
  locationCarouselView();

  $(".rating").each((i, element) => {
    $(element).starRating({
      initialRating: $(element).attr("value"),
      readOnly: true,
    });
  });
  if (!Cookies.get("location")) {
    getLocation((location) => {
        Cookies.set("location", JSON.stringify(location), {
        expires: 1/48,
        path: "/",
        secure: true,
      });
    });
  }
});
const getLocation = (success, error) => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const location = {
          lat: position.coords.latitude,
          lon: position.coords.longitude,
        };
        success(location);
      },
      error,
      {
        enableHighAccuracy: false,
        timeout: 5000,
        maximumAge: Infinity,
      }
    );
  } else {
    error();
  }
};
