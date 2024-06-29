document.addEventListener('DOMContentLoaded', (event) => {
    const themeToggle = document.getElementById('theme-toggle');
    const menuToggle = document.getElementById('menu-toggle');
    const navMenu = document.getElementById('nav-menu');
    const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        themeToggle.innerHTML = theme === 'dark' ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
    }

    // Check for saved theme preference or use the system preference
    const currentTheme = localStorage.getItem('theme') || (prefersDarkScheme.matches ? 'dark' : 'light');
    setTheme(currentTheme);

    themeToggle.addEventListener('click', () => {
        const switchToTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        setTheme(switchToTheme);
    });

    // Toggle mobile menu
    menuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('show');
    });

    // Close mobile menu when a link is clicked
    navMenu.addEventListener('click', (event) => {
        if (event.target.tagName === 'A') {
            navMenu.classList.remove('show');
        }
    });

    // Add fade-in effect to all main content
    const mainContent = document.querySelector('main');
    mainContent.classList.add('fade-in');
});
