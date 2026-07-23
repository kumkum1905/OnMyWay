const music = document.getElementById("bgMusic");
const musicToggle = document.getElementById("musicToggle");

music.volume = 0.35;
music.loop = true;

let isPlaying = false;

musicToggle.addEventListener("click", async () => {

    if (isPlaying) {

        music.pause();

        musicToggle.classList.remove("playing");

        isPlaying = false;

    } else {

        try {

            await music.play();

            musicToggle.classList.add("playing");

            isPlaying = true;

        } catch (err) {

            console.error(err);

        }

    }

});