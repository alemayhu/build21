// Theme management
function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    updateThemeSelect(theme);
}

function updateThemeSelect(theme) {
    const select = document.getElementById('theme-select');
    if (select) {
        select.value = theme || 'auto';
    }
}

// Initialize theme on page load
function initTheme() {
    const savedTheme = localStorage.getItem('theme') || 'auto';
    setTheme(savedTheme);
}

// Make sure the theme is initialized both on load and when the script runs
initTheme();
document.addEventListener('DOMContentLoaded', initTheme);
