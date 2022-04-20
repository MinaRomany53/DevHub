try {
  const alertCloseBtns = document.querySelectorAll(".alert__close");

  alertCloseBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.target.closest(".alert").style.display = "none";
    });
  });
} catch (err) {
  console.log(err);
}
