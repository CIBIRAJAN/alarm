import winsound #specily uses for desktop notifier
from win10toast import ToastNotifier
def timer (reminder,seconds):
    notificator=ToastNotifier()
    notificator.show_toast("Reminder",f"""Alarm will go off in{seconds}seconds.""",duration=20)
    notificator.show_toast("Reminder",remider,duration=20)
#alarm
    frequency=2500
    duration=1000
    winsound.Beep(frequency,duration)
if __name__=="__main__":
    words=input("What would you remides of: ")
    sec=int(input("Enter second: "))
    timer(words,sec)
    
