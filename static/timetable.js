$(document).ready(function() {
    // Enable drag-and-drop for timeslots
    $(".timeslot").draggable({
        helper: 'clone',
        zIndex: 100,
        revert: 'invalid'
    });

    // Enable drop functionality for table cells
    $("td").droppable({
        accept: ".timeslot",
        drop: function(event, ui) {
            // Get the dropped timeslot data
            var droppedTimeslot = ui.helper.data();
            
            // Check for conflicts in the same time slot on the selected day
            var targetDay = droppedTimeslot.weekday;
            var targetTime = droppedTimeslot.time;

            var existingTimeslot = $(this).find('.timeslot[data-weekday="' + targetDay + '"][data-time="' + targetTime + '"]');

            if (existingTimeslot.length > 0) {
                alert('Time slot conflict! Please choose another time slot.');
                ui.helper.draggable('cancel');
            } else {
                // Move the timeslot to the selected cell
                var clonedTimeslot = ui.helper.clone();
                $(this).empty().append(clonedTimeslot);
                clonedTimeslot.draggable({
                    helper: 'clone',
                    zIndex: 100,
                    revert: 'invalid'
                });
            }
        }
    });
});
