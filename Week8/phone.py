class iPhone:
    def __init__(self, name, version, number, color, model):
        self.name = name
        self.ios_version = version
        self.phone_number = number
        self.phone_color = color
        self.phone_model = model 
        self.messages = []

    def imessages(self, message, recipient):
        if isinstance(recipient, iPhone):
            print(f"Sending iMessage '{message}' from {self.name} to {recipient.name}")
            recipient.messages.append({"text": message, "read": False})

    def show_messages(self):
        print(f"\n Messages on {self.name}: ")

        if not self.messages:
            print("No Messages.")
        for idx, message in enumerate(self.messages, 1):
            status = "Read" if message["read"] else "Unread"
            print(f"{idx}. {message['text']} ({status})")
            message["read"] = True

    def unread_count(self):
        count = sum(1 for message in self.messages if not message["read"])
        print(f"\n{self.name} has {count} unread messages.")

    def set_name(self, new_name):
        print(f"This iPhone's name is {self.name}")
        self.name = new_name
        print(f"Name is being changed to: '{self.name}'\n")

phone1 = iPhone(
    name = "Harsha's Iphone",
    version = '18.0.1',
    number = '423-531-2116',
    color = "Deep Purple",
    model = "16 Pro Max",
)    

phone2 = iPhone(
    name = "Recipient's Iphone",
    version = '18.0.1',
    number = '123-456-7890',
    color = "Gold",
    model = "15 Pro Max",
)   

phone1.set_name("Harshavardhan's iPhone")
phone2.set_name("Ian's iPhone")

phone1.imessages("Hey! How are you!", phone2)
phone2.imessages("I am doing great! What about you? Are you liking the TECHIN509 class so far?", phone1)

phone1.imessages("I am good! Thank you!", phone2)
phone1.imessages("Yes, I am loving it so far. I wish to learn more in the future!", phone2)

phone1.unread_count()
phone2.unread_count()

phone1.show_messages()
phone2.show_messages()

phone1.unread_count()
phone2.unread_count()

