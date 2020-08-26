# working on final project to combine all the learnt concepts into 1
# problem statement.
#The CTO wants to monitor all the computer usage by all engineers. Using Python ,
# write an automation script that will produce a report when each user logged in and out,
# and how long each user used the computers.



# writing real script:
# first sort all the processes by date using a function:
def get_event_date(event):
    return event.date
#get current user and pass the sorted date function
# first sort all the processes by date using a function:
def get_event_date(event):
    return event.date
#get current user and pass the sorted date function
# first sort all the processes by date using a function:
def get_event_date(event):
    return event.date
#get current user and pass the sorted date function
def current_users(events):
    events.sort(key=get_event_date)
    #create a dictionary to store the values
    machines = {}
    for event in events:
        #check if a mchine exist in dictionary  else add
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "logout":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines
#create a different function to print the report
def generate_report(machines):
    for machines,users in machines.items():
        #print only thoses who logged in and not those who loged in and out:
        if len(users)>0:
            users_list = ", ".join(users)
            print("{} : {}".format(machines,users_list))

class Event:
    def __init__(self, event_date, event_type, machine_name,user):
        self.date = event_date
        self.type = event_type
        self.machine =machine_name
        self.user = user
events = [
    Event("2020-05-12 12:50PM","login","mail-server local", "owen"),
    Event("2021-04-12 4:50PM","logout","mail-server local", "james"),
    Event("2020-05-14 2:50PM","login","workstation local", "shem"),
    Event("2020-05-1 16:50PM","login","mail-server local", "Timz"),
    Event("2020-06-19 18:50PM","logout","admin server local", "brian"),
    Event("2020-02-12 17:50PM","login","mail-server local", "chris")
    ]

#try creation
users = current_users(events)
print(users)

# generate user report
generate_report(users)

# CONGRATALTIONS: 
# Up next final project;
