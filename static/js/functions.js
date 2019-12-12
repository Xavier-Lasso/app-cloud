function httpRequestMovieId(url) {
    $.ajax({
        url: url,
        type: "get",
        data: 'json',
        success: function(response) {
            $("#movieid").html(response);
        },
        error: function(e) {
            console.log(e);
        }
    });
}

function httpRequestEvents(url) {
    $.ajax({
        url: url,
        type: "get",
        data: 'json',
        success: function(response) {
            $("#events").html(response);
        },
        event: function(e) {
            console.log(e);
        }
    });
}

function httpRequestGraph(url, layout) {
    $.ajax({
        url: url,
        type: "get",
        data: 'json',
        success: function(response) {
            Plotly.newPlot('chart', response, layout, {responsive: true});
        },
        error: function(e) {
            console.log(e);
        }
    });
}

function changeMoviesById() {
    const movieId = document.getElementById('movieid').value;
    httpRequestErrors('/movies/' + movieId);
}

function changeEvents() {
    const select_number_events = document.getElementById('select-number-events');
    const selected_number_events = select_number_events.options[select_number_events.selectedIndex].value;
    const select_job_events = document.getElementById('select-job-events');
    const selected_job = select_job_events.options[select_job_events.selectedIndex].value;
    httpRequestEvents('/events/' + selected_job + '?q=' + selected_number_events);
}

function changeGraph() {
    const weekly = document.getElementById('radio-weekly');
    const select = document.getElementById('select-worker-graph');
    const selected_worker= select.options[select.selectedIndex].value;
    let layout;
    if(weekly.checked === true) {
        if(selected_worker === 'All workers') {
            layout = {'title': 'Weekly evolution of average execution time of jobs for all workers' ,'xaxis': {'title': 'Weeks'}, 'yaxis': {'title': 'Average execution time (in sec)'}};
            httpRequestGraph('/graphs/weekly', layout);
        }
        else {
            layout = {'title': 'Weekly evolution of average execution time of jobs for ' + selected_worker,'xaxis': {'title': 'Weeks'}, 'yaxis': {'title': 'Average execution time (in sec)'}};
            httpRequestGraph('/graphs/weekly/' + selected_worker, layout);
        }
    }
    else {
        if(selected_worker === 'All workers') {
            layout = {'title': 'Monthly evolution of average execution time of jobs for all workers' ,'xaxis': {'title': 'Months'}, 'yaxis': {'title': 'Average execution time (in sec)'}};
            httpRequestGraph('/graphs/monthly', layout);
        }
        else {
            layout = {'title': 'Monthly evolution of average execution time of jobs for ' + selected_worker,'xaxis': {'title': 'Months'}, 'yaxis': {'title': 'Average execution time (in sec)'}};
            httpRequestGraph('/graphs/monthly/' + selected_worker, layout);
        }
    }
}

window.onload = function() {
    changeErrors();
    changeEvents();
    changeGraph();
};