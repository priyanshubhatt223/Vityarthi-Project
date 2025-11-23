# Assignment Submission Reminder

##  Overview

The **Assignment Submission Reminder** is a Python-based console
application designed to help students keep track of their assignment
deadlines. Users can add, view, delete, and monitor upcoming assignments
using an interactive menu-driven interface.\
The program stores assignment titles along with their submission dates
and times, and also alerts users about submissions due within the next
24 hours.

##  Features

###  Add Assignments

-   Enter assignment title, date, and time.\
-   Stores the assignment along with a timestamp.

###  View Assignments

-   Displays all added assignments sorted by nearest deadline.\
-   Shows both date and time in a readable format.

###  Delete Assignments

-   View the list with index numbers and remove any selected assignment.

###  Upcoming Due Alerts

-   Checks for assignments due within the next **24 hours**.\
-   Displays the time remaining in hours and minutes.

###  User-Friendly Menu

-   Simple console-based interface that guides the user step-by-step.

##  Technologies / Tools Used

-   **Python 3.x**
-   **datetime module**
-   **Basic I/O functions**
-   **Sorting and list operations**

##  Steps to Run the Project

1.  **Install Python 3**\
    Check using:

    ``` bash
    python --version
    ```

2.  **Save the script**\
    Create a `.py` file (e.g., `assignment_reminder.py`) and paste the
    code.

3.  **Run the program**

    ``` bash
    python assignment_reminder.py
    ```

##  Instructions for Testing

### 1. Test Adding Assignments

-   Add valid and invalid dates/time values.

### 2. Test Viewing Assignments

-   Ensure sorting by date/time.

### 3. Test Deleting Assignments

-   Delete valid index, invalid index, or cancel with 0.

### 4. Test Upcoming Submissions

-   Add one assignment due within 24 hours and one farther away.

### 5. Test Exit Option

-   Choose option **5** to exit smoothly.