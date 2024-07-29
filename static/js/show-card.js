document.addEventListener('DOMContentLoaded', function() {
    window.showCard = function(playerId) {
        if (!playerId) return;

        // Make an AJAX request to get player card HTML
        fetch(`/show_card?player_id=${playerId}`)
            .then(response => response.text())
            .then(html => {
                // Update modal content and show modal
                const modal = document.getElementById('playerCardModal');
                modal.innerHTML = html;
                modal.style.display = 'block';
            })
            .catch(error => console.error('Error fetching player card:', error));
    };

    // Optionally, add event listener to close modal when clicking outside of it
    document.addEventListener('click', function(event) {
        const modal = document.getElementById('playerCardModal');
    });
});