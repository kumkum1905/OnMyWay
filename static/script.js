const form = document.getElementById("placeForm");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const city = document.getElementById("cityInput").value.trim();

    if (city === "") return;

    window.location.href = `/city?city=${encodeURIComponent(city)}`;
});