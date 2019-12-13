function httpRequestMovieId(url) {
    $.ajax({
        url: url,
        type: "get",
        data: 'json',
        success: function(response) {
            $("#s1").html(response);
        },
        error: function(e) {
            console.log(e);
        }
    });
}

function httpRequestMovieYear(url) {
    $.ajax({
        url: url,
        type: "get",
        data: 'json',
        success: function(response) {
            $("#s2").html(response);
        },
        event: function(e) {
            console.log(e);
        }
    });
}

function httpRequestGenreId(url) {
    $.ajax({
        url: url,
        type: "get",
        data: 'json',
        success: function(response) {
            $("#c2").html(response);
        },
        error: function(e) {
            console.log(e);
        }
    });
}

function changeMoviesById() {
    const movieId = document.getElementById('input-movieid') ? document.getElementById('input-movieid').value : null;
    if(movieId) {
        httpRequestMovieId('/user/movies/' + movieId);
    }
}

function changeYear() {
    const year = document.getElementById('input-year') ? document.getElementById('input-year').value : null;
    if(year) {
        httpRequestMovieYear('/user/movies/year/' + year);
    }
}

function changeSexe() {
    const userSex = document.getElementById('select-sexe') ? document.getElementById('select-sexe').value : null;
    const topNumber = document.getElementById('topNumber') ? document.getElementById('topNumber').value : null;
    if(userSex && topNumber) {
        httpRequestGenreId('/analyst/genre/' + userSex + '?q=' + topNumber);
    }
}

function changeTopNumber() {
    const userSex = document.getElementById('select-sexe') ? document.getElementById('select-sexe').value : null;
    const topNumber = document.getElementById('topNumber') ? document.getElementById('topNumber').value : null;
    if(userSex && topNumber) {
        httpRequestGenreId('/analyst/genre/' + userSex + '?q=' + topNumber);
    }
}

window.onload = function() {
    changeMoviesById();
    changeYear();
    changeSexe();
};
