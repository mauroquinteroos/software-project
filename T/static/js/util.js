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
const addmenu = (event) => {
  event.preventDefault();
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

// Crear elementos con atributos e hijo
const createCustomElement = (element, attributes, children) => {
  let customElement = document.createElement(element);
  if (children !== undefined)
    children.forEach((el) => {
      if (el.nodeType) {
        if (el.nodeType === 1 || el.nodeType === 11)
          customElement.appendChild(el);
      } else {
        customElement.innerHTML += el;
      }
    });
  addAttributes(customElement, attributes);
  return customElement;
};
// Añadir un objeto de atributos a un elemento
const addAttributes = (element, attrObj) => {
  for (let attr in attrObj) {
    if (attrObj.hasOwnProperty(attr)) element.setAttribute(attr, attrObj[attr]);
  }
};
// const imprimir modal
const printmodal = (content) => {
  const modalcontentEl = createCustomElement(
    "div",
    {
      id: "modal-content",
      class: "modal-content",
    },
    [content]
  );

  const modalContainerEl = createCustomElement(
    "div",
    {
      id: "modal-container",
      class: "modal-container",
    },
    [modalcontentEl]
  );
  //imprimir
  document.body.appendChild(modalContainerEl);

  //FUNCION DE QUITAR

  const removemodal = () => document.body.removeChild(modalContainerEl);

  modalContainerEl.addEventListener("click", (e) => {
    console.log(e.target);
    if (e.target === modalContainerEl) removemodal();
  });
};
//imgresar ruta
let ingresar = document.getElementById("ingresar");
ingresar.addEventListener("click", () => {
  printmodal(`
<div class="tab-pane fade show active " id="home" role="tabpanel" aria-labelledby="home-tab">
              <form class="formulario" id="formulario">
                <div class="row tab-item">
                  <div class="col-2 pad">
                    <label>Cod.Ruta:</label>
                    <input class="input" type="text" style="width:40px; " disabled="true" value="001"/>
                  </div>
                  <div class="col-3 pad">
                    <label>Cod.Ruta Py:</label>
                    <input class="input" type="text" style="width: 100px; "  value="AN-112"/>
                  </div>
                  <div class="col-4">
                    <label>Fecha:</label>
                    <input class="input" type="date"/>
                  </div>
                  <div class="col-3">
                    <label>Estado:</label>
                    <select style="width: 100px;">
                      <option>Vigente</option>
                      <option>Vigentea</option>
                      <option>Vigenteb</option>
                      <option>Vigentec</option>
                      <option>Vigented</option>
                    </select>
                  </div>
                </div>
                <div class="row tab-item">
                  <div class="col">
                    <label>Denominación Ruta:</label>
                    <textarea class="form-control" rows="4"></textarea>
                  </div>
                </div>
                <div class="row tab-item">
                  <div class="col-6 pad">
                    <label>Den. conto:</label>
                    <input class="input" type="text" style="width: 300px; "  value="Emp. PE 16 hasta Emp. PE 16 A (Dv.Rinconada)"/>
                  </div>
                  <div class="col-3 pad">
                    <label>Zona GPS:</label>
                    <select style="width: 80px; ">
                      <option>18</option>
                      <option>19</option>
                      <option>20</option>
                      <option>21</option>
                      <option>22</option>
                    </select>
                  </div>
                  <div class="col-3 pad">
                    <label>Long:</label>
                    <input class="input" type="text" style="width: 65px; " disabled="true" value="128.000"/>
                    <label>Kms.</label>
                  </div>
                </div>
                <div class="row tab-item">
                  <div class="col-3">
                    <label>Prog Inicio:</label>
                    <input class="input" type="text" style="width:115px; "/>
                  </div>
                  <div class="col-3">
                    <label>Latitud Inicio:</label>
                    <input class="input" type="text" style="width:115px; "/>
                  </div>
                  <div class="col-3">
                    <label>Longitud.Inicio:</label>
                    <input class="input" type="text" style="width:115px; "/>
                  </div>
                  <div class="col-3">
                    <label>ALtitud Inicio:</label>
                    <input class="input" type="text" style="width:115px; "/>
                  </div>
                </div>
                <div class="row tab-item">
                  <div class="col-3">
                    <label>Prog Final:</label>
                    <input class="input" type="text" style="width:115px; "/>
                  </div>
                  <div class="col-3">
                    <label>Latitud Final:</label>
                    <input class="input" type="text" style="width:115px; "/>
                  </div>
                  <div class="col-3">
                    <label>Longitud.Final:</label>
                    <input class="input" type="text" style="width:115px; "/>
                  </div>
                  <div class="col-3">
                    <label>ALtitud Final:</label>
                    <input class="input" type="text" style="width:115px; "/>
                  </div>
                </div>
                <div class="row tab-item">
                  <div class="col">
                    <label>Observación:</label>
                    <textarea class="form-control" rows="4"></textarea>
                  </div>
                </div>
                <div class="row tab-item">
                  <div class="col">
                    <label>Elaborado por:</label>
                    <select style="width: 300px; ">
                      <option>Luis Soto Vargas</option>
                      <option>19</option>
                      <option>20</option>
                      <option>21</option>
                      <option>22</option>
                    </select>
                  </div>
                </div>
                <button type="submit" class="btn btn-primary">Aceptar</button>
                <button type="" class="btn btn-light">Cancelar</button>
              </form>
</div>  `);
});
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
