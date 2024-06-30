function toggleTheme() {
    const body = document.body;
    const button = document.getElementById('theme-toggle-button')
    const currentTheme = body.getAttribute('data-theme');

    if (currentTheme === 'light') {
        body.setAttribute('data-theme', 'colour1');
        button.textContent = 'Theme 🔵';
    }
    else if (currentTheme === 'colour1') {
        body.setAttribute('data-theme', 'dark');
        button.textContent = 'Theme ⚫️';
    }
    else if (currentTheme === 'dark') {
        body.setAttribute('data-theme', 'light')
        button.textContent = 'Theme ⚪️';
    }

    localStorage.setItem('theme', body.getAttribute('data-theme'))
}

document.getElementById('theme-toggle-button').addEventListener('click', toggleTheme);

function applyStoredTheme() {
    const body = document.body;
    const button = document.getElementById('theme-toggle-button');
    const storedTheme = localStorage.getItem('theme');

    if (storedTheme) {
        body.setAttribute('data-theme', storedTheme);
        if (storedTheme === 'light') {
            button.textContent = 'Theme ⚪️';
        } else if (storedTheme === 'colour1') {
            button.textContent = 'Theme 🔵';
        } else if (storedTheme === 'dark') {
            button.textContent = 'Theme ⚫️';
        }
    }
}

applyStoredTheme();