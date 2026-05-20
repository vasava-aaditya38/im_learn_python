class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Train is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def fare(self):
        print(f"Ticket fare is: 900 ₹")

t=Train(20905)

t.book("Vadodara","Mumbai")
t.getstatus()
t.fare()
