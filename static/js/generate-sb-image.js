document.getElementById('download-button').addEventListener('click', function() {
    // Select the pitch element
    const pitch = document.getElementById('pitch');

    // Use html2canvas to take a screenshot of the pitch element
    html2canvas(pitch).then(canvas => {
        // Create a link element
        const link = document.createElement('a');

        // Set the download attribute with a filename
        link.download = 'squad_image.png';

        // Convert the canvas to a data URL and set it as the href attribute of the link
        link.href = canvas.toDataURL();

        // Append the link to the body (required for Firefox)
        document.body.appendChild(link);

        // Programmatically click the link to trigger the download
        link.click();

        // Remove the link from the document
        document.body.removeChild(link);
    });
});