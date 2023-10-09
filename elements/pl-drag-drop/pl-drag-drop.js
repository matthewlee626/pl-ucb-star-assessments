$(function() {
    $("#data-frame tbody tr").draggable({
        helper: "clone",
        opacity: 0.5,
        zIndex: 1000
    });

    $("#data-frame th").draggable({
        helper: "clone",
        opacity: 0.5,
        zIndex: 1000
    });

    // Make the table rows and columns droppable
    $("#data-frame tbody tr, #data-frame th").droppable({
        accept: "#data-frame tbody tr, #data-frame th",
        drop: function(event, ui) {
            var draggable = ui.draggable;
            var droppable = $(this);

            // Swap the content of the dragged and dropped cells
            var temp = droppable.html();
            droppable.html(draggable.html());
            draggable.html(temp);

            const thElements = document.querySelectorAll('th');
            const tdElements = document.querySelectorAll('td');

        }
    });
    
    //This code works when it's placed at the top
    //$('#data-frame').append('<p>This text was added by a script.</p>');
})
