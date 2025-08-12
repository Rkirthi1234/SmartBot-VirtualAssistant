import webbrowser
import pygetwindow as gw
import datetime
import pywhatkit as pwk
import time

def display_whatsapp_qr():
    webbrowser.open("https://web.whatsapp.com/")
    print("Please scan the QR code on WhatsApp Web.")
    time.sleep(10)

    try:
        whatsapp_window = gw.getWindowsWithTitle("WhatsApp")[0]
        whatsapp_window.minimize()
        print("WhatsApp Web window minimized.")
    except IndexError:
        print("WhatsApp window not found.")
def schedule_notification_custom_time(receiving_number, custom_time, notification_message):
    try:
        custom_time = datetime.datetime.strptime(custom_time, "%H:%M")
        now = datetime.datetime.now()
        notification_time = now.replace(hour=custom_time.hour, minute=custom_time.minute, second=0, microsecond=0)

        if now > notification_time:
            notification_time += datetime.timedelta(days=1)  # Schedule for the next day if the time has already passed

        delay = (notification_time - now).total_seconds()
        print(f"Scheduling a notification at {notification_time.strftime('%H:%M')}")
        time.sleep(5)

        # Send the message using pywhatkit
        pwk.sendwhatmsg(receiving_number, notification_message, notification_time.hour, notification_time.minute)

    except ValueError:
        print("Invalid time format. Please use HH:MM format.")

