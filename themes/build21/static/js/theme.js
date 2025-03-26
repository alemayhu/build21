// Theme management
function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    updateThemeIcon(theme);
}

function toggleTheme() {
    const currentTheme = localStorage.getItem('theme') || 'auto';
    const themes = ['auto', 'light', 'dark'];
    const nextTheme = themes[(themes.indexOf(currentTheme) + 1) % themes.length];
    setTheme(nextTheme);
}

function updateThemeIcon(theme) {
    const button = document.getElementById('theme-toggle');
    if (!button) return;
    
    // Update aria-label based on current theme
    const labels = {
        'auto': 'Using system theme (click for light)',
        'light': 'Using light theme (click for dark)',
        'dark': 'Using dark theme (click for system)'
    };
    button.setAttribute('aria-label', labels[theme] || labels['auto']);
    
    // Update the icon text
    const icons = {
        'auto': '⚙️',
        'light': '☀️',
        'dark': '🌙'
    };
    button.textContent = icons[theme] || icons['auto'];
}

// Initialize theme on page load
function initTheme() {
    const savedTheme = localStorage.getItem('theme') || 'auto';
    setTheme(savedTheme);
}

// Make sure the theme is initialized both on load and when the script runs
initTheme();
document.addEventListener('DOMContentLoaded', initTheme);
