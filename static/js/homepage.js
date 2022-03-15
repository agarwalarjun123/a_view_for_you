$(()=> {
    $("#search-button-search").on('click', () => {
        window.location.href = `/landscape?q=${$("#query").val()}`
    })
})