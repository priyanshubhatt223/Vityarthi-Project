#displaying all the options
def opt():
    print("1. Add an assignment")
    print("2. View all assignments")
    print("3. Delete an assignment")
    print("4. Check for upcoming assignments")
    print("5. Exit")

#storing assignmenta in a list
assignments = []

import datetime
#adding assignments to the list
def add():
    a = input("Enter assignment title: ")
    print("Enter submission date:")
    yr = int(input("Year (YYYY): "))
    mon = int(input("Month (MM): "))
    day = int(input("Day (DD): "))
    print("Enter submission time:")
    hr = int(input("Hour (0-23): "))
    min = int(input("Minute (0-59): "))
    try:
        assignment_time = datetime.datetime(yr, mon, day, hr, min)        
        assi = {
            'title': a,
            'time': assignment_time
        }
        assignments.append(assi)        
        print(f"\nAssignment '{a}' scheduled for {assignment_time.strftime('%Y-%m-%d %H:%M')}")
        input("Press enter to continue")
    except ValueError:
        print("\nInvalid date or time")
        input("Press enter to continue")

#checking the list of all the assignments
def assigns():
    if not assignments:
        print("No assignment due yet")
    else:
        sort_assi = sorted(assignments, key=lambda x: x['time'])
        for z, assign in enumerate(sort_assi, 1):
            print(f"{z}. {assign['title']}")
            print(f"Date: {assign['time'].strftime('%Y-%m-%d')}")
            print(f"Time: {assign['time'].strftime('%H:%M')}")
    input("Press enter to continue")

#deleting an assignment from the list
def delete():
    if not assignments:
        print("No assignment to delete")
        input("Press Enter to continue")
        return
    for b, assi in enumerate(assignments, 1):
        print(f"{b}. {assi['title']} - {assi['time'].strftime('%Y-%m-%d %H:%M')}")    
    try:
        choice = int(input("\nEnter assignment number to delete (Enter 0 to cancel): "))        
        if choice == 0:
            return
        elif 1 <= choice <= len(assignments):
            deleted = assignments.pop(choice - 1)
            print(f"\nDeleted assignment: {deleted['title']}")
        else:
            print("\nInvalid assignment number")
    except ValueError:
        print("\nPlease enter a valid number")    
    input("Press enter to continue")

#checking for a due submission in the upcoming 24 hours
def rem():
    if not assignments:
        print("No due date")
        input("Press enter to continue")
        return    
    now = datetime.datetime.now()
    upcoming = []    
    for assi in assignments:
        time_until = assi['time'] - now
        if datetime.timedelta(0)<=time_until<=datetime.timedelta(days=1):
            upcoming.append((assi, time_until))    
    if not upcoming:
        print("No submission due in the next 24 hours")
    else:
        print("UPCOMING DUE SUBMISSIONS:")
        for assi, time_until in sorted(upcoming, key=lambda x: x[1]):
            hours = int(time_until.total_seconds()//3600)
            minutes = int((time_until.total_seconds()%3600)//60)            
            print(f"\n{assi['title']}")
            print(f"Scheduled: {assi['time'].strftime('%Y-%m-%d %H:%M')}")
            print(f"In: {hours} hours and {minutes} minutes")
    input("\nPress enter to continue")

import time 
#calling the functions
def main():
    while True:
        opt()      
        choice = input("\nEnter your choice (1-5): ")        
        if choice == '1':
            add()
        elif choice == '2':
            assigns()
        elif choice == '3':
            delete()
        elif choice == '4':
            rem()
        elif choice == '5':
            break
        else:
            print("\nInvalid choice")
            time.sleep(1)

#running the program
main()