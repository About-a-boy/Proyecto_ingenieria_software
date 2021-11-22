function toggleProgressBar(progressBar, uploadForm, cancelBox, cancelButton) {
    return function (){
        const xhr = new XMLHttpRequest();
        xhr.upload.addEventListener('progress', function (e) {
            if (e.lengthComputable) {
                const percent = e.loaded / e.total * 100

                progressBar.innerHTML = `<div class="progress">
                                            <div
                                                class="progress-bar"
                                                role="progressbar"
                                                style="width: ${percent}%;background-color:white;text-align:center;"
                                                aria-valuenow="${percent}"aria-valuemin="0" aria-valuemax="100">
                                                ${percent.toFixed()}%
                                            </div>
                                        </div>`
                if (percent === 100) {
                    progressBar.innerHTML = ""
                }
            }
        }, false)
        cancelButton.addEventListener('click', (e) => {
            e.preventDefault()
            xhr.abort()
            setTimeout(() => {
                uploadForm.reset()
                progressBar.innerHTML = ""
                cancelBox.classList.add('hidden')
            }, 2000)
        })

        return xhr
    }
}
