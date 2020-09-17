var toggler = document.getElementsByClassName("caret");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
}

const $sidebar = document.querySelector('#sidebar')
const $sidebarBtn = document.querySelector('#sidebar-btn')
$sidebarBtn.addEventListener('click', () => {
  $sidebar.classList.toggle('hidden')
})
const $sidebarHeader = document.querySelector('#sidebar-header')
const $childsHeader = $sidebarHeader.querySelectorAll('#sidebar-header > *')
const $textSidebar = document.querySelectorAll('.sidebar--item-text')
$sidebarHeader.addEventListener("transitionstart", () => {
  if($sidebar.classList.contains('hidden')) {
    $childsHeader.forEach(item => item.style.visibility = 'hidden')
    $textSidebar.forEach(item => item.style.display = 'none')
  }
});
$sidebarHeader.addEventListener("transitionend", () => {
  if(!$sidebar.classList.contains('hidden')) {
    $childsHeader.forEach(item => item.style.visibility = 'visible')
    $textSidebar.forEach(item => item.style.display = 'inline-block')
  }
});