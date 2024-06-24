function toggleTheme() {
    const body = document.body;
    const currentTheme = body.getAttribute('data-theme');

    if (currentTheme === 'light') {
        body.setAttribute('data-theme', 'colour1');
    }
    else if (currentTheme === 'colour1') {
        body.setAttribute('data-theme', 'dark');
    }
    else if (currentTheme === 'dark') {
        body.setAttribute('data-theme', 'light')
    }

    localStorage.setItem('theme', body.getAttribute('data-theme'))
}

document.getElementById('theme-toggle-button').addEventListener('click', toggleTheme);

function applyStoredTheme() {
    const body = document.body;
    const storedTheme = localStorage.getItem('theme');

    if (storedTheme) {
        body.setAttribute('data-theme', storedTheme);
    }
}

applyStoredTheme();