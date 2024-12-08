class Information:
    def __init__(self,name,gender,age,contact_number,email_address):
        self.name = name
        self.gender = gender
        self.age = age
        self.contact_number = contact_number
        self.email_address = email_address

    def save_data(self):
        with open(f"Information.txt", 'w') as file:
            file.write(f"{self.name} have gender {self.gender} of age {self.age} having contact no.{self.contact_number} and email {self.email_address}\n")
            print("Your Data Has Been Saved!!!")

y_name = input("Enter Your Name:")
y_gender = input("Enter Your Gender:")
y_age = int(input("Enter Your Age:"))
y_contact = int(input("Enter Your Phone Number:"))
y_email_address = input("Enter Your Email Address:")

inf = Information(y_name,y_gender,y_age,y_contact,y_email_address)
inf.save_data()

