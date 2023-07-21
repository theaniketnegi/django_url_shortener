function submitForm(e) {
  e.preventDefault();
  fetch("/shorten", {
    method: "POST",
    body: new URLSearchParams(new FormData(form)),
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  })
    .then((response) => response.text())
    .then((data) => (shortened.textContent = `http://${window.location.host}/${data}`))
    .catch((error) => console.error(error));
}

const form = document.getElementById("form");
const shortened = document.getElementById("shortened");
form.addEventListener("submit", submitForm);
