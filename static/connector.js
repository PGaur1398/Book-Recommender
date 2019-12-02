window.onload = function(){
  setTimeout(addv, 8000)
};
var li = document.getElementsByTagName("article")

function addv(){
for(var i = 0;i<li.length;i++){
    li[i].addEventListener("click",function(){
    document.getElementById("img1").src = this.getElementsByTagName("img")[0].currentSrc;
    document.getElementsByTagName("textarea")[0].innerText = this.innerText  })}

}
