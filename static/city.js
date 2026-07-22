// Get city name from URL
const params = new URLSearchParams(window.location.search);

const city = params.get("city");

// If no city is provided
if (!city) {

    window.location.href = "/";

}

// Fetch city details from Flask API
fetch(`/search?city=${encodeURIComponent(city)}`)

.then(response => response.json())

.then(data => {

    // City not found
    if (data.message) {

        alert(data.message);

        window.location.href = "/";

        return;

    }

    // Hero Image
    document.getElementById("heroImage").src =
        `/static/${data.heroImage}`;

    // City Name
    document.getElementById("cityName").innerText =
        data.city;

    // Description
    document.getElementById("description").innerText =
        data.description;

    // Hotel Price
    document.getElementById("hotelPrice").innerText =
        data.averageHotelPrice;

    // Vehicle Rent
    document.getElementById("bikeRent").innerText =
        data.vehicleRent.Bike;

    document.getElementById("scooterRent").innerText =
        data.vehicleRent.Scooter;

    document.getElementById("carRent").innerText =
        data.vehicleRent.Car;

    // Tourist Places
    const placesContainer =
        document.getElementById("placesContainer");

    data.places.forEach(place => {

        placesContainer.innerHTML +=
        `
        <div class="place-card">

            📍 ${place}

        </div>
        `;

    });

    // Foods
    const foodContainer =
        document.getElementById("foodContainer");

    data.popularFoods.forEach(food => {

        foodContainer.innerHTML +=
        `
        <div class="food-card">

            🍽 ${food}

        </div>
        `;

    });

})

.catch(error => {

    console.log(error);

    alert("Something went wrong!");

});