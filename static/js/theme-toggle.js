function toggleTheme() {
    const body = document.body;
    const currentTheme = body.getAttribute('data-theme');

    if (currentTheme === 'light') {
        body.setAttribute('data-theme', 'colour1');
    }
    else if (currentTheme === 'colour1') {
        body.setAttribute('data-theme', 'light');
    }
}

document.getElementById('theme-toggle-button').addEventListener('click', toggleTheme);
