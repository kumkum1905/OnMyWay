// ==============================
// TAB SWITCHING
// ==============================

const tabs = document.querySelectorAll(".tab-btn");
const contents = document.querySelectorAll(".tab-content");

tabs.forEach(tab => {

    tab.addEventListener("click", () => {

        tabs.forEach(btn => btn.classList.remove("active"));
        contents.forEach(content => content.classList.remove("active"));

        tab.classList.add("active");

        document
            .getElementById(tab.dataset.tab)
            .classList.add("active");

    });

});

// ==============================
// DELETE CONFIRMATION
// ==============================

const deleteBtn = document.querySelector(".delete-btn");

if (deleteBtn) {

    deleteBtn.addEventListener("click", (e) => {

        const city = document
            .getElementById("updateCity")
            .value
            .trim();

        if (city === "") {

            alert("Please enter the city name.");

            e.preventDefault();

            return;

        }

        const confirmDelete = confirm(
            `Are you sure you want to delete "${city}"?`
        );

        if (!confirmDelete) {

            e.preventDefault();

        }

    });

}