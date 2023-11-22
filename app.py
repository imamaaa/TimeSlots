from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

# Placeholder data for courses, resources, and other necessary information
courses = ["Course A", "Course B", "Course C"]
resources = ["Room 101", "Room 102", "Room 103"]
weekdays = ["Monday"]#, "Tuesday", "Wednesday", "Thursday", "Friday"]

# Placeholder time slot structure
class TimeSlot:
    def __init__(self, start_time, end_time, weekday, course, resource):
        self.start_time = start_time
        self.end_time = end_time
        self.weekday = weekday
        self.course = course
        self.resource = resource

# Placeholder function for time slot generation
def generate_time_slots(start_time="08:30 AM", num_time_slots=8):
    time_slots = []

    for _ in range(num_time_slots):
        for weekday in weekdays:
            for course in courses:
                for resource in resources:
                    end_time = calculate_end_time(start_time)
                    time_slots.append(TimeSlot(start_time, end_time, weekday, course, resource))

        # Calculate the next start time for the next time slot
        start_time = calculate_next_start_time(start_time)

    return time_slots

def calculate_end_time(start_time):
    time_format = "%I:%M %p"  # 12-hour time format
    start_datetime = datetime.strptime(start_time, time_format)
    end_datetime = start_datetime + timedelta(hours=1, minutes=20)
    return end_datetime.strftime(time_format)

def calculate_next_start_time(current_start_time):
    time_format = "%I:%M %p"  # 12-hour time format
    current_datetime = datetime.strptime(current_start_time, time_format)
    next_datetime = current_datetime + timedelta(hours=1, minutes=20)
    return next_datetime.strftime(time_format)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_time_slots', methods=['GET', 'POST'])
def generate_time_slots_route():
    if request.method == 'POST':
        start_time = request.form.get('start_time')
    else:
        start_time = "08:30 AM"  # Default start time

    # Assuming you have a way to determine the current day dynamically
    # In this example, let's assume it's Wednesday (3rd day of the week)
    current_day = 1

    # Call the time slot generation function with the specified start time
    generated_time_slots = generate_time_slots(start_time=start_time)

    return render_template('time_slots.html', time_slots=generated_time_slots, start_time=start_time, current_day=current_day)


if __name__ == '__main__':
    app.run(debug=True)




