$(()=> {
    search()
    $("#search-button-search").on('click',(e)=>{
        const filters = getFilters()
        e.preventDefault()
        search($("#query").val(),filters)
    })
})

const search = (q = '', filters = {}) => {
    $.ajax({
        url: "/landscape/search/",
        method: 'GET',
        data: {
            q,
            ...filters
        },
        dataType: 'json',
        error : (xhr,status,error) => {
        },
        success : (data) => {
            $(".search-results").empty()
            if (data?.data?.length === 0){
                $(".search-results").append('<center><span class = "no-result-label">No Results</span></center>')
            }
            data.data.forEach(landscape => {
                appendResult(landscape)
            });
            
        }
    })
}
const appendResult = (result) => {
    $(".search-results").append(`
    <div class = 'search-result-container'>
        <div class = 'search-result-container-image-container'>
            <img class = 'search-result-container-image' src = 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/80/1e/29/loch-katrine.jpg?w=2000&h=-1&s=1'/>
        </div>
        <div class = 'search-result-container-content'>
            <h4>${result.name}</h4>
            <div class="my-rating-${result.id}" style = 'display:inline; padding: 2px;'></div>
            <span style>${result?.review?.count} reviews</span>
            <div class='address'>${result.address}</div>
            <div class = 'search-result-container-content-description'>${result.description.length > 300 ? result.description.slice(0,300) + '...' : result.description }</div>
        </div>   
    </div>`)
    $(`.my-rating-${result.id}`).starRating({
        initialRating: result?.review?.average_rating,
        readOnly: true,

    });
}

const getFilters = () => {
    const activities = []
    const accessibilities = []
    let filters = {}
    $(".activities:checked").each(function() {
       activities.push($(this).val())
    })
    $(".accessibilities:checked").each(function() {
        accessibilities.push($(this).val())
     })
    filters = accessibilities.length > 0 ?{
        ...filters,
        accessibilities: accessibilities.join(',')
    } : filters
    filters = activities.length > 0 ?{
        ...filters,
        activities: activities.join(',')
    } : filters
    return filters

}