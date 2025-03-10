ClassicEditor
    .create(document.querySelector('#id_content'), {
        ckfinder: {
            uploadUrl: '/ckeditor/upload/',  // Django CKEditor upload URL
        }
    })
    .catch(error => {
        console.error(error);
    });
