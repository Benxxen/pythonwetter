/**
 * Created by McDaemon on 05.11.14.
 */

// <![CDATA[
function showHide() {
    var ele = document.getElementById("vorschau");
    var ele2 = document.getElementById("aktuell");
    var ele3 = document.getElementById("container");
    if(ele.style.display == "block") {
            ele.style.display = "none";
            ele2.style.display = "block";
            ele3.style.display = "none";
      }
    else {
        ele.style.display = "block";
        ele2.style.display = "none";
        ele3.style.display = "none";
    }
}
function showLogin(){
    var ele= document.getElementById("container");
    var ele2= document.getElementById("vorschau");
    var ele3= document.getElementById("aktuell");
    if(ele.style.display== "block") {
        ele.style.display="none";
        ele2.style.display="none";
        ele3.style.display="block";
    }
    else {
        ele.style.display="block";
        ele2.style.display="none";
        ele3.style.display="none";
    }
}
function logout(){
    window.location.href="/accounts/logout";
    return false;
    }
function register(){
    window.location.href="/accounts/signup"
}
// ]]>
