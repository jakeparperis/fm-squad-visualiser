// drag-drop.js

document.addEventListener('DOMContentLoaded', () => {
    let draggedElement = null;
    let draggedPosition = null;
    let offsetX = 0;
    let offsetY = 0;

    // Function to handle the drag start event for player info (name and overall rating)
    function onPlayerInfoDragStart(event) {
    draggedElement = event.target;
    if (draggedElement.classList.contains('player-info')) {
        const playerName = draggedElement.childNodes[0].nodeValue.trim(); // Get the player's name only
        const playerOvr = draggedElement.querySelector('.player-ovr').textContent.trim(); // Get the player's OVR

        const playerInfo = `${playerName} ${playerOvr}`; // Combine name and OVR
        event.dataTransfer.setData('text/plain', playerInfo); // Transfer player name and OVR
        draggedElement.style.opacity = '0.5'; // Visual feedback
        }
    }

    // Function to handle the drag end event for player info
    function onPlayerInfoDragEnd(event) {
        if (draggedElement) {
            draggedElement.style.opacity = '1'; // Restore opacity
            draggedElement = null; // Clear the dragged element
        }
    }

    // Function to handle the drag start event for positions
    function onPositionDragStart(event) {
        draggedPosition = event.target;
        const rect = draggedPosition.getBoundingClientRect();
        offsetX = event.clientX - rect.left;
        offsetY = event.clientY - rect.top;
        event.dataTransfer.setData('text/plain', ''); // Required for Firefox compatibility
        draggedPosition.style.opacity = '0.5'; // Visual feedback
    }

    // Function to handle the drag end event for positions
    function onPositionDragEnd(event) {
        if (draggedPosition) {
            draggedPosition.style.opacity = '1'; // Restore opacity
            draggedPosition = null; // Clear the dragged position
        }
    }

    // Function to handle the drag event for positions
    function onPositionDrag(event) {
        if (draggedPosition) {
            const pitchContainer = document.querySelector('.pitch-container');
            const rect = pitchContainer.getBoundingClientRect();
            const x = event.clientX - rect.left - offsetX;
            const y = event.clientY - rect.top - offsetY;

            draggedPosition.style.position = 'absolute'; // Ensure element is positioned absolutely
            draggedPosition.style.left = `${x}px`;
            draggedPosition.style.top = `${y}px`;
        }
    }

    // Function to handle the drag over event
    function onDragOver(event) {
        event.preventDefault(); // Necessary to allow dropping
    }

    // Function to handle the drop event for players
    function onDrop(event) {
        event.preventDefault();
        const position = event.target.closest('.position');
        if (position && draggedElement) {
            const playerHTML = event.dataTransfer.getData('text/plain');
            if (playerHTML) {
                position.innerHTML = playerHTML; // Display player details in the position
                position.style.color = '#fff'; // Ensure text color is readable
            }
            draggedElement.style.opacity = '1'; // Restore opacity
        }
    }

    // Attach event listeners to draggable player info elements
    const draggablePlayerInfos = document.querySelectorAll('.player-info');
    draggablePlayerInfos.forEach(playerInfo => {
        playerInfo.setAttribute('draggable', 'true'); // Make player info draggable
        playerInfo.addEventListener('dragstart', onPlayerInfoDragStart);
        playerInfo.addEventListener('dragend', onPlayerInfoDragEnd);
    });

    // Attach event listeners to draggable position elements
    const positions = document.querySelectorAll('.position');
    positions.forEach(position => {
        position.setAttribute('draggable', 'true'); // Make positions draggable
        position.addEventListener('dragstart', onPositionDragStart);
        position.addEventListener('dragend', onPositionDragEnd);
        position.addEventListener('drag', onPositionDrag); // Handle dragging in real-time
    });

    // Attach event listeners to the pitch for drop events
    const pitchContainer = document.querySelector('.pitch-container');
    pitchContainer.addEventListener('dragover', onDragOver);
    pitchContainer.addEventListener('drop', onDrop);
});
