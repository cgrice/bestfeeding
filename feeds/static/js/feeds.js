$(document).ready(function() {
    $('.feeds .delete').on('click', function(event) {
        event.preventDefault();
        $(this).closest('tr').fadeOut();
        if($(this).closest('.feeds').find('tr').length <= 0) {
            $(this).closest('.feeds').remove();
        }
    });
});
