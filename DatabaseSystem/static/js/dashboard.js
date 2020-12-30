$(document).ready(function () {
    $('#bootstrapdatatable').DataTable({
        "aLengthMenu": [
            [3, 5, 10, 25, -1],
            [3, 5, 10, 25, "All"]
        ],

        "iDisplayLength": 3
    });
});

var text = document.getElementById('prompt');

function closeText() {
    text.parentNode.removeChild(text);
}

function promptDelete(e) {
    if (!confirm('Are you sure you want to delete item? You cannot undo this action.')) {
        e.preventDefault();
    }
}