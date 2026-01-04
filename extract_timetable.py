# import required modules
from bs4 import BeautifulSoup
import os, re



# function to open and parse file with beautifulsoup
# (also handles FileNotFoundError)
# - returns parsed soup object
def open_and_parse_file(FILE_NAME):

    if not os.path.exists(FILE_NAME):
        raise FileNotFoundError(f"Error: HTML file '{FILE_NAME}' not found!")
    
    else:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')

    return soup



# extracts course and lesson details from parsed HTML
# - returns dict: 
#   + key = course code:
#       - course_name (str)
#       - lessons (list of dicts):
#           + class_nbr     (str)
#           + section       (str)
#           + component     (str)
#           + days_times    (str)
#           + room          (str)
#           + instructor    (str)
#           + dates         (str)
def extract_details(soup):

    # define dict to store all courses
    courses = {}

    # each course is contained in a <td> with the class 'PAGROUPDIVIDER'
    for header_td in soup.select('td.PAGROUPDIVIDER'):
        text = header_td.get_text(" ", strip=True)

        # splits header text into course code and course name
        # e.g.: "CSCI218 - Foundations of AI" = "CSCI218", "Foundations of AI"
        course_code, course_name = text.split(" - ", 1)

        # clean formatting of course_code
        course_code = course_code.replace(" ", "").strip()
        course_name = course_name.strip()

        # add course entry into dcit
        courses[course_code] = {
            "course_name": course_name,
            "lessons": []
            }
        
        # find lesson table that appears after cousrse header
        # (table ID starts with "CLASS_MTG_VW$scroll$")
        lessons_table = header_td.find_next(
            "table",
            id=re.compile(r"^CLASS_MTG_VW\$scroll\$")
        )

        # skips course if no lessons found
        if not lessons_table:
            print(f"Error: No classes found for '{course_code} - {course_name}'!")
            continue

        # variables to store last non-empty value as some roles omit repeated values
        current_class_nbr = None
        current_section = None
        current_comp = None

        # loop through each row in the lesson table
        for tr in lessons_table.select("tr"):

            tds = tr.find_all("td")

            # skip rows that does not contain lesson data
            if len(tds) < 7:
                continue

            # helper function to clean and normalise cell text
            def td_text(i):
                return (
                    tds[i]
                    .get_text(" ", strip=True)
                    .replace("\xa0", "")
                    .strip()
                )

            # extract values from table rows
            class_nbr = td_text(0) or None
            section   = td_text(1) or None
            comp      = td_text(2) or None
            sched     = td_text(3) or None
            room      = td_text(4) or None
            instr     = td_text(5) or None
            dates     = td_text(6) or None

            # update current values if there is a new value
            if class_nbr:
                current_class_nbr = class_nbr
            if section:
                current_section = section
            if comp:
                current_comp = comp

            # store lesson details
            courses[course_code]["lessons"].append({
                "class_nbr": current_class_nbr,
                "section": current_section,
                "component": current_comp,
                "days_times": sched,
                "room": room,
                "instructor": instr,
                "dates": dates,
            })
    
    # return all extracted course data
    return courses



# function to print extracted course and lesson details in a readable format for checking
def print_courses(courses):
    
    # handles case where there are no courses
    if not courses:
        print("No courses found")
        return
    
    print("Courses found:\n" + "-" * 40)

    # loop through each course
    for k in courses.keys():
        print(f"Course Code: {k}")
        print(f"Course Name: {courses[k]['course_name']}")

        # print all lessons under the current course
        for lesson in courses[k]["lessons"]:
            print(lesson)

        print()



# function to load HTML file, parse it, and extract timetable information
# - returns dict of courses and lessons like in extract_details()
def get_timetable(FILE_NAME_HTML):

    soup = open_and_parse_file(FILE_NAME_HTML)
    courses = extract_details(soup)

    return courses



def main():

    FILE_NAME_HTML = 'test.html'

    courses = get_timetable(FILE_NAME_HTML)
    print_courses(courses)



if __name__ == "__main__":
    main()