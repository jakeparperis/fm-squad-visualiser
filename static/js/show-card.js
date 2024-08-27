document.addEventListener('DOMContentLoaded', function() {
    window.showCard = function(playerId) {
        if (!playerId) return;

        const modal = document.getElementById('playerCardModal');

        // If the modal is already displayed (i.e., another card is being shown), fade it out first
        if (modal.style.display === 'block' && modal.style.opacity === '1') {
            modal.style.opacity = '0';  // Start fading out

            // Wait for the fade-out transition to complete before changing content
            setTimeout(() => {
                fetchAndDisplayCard(playerId);  // Fetch and show the new card after fade-out
            }, 500);  // Match the duration of the fade-out (500ms)
        } else {
            fetchAndDisplayCard(playerId);  // If not already displayed, fetch and show immediately
        }
    };

    function fetchAndDisplayCard(playerId) {
        fetch(`/show_card?player_id=${playerId}`)
            .then(response => response.text())
            .then(html => {
                const modal = document.getElementById('playerCardModal');
                modal.innerHTML = html;

                // Show the modal and trigger the fade-in effect
                modal.style.display = 'block';
                setTimeout(() => {
                    modal.style.opacity = '1';  // Fade-in after content is loaded
                }, 10);  // Slight delay to ensure the display is applied before the transition
            })
            .catch(error => console.error('Error fetching player card:', error));
    }

    // Optionally, add event listener to close modal when clicking outside of it
    document.addEventListener('click', function(event) {
        const modal = document.getElementById('playerCardModal');
        if (modal.style.display === 'block' && !modal.contains(event.target)) {
            modal.style.opacity = '0';  // Fade out
            setTimeout(() => {
                modal.style.display = 'none';
            }, 500);  // Match the transition duration
        }
    });
});
