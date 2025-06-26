document.addEventListener("DOMContentLoaded", function () {
  const button = document.getElementById("clickMe");
  if (button) {
    button.addEventListener("click", () => {
      alert("Library portal button clicked!");
    });
  }
});
