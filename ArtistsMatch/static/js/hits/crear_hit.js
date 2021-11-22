const uploadForm = document.getElementById("upload-form")
const progressBar = document.getElementById("progress-bar")
// for cover
const coverCancelBox = document.getElementById("cover-cancel-box")
const coverCancelButton = document.getElementById("cover-cancel-button")

// for song
const songCancelBox = document.getElementById("song-cancel-box")
const songCancelButton = document.getElementById("song-cancel-button")

const imageBox = document.getElementById("image-box")

const csrftoken = document.getElementsByName("csrfmiddlewaretoken")

const coverInput = document.getElementById("cover-input")
const songInput = document.getElementById("song-input")
const submitInput = document.getElementById("submit-form")

let hit = document.getElementById("hit")

let hitPk = null
let ajaxMethod = hitPk ? 'PATCH' : 'POST' 

coverInput.addEventListener('change', () => {
    progressBar.classList.remove("hidden")
    coverCancelBox.classList.remove("hidden")

    const coverData = coverInput.files[0]

    const formData = new FormData()
    const url = URL.createObjectURL(coverData)
    formData.append('csrfmiddlewaretoken', csrftoken[0].value)
    formData.append('cover', coverData)
    
    if (hitPk) {
        formData.append('hit', hitPk)
    }

    $.ajax({
        type: ajaxMethod,
        url: uploadForm.action,
        enctype: "multipart/form-data",
        data: formData,
        beforeSend: function () {
            imageBox.innerHTML = ""
        },
        xhr: toggleProgressBar(progressBar, uploadForm, coverCancelBox, coverCancelButton),
        success: function(response) {
            imageBox.innerHTML = `<img src="${url}" width="250px">`
            coverCancelBox.classList.add("hidden")
            hitPk = response.hit
            hit.value = hitPk
        },
        error: function(error) {
            console.error(error)
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})


songInput.addEventListener('change', () => {
    progressBar.classList.remove("hidden")
    songCancelBox.classList.remove("hidden")

    const songData = songInput.files[0]

    const formData = new FormData()
    formData.append('csrfmiddlewaretoken', csrftoken[0].value)
    formData.append('song', songData)

    if (hitPk) {
        formData.append('hit', hitPk)
    }

    $.ajax({
        type: 'POST',
        url: uploadForm.action,
        enctype: "multipart/form-data",
        data: formData,
        beforeSend: function () {
            // code
        },
        xhr: toggleProgressBar(progressBar, uploadForm, songCancelBox, songCancelButton),
        success: function(response) {
            songCancelBox.classList.add("hidden")
            hitPk = response.hit
            hit.value = hitPk
        },
        error: function(error) {
            console.error(error)
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})



// submitInput.addEventListener("click", e => {
//     e.preventDefault()
//     const title = document.getElementsByName("title")[0].value
//     const description = document.getElementsByName("description")[0].value

//     const formData = new FormData()
//     formData.append('csrfmiddlewaretoken', csrftoken[0].value)
//     formData.append('title', title)
//     formData.append('description', description)
//     formData.append('hit', hitPk)
    
//     $.ajax({
//         type: 'POST',
//         url: uploadForm.action,
//         enctype: "multipart/form-data",
//         data: formData,
//         success: response => {
//             console.log(response);
//             window.location = response.url
//         },
//         error: error => {
//             console.error(error);
//         },
//         cache: false,
//         contentType: false,
//         processData: false,
//     })
// })