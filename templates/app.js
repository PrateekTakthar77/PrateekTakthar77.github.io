const scrollbtn = document.querySelector("#scrollbtn");
let userTexts = document.getElementsByClassName('user-text');
let userpic = document.getElementsByClassName('user-pic');

function showmagic() {
    for (userPics of userpic) {
        userPics.classList.remove("active-pic");
    }
    for (usertext of userTexts) {
        usertext.classList.remove("active-text")
    }
    let i = Array.from(userpic).indexOf(event.target);
    userpic[i].classList.add("active-pic")
    userTexts[i].classList.add("active-text")
}

scrollbtn.addEventListener("click", function () {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
    });
});