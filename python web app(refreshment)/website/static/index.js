function deleteNote(noteId) {
    fetch('/delete', {
        method: 'POST',
        body: JSON.stringify({noteId})
    }).then(res => window.location.href = '/');
}