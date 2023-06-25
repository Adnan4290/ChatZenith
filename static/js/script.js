/*=============== SHOW MENU ===============*/
function show() {
    const navMenu = document.querySelector('.nav__menu');
    navMenu.classList.toggle('show-menu');
    
}

/*=============== REMOVE MENU MOBILE ===============*/
const navLink = document.querySelectorAll('.nav__link')

const linkAction = () => {
    const navMenu = document.getElementById('nav-menu')
    // When we click on each nav__link, we remove the show-menu class
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))
limitText('.chat__title', 20, 20);
limitText('.last__text', 30, 20);
// popup 
function popup() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
  }

  


