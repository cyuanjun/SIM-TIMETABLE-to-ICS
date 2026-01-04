# import required modules
from icalendar import Calendar, Event
from datetime import datetime as dt
import pytz
import extract_timetable as et

# INPUT FILE NAME (CHANGE THIS):
# (keep .html)
FILE_NAME_HTML = 'mock_html.html'
# OUTPUT FILE NAME (CHANGE THIS):
# (keep .ics)
FILE_NAME_ICS = "mock_timetable.ics"



# function to create .ics file from cources dict
def create_calendar(courses, tz):

    # create calander
    cal = Calendar()
    cal.add("prodid", "-//Chia Yuan Jun//SIM Timetable Generator//SG")
    cal.add("version", "2.0")
    cal.add("calscale", "GREGORIAN")

    # loop through courses 
    for k in courses.keys():

        course_code = k
        course_name = courses[k]["course_name"]

        # loop through each lesson in a course
        for lesson in courses[k]["lessons"]:

            # extract details from each lesson
            class_nbr = lesson["class_nbr"]
            section = lesson["section"]
            component = lesson["component"]
            room = lesson["room"]
            instructor = lesson["instructor"]

            times = lesson["days_times"]
            time_parts = times.split()
            start_time = time_parts[1]
            end_time = time_parts[3]

            dates = lesson["dates"]
            date_parts = dates.split()
            date = date_parts[0]


            # create events with extracted details
            date = dt.strptime(date, "%d/%m/%Y").date()
            start_time = dt.strptime(start_time, "%H:%M").time()
            end_time = dt.strptime(end_time, "%H:%M").time()

            uid = (
                f"{course_code}_{section}_"
                f"{start_time.strftime('%H%M')}-{end_time.strftime('%H%M')}_"
                f"{date.strftime('%Y%m%d')}"
                "@github.com/cyuanjun"
            )

            summary = f"{course_code}-{component[:3]}"

            event = Event()
            event.add("uid", uid)
            event.add("dtstamp", tz.localize(dt.now()))
            event.add("summary", summary)
            event.add("dtstart", tz.localize(dt.combine(date, start_time)))
            event.add("dtend", tz.localize(dt.combine(date, end_time)))
            event.add("location", room)
            event.add(
                "description",
                f"COURSE CODE: {course_code}\n"
                f"COURSE NAME: {course_name}\n"
                f"CLASS NUMBER: {class_nbr}\n"
                f"SECTION: {section}\n"
                f"COMPONENT: {component}\n"
                f"INSTRUCTOR: {instructor}\n"
                f"IMPORTED FROM SIM-TIMETABLE-to-ICS:\n"
                f"github.com/cyuanjun/SIM-TIMETABLE-to-ICS\n"
            )

            # add event to calendar
            cal.add_component(event)

    # write .ics file for the calendar
    with open(FILE_NAME_ICS, 'wb') as f:
        f.write(cal.to_ical())



def main():

    print("\nCreating file...")

    # specifying timezone
    tz = pytz.timezone("Asia/Singapore")

    # getting course and lessond data from HTML
    courses = et.get_timetable(FILE_NAME_HTML)

    # creates .ics file from courses dict
    create_calendar(courses, tz)

    print(f"Calendar file: '{FILE_NAME_ICS}' successfully created")



if __name__ == "__main__":
    main()