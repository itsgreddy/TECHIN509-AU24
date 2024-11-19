class Phone:
    def __init__(self, model, number):
        self.model = model
        self.number = number

    def call(self, target_number):
        print(f"{self.model} is calling {target_number}...")

class iPhone(Phone):
    def airdrop(self, filename, recipient):
        print(f"Airdropping '{filename}' to {recipient.model} ({recipient.number})...")

class Android(Phone):
    def okay_google(self):
        print("Listening to the command...")

phone1 = iPhone(model="iPhone 14 Pro Max", number="987-654-2310")
phone1.call('123-456-7890')
phone1.airdrop("TECHIN509.pdf", Phone("iPhone Device", "654-987-3210"))

phone2 = Android(model="Samsung S24+", number="123-456-7890")
phone2.call('987-654-2310')
phone2.okay_google()