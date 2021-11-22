const progressBox = document.getElementById("progress-box")
const cancelBox = document.getElementById("cancel-box")
const cancelButton = document.getElementById("cancel-button")
const uploadForm =  document.getElementById("form")
const submit = document.getElementById("submit")
const songInput = document.getElementById("song-input")
let collaboration = document.getElementById("collaboration")

const csrftoken = document.getElementsByName("csrfmiddlewaretoken")

songInput.addEventListener('change', () => {
    progressBox.classList.remove("hidden")
    cancelBox.classList.remove("hidden")

    const formData = new FormData()
    const songData = songInput.files[0]
    formData.append('csrfmiddlewaretoken', csrftoken[0].value)
    formData.append('song', songData)
    
    $.ajax({
        type: 'POST',
        enctype: "multipart/form-data",
        data: formData,
        url: uploadForm.action,
        beforeSend: function(){},
        xhr: toggleProgressBar(progressBox, uploadForm, cancelBox, cancelButton),
        success: response => {
            cancelBox.classList.add("hidden")
            collaboration.value = response.collaboration
        },
        error: error => {
            console.error(error);
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})