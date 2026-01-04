# SIM-TIMETABLE-to-ICS 🎯
SIM-TIMETABLE-to-ICS is a python based tool that extracts timetable data from the SIMConnect portal and converts them into a standards-compliant iCalendar (.ics) file for seamless imports into **Google Calendar, Apple Calendar, and Outlook.**

---

## 📊 Project Overview
The motivation behind this project came from real, everday frustrations:
- Checking my timetable required repeatedly logging into the SIMConnect website or app, which was troublesome, slow, and the UI/UX was not the best.
- There was no easy way to view my lessons alongside my personal calendar. This made it troublesome when planning my days as it often required me to switch between my personal calendar and the SIM website/app.

This tool aims to solve these issues by allowing timetable data to be imported directly into personal calendars such as **Google Calendar, Apple Calendar, Outlook**, allowing schedules to be easier to view, manage, and cross-check.

---

## ✨ Key Features
- 📍 Timezone-aware events (Asia/Singapore)

- 🔁 Stable event UIDs for safe re-imports (no duplicate events)

- 📝 Clean event summaries, descriptions, and locations

- 📱 Compatible with mobile and desktop calendar clients

- 📆 Standards-compliant iCalendar output (RFC 5545)

---

## 🧠 What This Project Explores
- Practical use of the iCalendar (RFC 5545) specification
- Handling real-world differences between calendar clients (Google vs Apple vs Outlook)
- Robust parsing and data normalization from web-based timetable sources
- Timezone correctness and event identity management
- Turning a personal workflow problem into a reusable automation tool

---

## 🧰 Tech Stack
- **Language**:
```
    - Python 3
```

- **Libraries**:
```
    - BeautifulSoup4    (For HTML parsing and data extraction)
    - icalendar         (For iCalendar (.ics) file generation)
    - datetime          (For date and time parsing and manipulation)
    - pytz              (For timezone handling)
    - os                (For file system operations)
    - re                (For pattern matching with regular expressions) 
```

---

## 📁 Project Structure
```
SIM-TIMETABLE-to-ICS/
├── assets/                 # Folder containing README images
├── extract_timetable.py    # Script to extract course/lesson data from HTML
├── generate_ics.py         # Main script generating .ics file
├── mock_html_test.html     # Example HTML from SIMConnect Website
├── mock_timetable.ics      # Output .ics file with timetable data
├── README.md               # Project documentation
└── requirements.txt        # Python package dependencies
```

---

## ▶️ How to Use
1. **Clone the repository**:
    ```bash
    git clone https://github.com/cyuanjun/SIM-TIMETABLE-to-ICS.git
    ```

2. **Change directory**:
    ```bash
    cd SIM-TIMETABLE-to-ICS
    ```

3. **Create/Activate virtual environment (Optional)**:
    
    - #### Windows:
        - Creating virtual environment
        ```bash
        python -m timetable_to_ics_venv
        ```

        - Activating virtual environment
        ```
        timetable_to_ics_venv\Scripts\activate
        ```
    - #### Mac:
        - Creating virtual environment
        ```bash
        python3 -m venv timetable_to_ics_venv
        ```

        - Activating virtual environment
        ```
        source timetable_to_ics_venv/bin/activate
        ```

    - #### Deactivating virtual environment (Windows/Mac)
        - Same for Windows / Mac
        ```bash
        deactivate
        ```

4. **Install necessary libraries from requirements.txt file into virtual environment**:
    ```bash
    pip install -r requirements.txt
    ```
5. **Getting HTML table data**:

    ![Timetable Exraction 1](assets/timetable_extraction_1.png)
    - Login to the SIMConnect page and navigate to the "My Apps" section on the top left.
    - Click on the dropdown menu under Academics with "other academic...", select "Personalised Timetable", and click the arrow icon beside.
    - You should end up at the timetable page.

    ![Timetable Exraction 2](assets/timetable_extraction_2.png)
    - Right click on the timetable table and click on "View frame source".
    - A page should pop up. Copy everything on that page using "CTRL + A" and "CTRL + C".

    ![Timetable Exraction 3](assets/timetable_extraction_3.png)
    - Paste the contents into your notepad and save it as a .html file (Remember to change the file type to "All files"). You can put any name you want, for simplicity we're using "timetable_data.html".

6. **Running the script**:
    ```bash
    python generate_ics.py
    ```

---

## ⚠️ Disclaimer

This project is built specifically for SIM timetable data and is intended for personal and educational use.
It is not an official SIM tool and is not affiliated with or endorsed by Singapore Institute of Management.

---



