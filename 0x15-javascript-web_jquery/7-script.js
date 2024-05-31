$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (fetcheddata){
    $('#character').text(fetcheddata.name)  
})
