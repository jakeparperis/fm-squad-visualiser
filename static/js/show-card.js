document.addEventListener('DOMContentLoaded', function() {
    window.showCard = function(playerId) {
        if (!playerId) return;

        // Make an AJAX request to get player card HTML
        fetch(`/show_card?player_id=${playerId}`)
            .then(response => response.text())
            .then(html => {
                // Update modal content and show modal
                document.getElementById('playerCardModal').innerHTML = html;
                document.getElementById('playerCardModal').style.display = 'block';
            })
            .catch(error => console.error('Error fetching player card:', error));
    };

    // Optionally, add event listener to close modal when clicking outside of it
    document.addEventListener('click', function(event) {
        if (event.target.id === 'playerCardModal') {
            event.target.style.display = 'none';
        }
    });
});