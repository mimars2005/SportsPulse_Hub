function tweets_activity(config = {
    "tweetLimit": 10,
}) {
    var container = document.getElementById('tweet-activity-chart');
    container.innerHTML = ''; // Clear previous chart content

    let activityChart; // Variable to store chart instance

    function onEvent(data) {
        // Chart data
        // Sample data for Tweet Activity (line chart)
        const tweetActivityData = {
            labels: ['16th of November','17th of November'], // X-axis labels
            datasets: [{
                label: 'Number of Tweets',
                data: [0,data.sixtienth,data.seventieth,0], // Data points
                borderColor: '#1da1f2',
                backgroundColor: 'rgba(29, 161, 242, 0.2)',
                fill: true,
            }]
        };

        // Tweet Activity Line Chart
        const tweetActivityCtx = document.getElementById('tweet-activity-chart').getContext('2d');

        // Destroy the previous chart if it exists
        if (activityChart) {
            activityChart.destroy();
        }

        activityChart=new Chart(tweetActivityCtx, {
            type: 'line',
            data: tweetActivityData,
            options: {
                animation:false,
                responsive: true,
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                    }
                },
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'Days'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Tweets'
                        },
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Return the onEvent function to be called with new data
    return onEvent;
}
