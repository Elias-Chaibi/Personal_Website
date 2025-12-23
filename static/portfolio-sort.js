document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.projekte-container');
    const projects = [...container.querySelectorAll('.projekte')];

    projects.sort((a, b) => {
        const dateA = new Date(a.querySelectorAll('span')[1].textContent);
        const dateB = new Date(b.querySelectorAll('span')[1].textContent);
        return dateB - dateA; // neu → alt
    });

    projects.forEach(project => container.appendChild(project));
});