function sentiment_analysis(config = {
    "tweetLimit": 10,
}) {
    var container = document.getElementById('sentiment-analysis-chart');
    container.innerHTML = ''; // Clear previous chart content

    let sentimentChart; // Variable to store chart instance

    function onEvent(data) {
        // Chart data
        const sentimentAnalysisData = {
            labels: ['Positive', 'Neutral', 'Negative'], // Categories on X-axis
            datasets: [{
                label: 'Sentiment Count',
                data: [data.positive_tweets, data.neutral_tweets, data.negative_tweets], // Data points
                backgroundColor: ['#28a745', '#ffc107', '#dc3545'], // Colors for each bar
            }]
        };

        const sentimentAnalysisCtx = document.getElementById('sentiment-analysis-chart').getContext('2d');

        // Destroy the previous chart if it exists
        if (sentimentChart) {
            sentimentChart.destroy();
        }

        // Create a new chart instance
        sentimentChart = new Chart(sentimentAnalysisCtx, {
            type: 'bar',
            data: sentimentAnalysisData,
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
                            text: 'Sentiment'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Count'
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
