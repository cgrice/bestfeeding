$(document).ready(function() {
    $('.feeds .delete').on('click', function(event) {
        $(this).closest('tr').fadeOut();
    });
});
