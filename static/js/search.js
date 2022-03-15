$(() => {
  $("#query").val(q);

  const getFilters = () => {
    filters = {};
    const activities = [];
    const accessibilities = [];
    $(".activities:checked").each(function () {
      activities.push($(this).val());
    });
    $(".accessibilities:checked").each(function () {
      accessibilities.push($(this).val());
    });
    filters =
      accessibilities.length > 0
        ? {
            ...filters,
            accessibilities: accessibilities.join(","),
          }
        : filters;
    filters =
      activities.length > 0
        ? {
            ...filters,
            activities: activities.join(","),
          }
        : filters;
    getLocation(
      (location) => {
        localStorage.setItem("location", JSON.stringify(location));
        filters = {
          ... filters,
          ...location,
        };
        search($("#query").val(), filters);
      },
      () => {
        localStorage.removeItem("location");
        filters = _.omit(filters, ["lat", "lon"]);
        search($("#query").val(), filters);
      }
    );
    filters = localStorage.getItem("location")
      ? { ...JSON.parse(localStorage.getItem("location")), ...filters }
      : filters;
    return filters;
  };

  const getLocation = (success, error) => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        const location = {
          lat: position.coords.latitude,
          lon: position.coords.longitude,
        };
        success(location);
      }, error);
    }
    else {
      error()
    }
  };

  filters = getFilters();

  search(q, filters);
  $("#search-button-search").on("click", (e) => {
    e.preventDefault();
    filters = getFilters();
    search($("#query").val(), filters);
  });
});

const search = (query = "", filters = {}) => {
  $.ajax({
    url: "/landscape/search/",
    method: "GET",
    data: {
      q: query,
      ...filters,
    },
    dataType: "json",
    error: (xhr, status, error) => {},
    success: (data) => {
      $(".search-results").empty();
      if (data?.data?.length === 0) {
        $(".search-results").append(
          '<center><span class = "no-result-label">No Results</span></center>'
        );
      }
      data.data.forEach((landscape) => {
        appendResult(landscape);
      });
    },
  });
};

const appendResult = (result) => {
  $(".search-results").append(`
    <div class = 'search-result-container' id = '${result.slug}'>
        <div class = 'search-result-container-image-container'>
            <img class = 'search-result-container-image' src = '${
              result.image
            }'/>
        </div>
        <div class = 'search-result-container-content'>
            <h4>${result.name}</h4>
            <div class="my-rating-${
              result.id
            }" style = 'display:inline; padding: 2px;'></div>
            <span style>${result?.review?.count} reviews</span>
            <div class='address'>${result.address}</div>
            <div class = 'search-result-container-content-description'>${
              result.description.length > 300
                ? result.description.slice(0, 300) + "..."
                : result.description
            }</div>
        </div>   
    </div>`);
  $(`.my-rating-${result.id}`).starRating({
    initialRating: result?.review?.average_rating,
    readOnly: true,
  });
  $(`#${result.slug}`).on('click',(e) => {
    window.location.href = `/landscape/${result.slug}`
  })
  
};
