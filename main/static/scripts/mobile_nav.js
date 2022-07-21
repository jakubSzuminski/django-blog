const nav_open_button = document.getElementById('show-menu');
const nav_close_button = document.getElementById('hide-menu');
const sidebar_menu = document.getElementById('sidebar-menu');

nav_open_button.addEventListener('click', () => {
    sidebar_menu.style.transform = "translateX(0)";
    nav_close_button.style.display = "block";
    nav_open_button.style.display = "none";    
});

nav_close_button.addEventListener('click', () => {
    sidebar_menu.style.transform = "translateX(100%)";
    nav_close_button.style.display = "none";
    nav_open_button.style.display = "block";
});

//Year in the footer
const year_element = document.getElementById("year");
year_element.textContent = new Date().getFullYear();
