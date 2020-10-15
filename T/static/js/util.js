
window.addEventListener('load',()=>{

  var menu = document.querySelectorAll(".mi-menu");
  console.log(menu);
  menu.forEach((element)=>{
  element.addEventListener("click",()=>{
    console.log(element);
  });
})
});

const addmenu = (event) => {
  event.preventDefault();
  let menu=event.target.parentNode.querySelector('.mi-menu')
  
  menu.style.display = "block";
  menu.style.left =50+"%";
  menu.style.top = 25+"%";


  
};

    const salirmenu = (event) => {
      event.preventDefault();
      let menu=event.target.parentNode.querySelector('.mi-menu')
      menu.style.display = "";
      menu.style.left = "";
      menu.style.top = "";
    
     };
    let container = document.querySelectorAll(".click-derecho");
    
    container.forEach((element) => {
     
      element.addEventListener("contextmenu",addmenu);
      element.addEventListener("click",salirmenu);
    
     
    });
let content = document.getElementById("content");
content.addEventListener("click", (event) => {
  if (event.target != container) {
    var elementos = document.querySelectorAll(".mi-menu");
   elementos.forEach((menu)=>{

     menu.style.display = "";
     menu.style.left = "";
     menu.style.top = "";
   })
  }
});
// let dato;
// var codigo;

async function getruta(codigo){
const response=await fetch(`http://127.0.0.1:8000/proyecto/api/ruta/${codigo}`);
const data=await response.json()
return data;
}


// //Eliminar ruta
// let eliminar = document.getElementById("delete");
// eliminar.addEventListener("click", () => {
//   printmodal(`
//      <div class="delete"> 

// <img src="/static/img/delete.png"   alt="img-delete">

//      <p>¿Estas seguro que deseas eliminar el registro?</p>
//          <button class="btn btn-danger" id="eliminar">Eliminar</button>

//     <button  class="btn btn-light" >Cancelar</button>
 
//     </div>  
//            `);

//   menu.style.display = "none";
// });
// let detalle=document.getElementById("detalle");
// detalle.addEventListener('click',async()=>{
//   const ruta=await getruta(codigo);
//   console.log(ruta);
// })
