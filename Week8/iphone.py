class iPhone:
    def __init__(self, name, version, number, color, model):
        self.name = name
        self.ios_version = version
        self.phone_number = number
        self.phone_color = color
        self.phone_model = model 
        self.files = []

    def airdrop(self, filename, recipient):
        if isinstance(recipient, iPhone):
            print(f"Air Dropping '{filename}' from {self.name} to {recipient.name}")
            recipient.files.append(filename)
            print(f"Files on {recipient.name} after AirDrop: {recipient.files}")

    def show_files(self):
        print(f"Files on {self.name}: {self.files}")

harsha_iphone = iPhone(
    name = "Harsha's Iphone",
    version = '18.0.1',
    number = '423-531-2116',
    color = "Deep Purple",
    model = "16 Pro Max",
)    

recipient_iphone = iPhone(
    name = "Recipient's Iphone",
    version = '18.0.1',
    number = '123-456-7890',
    color = "Gold",
    model = "15 Pro Max",
)   

harsha_iphone.files = ["Week6.pdf", "Week8.pdf"]
recipient_iphone.files = ["Week6.pdf", "TECHIN509.pdf"]

harsha_iphone.show_files()
recipient_iphone.show_files()

# print(harsha_iphone.name)
harsha_iphone.airdrop("Week8.pdf", recipient_iphone)

harsha_iphone.show_files()
recipient_iphone.show_files()

