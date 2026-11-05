# Factory Pattern - Notification System

class Notification:
    def send(self):
        pass


class Email(Notification):
    def send(self):
        print("Sending Email notification.")


class SMS(Notification):
    def send(self):
        print("Sending SMS notification.")


class WhatsApp(Notification):
    def send(self):
        print("Sending WhatsApp notification.")


class NotificationFactory:
    @staticmethod
    def get_notification(choice):
        if choice == "email":
            return Email()
        elif choice == "sms":
            return SMS()
        elif choice == "whatsapp":
            return WhatsApp()
        else:
            return None


choice = input("Enter notification (email/sms/whatsapp): ").lower()

notification = NotificationFactory.get_notification(choice)

if notification:
    notification.send()
else:
    print("Invalid notification type.")
```