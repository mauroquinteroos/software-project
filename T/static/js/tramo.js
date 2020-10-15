const addmenu = (event) => {
  event.preventDefault()
  let menu=event.target.parentNode.querySelector('.mi-menu-tramo')
  menu.style.display = "block";
  menu.style.left =50+"%";
  menu.style.top = 25+"%";
};

const ocultarMenu = (menu) => {
  menu.style.display = "";
  menu.style.left = "";
  menu.style.top = "";
}

const salirmenu = (event) => {
  let menu=event.target.parentNode.querySelector('.mi-menu-tramo');
  if(menu == null) {
    let menu2 = event.target.parentNode.parentNode.parentNode.querySelector('.mi-menu-tramo')
    if(menu2 == null) {
      let menu3 = event.target.parentNode.parentNode.parentNode.parentNode.querySelector('.mi-menu-tramo')
      ocultarMenu(menu3)
    } else {
      ocultarMenu(menu2)
    }
  } else {
    ocultarMenu(menu)
  }
};
let container = document.querySelectorAll(".click-derecho");

container.forEach((element) => {
  element.addEventListener("contextmenu",addmenu);
  element.addEventListener("click",salirmenu);
});

let content = document.getElementById("content");
content.addEventListener("click", (event) => {
  if (event.target != container) {
    var elementos = document.querySelectorAll(".mi-menu-tramo");
   elementos.forEach((menu)=>{
     menu.style.display = "";
     menu.style.left = "";
     menu.style.top = "";
   })
  }
});
