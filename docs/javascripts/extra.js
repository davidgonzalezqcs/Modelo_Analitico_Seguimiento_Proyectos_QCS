document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.querySelector(".md-search__input");
  if (searchInput) {
    searchInput.setAttribute("placeholder", "Buscar...");
  }
});