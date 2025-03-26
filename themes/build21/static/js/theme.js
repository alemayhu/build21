// Theme management
function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
}

function toggleTheme() {
    const currentTheme = localStorage.getItem('theme') || 'auto';
    const themes = ['auto', 'light', 'dark'];
    const nextTheme = themes[(themes.indexOf(currentTheme) + 1) % themes.length];
    setTheme(nextTheme);
    updateThemeIcon(nextTheme);
}

function updateThemeIcon(theme) {
    const button = document.getElementById('theme-toggle');
    if (!button) return;
    
    // Update aria-label based on next theme
    const labels = {
        'auto': 'Use light theme',
        'light': 'Use dark theme',
        'dark': 'Use system theme'
    };
    button.setAttribute('aria-label', labels[theme]);
    
    // Update the icon text
    const icons = {
        'auto': '⚙️',
        'light': '☀️',
        'dark': '🌙'
    };
    button.textContent = icons[theme];
}

// Initialize theme on page load
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'auto';
    setTheme(savedTheme);
    updateThemeIcon(savedTheme);
});
