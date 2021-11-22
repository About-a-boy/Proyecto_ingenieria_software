const playButton = document.getElementById("play")
const musicContainer = document.getElementById("music-container")
const audio = document.getElementById("audio")
const progress = document.getElementById("progress")
const progressContainer = document.getElementById("progress-container")

function playSong() {
    musicContainer.classList.add("play")
    playButton.querySelector("i.fas").classList.remove("fa-play")
    playButton.querySelector("i.fas").classList.add("fa-pause")

    setTimeout(() => {
        audio.play()
    }, 500)
}

function pauseSong() {
    musicContainer.classList.remove("play")
    playButton.querySelector("i.fas").classList.remove("fa-pause")
    playButton.querySelector("i.fas").classList.add("fa-play")
    
    setTimeout(() => {
        audio.pause()
    }, 500)
}

function updateProggress(e) {
    const { duration, currentTime } = e.srcElement;
    const progressPercent = (currentTime / duration) * 100
    progress.style.width = `${progressPercent}%`
}

function setProgress(e) {
    const width = this.clientWidth;
    const clickX = e.offsetX;
    const duration = audio.duration;

    audio.currentTime = `${(clickX / width) * duration}`;
}

playButton.addEventListener("click", () => {
    const isPlaying = musicContainer.classList.contains("play")

    if (isPlaying) {
        pauseSong()
    } else {
        playSong()
    }
});

audio.addEventListener("timeupdate", updateProggress)
progressContainer.addEventListener("click", setProgress)