
var menu = document.getElementById("mi-menu-tramo");

let container = document.querySelectorAll(".click-derecho");
console.log(container);
let content = document.getElementById("content");
content.addEventListener("click", (event) => {
  if (event.target != container) {
    var menu = document.getElementById("mi-menu-tramo");
    menu.style.display = "";
    menu.style.left = "";
    menu.style.top = "";
  }
});
let dato;
var codigo;
const addmenu = async(event) => {
  event.preventDefault();
   codigo=parseInt(event.target.parentNode.dataset.id);
  
  menu.style.display = "block";
  menu.style.left = event.pageX + "px";
  menu.style.top = event.pageY + "px";
  console.log(event.target.parentNode);
  dato = event.target.parentNode;

 
};
const salirmenu = (event) => {
  menu.style.display = "";
  menu.style.left = "";
  menu.style.top = "";

};
container.forEach((element) => {
  element.addEventListener("contextmenu", addmenu);
  element.addEventListener("click", salirmenu);
});