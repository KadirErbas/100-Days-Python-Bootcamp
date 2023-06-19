from plyer import notification

notification_title = '100 Days Programing Camp'
notification_message = 'Thanks for the education Atil Samancioglu!'

notification.notify(
    title = notification_title,
    message = notification_message,
    app_icon =  "myico.ico",
    timeout = 3,
    toast = False
)