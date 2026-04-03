let mode = document.getElementById("mode");
let body = document.body;


mode.addEventListener("click", () => {
  if (mode.innerText === "Darkmode") {
    body.style.background = "#171515";
    body.style.color = "#fff";
    mode.innerText = "lightmode";
  }
   else {
    body.style.background="#ffffff";
    body.style.color = "#1d1b1b";
    mode.innerText = "Darkmode";
  }
});
