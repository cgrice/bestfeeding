$(document).ready(function() {
    $('.feeds .delete').live('click', function(event) {
        $(this).closest('tr').fadeOut();
    });
});
