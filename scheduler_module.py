import datetime
import pywhatkit as pwk

def schedule_notification_custom_time(receiving_number, custom_time, notification_message):
    custom_time = datetime.datetime.strptime(custom_time, "%H:%M")
    now = datetime.datetime.now()
    notification_time = now.replace(hour=custom_time.hour, minute=custom_time.minute)

    if now > notification_time:
        notification_time += datetime.timedelta(days=1)

    pwk.sendwhatmsg(receiving_number, notification_message, notification_time.hour, notification_time.minute)
