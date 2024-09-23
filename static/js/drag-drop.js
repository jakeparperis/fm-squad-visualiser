// The JavaScript in this project was generated by AI

document.addEventListener('DOMContentLoaded', () => {
    let draggedElement = null;
    let draggedPosition = null;
    let offsetX = 0;
    let offsetY = 0;

    function onPlayerInfoDragStart(event) {
    draggedElement = event.target;
    if (draggedElement.classList.contains('player-info')) {
        const playerName = draggedElement.childNodes[0].nodeValue.trim();
        const playerOvr = draggedElement.querySelector('.player-ovr').textContent.trim();

        const playerInfo = `${playerName} ${playerOvr}`;
        event.dataTransfer.setData('text/plain', playerInfo);
        draggedElement.style.opacity = '0.5';
        }
    }

    function onPlayerInfoDragEnd(event) {
        if (draggedElement) {
            draggedElement.style.opacity = '1';
            draggedElement = null;
        }
    }

    function onPositionDragStart(event) {
        draggedPosition = event.target;
        const rect = draggedPosition.getBoundingClientRect();
        offsetX = event.clientX - rect.left;
        offsetY = event.clientY - rect.top;
        event.dataTransfer.setData('text/plain', '');
        draggedPosition.style.opacity = '0.5';
    }

    function onPositionDragEnd(event) {
        if (draggedPosition) {
            draggedPosition.style.opacity = '1';
            draggedPosition = null;
        }
    }

    function onPositionDrag(event) {
        if (draggedPosition) {
            const pitchContainer = document.querySelector('.pitch-container');
            const rect = pitchContainer.getBoundingClientRect();
            const x = event.clientX - rect.left - offsetX;
            const y = event.clientY - rect.top - offsetY;

            draggedPosition.style.position = 'absolute';
            draggedPosition.style.left = `${x}px`;
            draggedPosition.style.top = `${y}px`;
        }
    }

    function onDragOver(event) {
        event.preventDefault();
    }

    function onDrop(event) {
        event.preventDefault();
        const position = event.target.closest('.position');
        if (position && draggedElement) {
            const playerHTML = event.dataTransfer.getData('text/plain');
            if (playerHTML) {
                position.innerHTML = playerHTML;
                position.style.color = '#fff';
            }
            draggedElement.style.opacity = '1';
        }
    }

    const draggablePlayerInfos = document.querySelectorAll('.player-info');
    draggablePlayerInfos.forEach(playerInfo => {
        playerInfo.setAttribute('draggable', 'true');
        playerInfo.addEventListener('dragstart', onPlayerInfoDragStart);
        playerInfo.addEventListener('dragend', onPlayerInfoDragEnd);
    });

    const positions = document.querySelectorAll('.position');
    positions.forEach(position => {
        position.setAttribute('draggable', 'true');
        position.addEventListener('dragstart', onPositionDragStart);
        position.addEventListener('dragend', onPositionDragEnd);
        position.addEventListener('drag', onPositionDrag);
    });

    const pitchContainer = document.querySelector('.pitch-container');
    pitchContainer.addEventListener('dragover', onDragOver);
    pitchContainer.addEventListener('drop', onDrop);
});
