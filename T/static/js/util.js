var toggler = document.getElementsByClassName("caret");
var i;
var menu = document.getElementById("mi-menu");
for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function () {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
}

let container = document.querySelectorAll(".click-derecho");
console.log(container);
let content = document.getElementById("content");
content.addEventListener("click", (event) => {
  if (event.target != container) {
    var menu = document.getElementById("mi-menu");
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

async function getruta(codigo){
const response=await fetch(`http://127.0.0.1:8000/proyecto/api/ruta/${codigo}`);
const data=await response.json()
return data;
}


//Eliminar ruta
let eliminar = document.getElementById("delete");
eliminar.addEventListener("click", () => {
  printmodal(`
     <div class="delete"> 

<img src="/static/img/delete.png"   alt="img-delete">

     <p>¿Estas seguro que deseas eliminar el registro?</p>
         <button class="btn btn-danger" id="eliminar">Eliminar</button>

    <button  class="btn btn-light" >Cancelar</button>
 
    </div>  
           `);

  menu.style.display = "none";
});
let detalle=document.getElementById("detalle");
detalle.addEventListener('click',async()=>{
  const ruta=await getruta(codigo);
  console.log(ruta);
})
