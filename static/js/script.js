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

/*=============== ADD BLUR TO HEADER ===============*/
const blurHeader = () => {
    const header = document.getElementById('header')
    // When the scroll is greater than 50 viewport height, add the blur-header class to the header tag
    this.scrollY >= 50 ? header.classList.add('blur-header')
        : header.classList.remove('blur-header')
}
window.addEventListener('scroll', blurHeader)
// ========================== LIMIT NUMBER OF CHARACTERS DISPLAYED ON CHATS PAGE ==========================
const limitText = (selector, defaultLimit, smallLimit) => {
    const elements = document.querySelectorAll(selector);
    elements.forEach(element => {
        let limit = defaultLimit;
      if (window.innerWidth < 350) {
        limit = smallLimit;
      }
      if (element.textContent.length > limit) {
        const truncated = element.textContent.substring(0, limit) + '...';
        element.textContent = truncated;
    }
    });
};

limitText('.chat__title', 20, 20);
limitText('.last__text', 30, 20);
// popup 
function popup() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
  }

  


