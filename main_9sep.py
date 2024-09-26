class ATM:
    def _init_(self, BankName="BOI", Pin=1234, Balance=5000):
        self.bankName = BankName
        self.pin = Pin
        self.balance = Balance

    def Verification(self):
        print("Wait for few sec...")
        print("Details are varifying...")
        print("Verification is successfully done: ")
        pin = int(input("Enter your Pin:"))
        self.userValidation(pin)

    def userValidation(self, Pin):
        while(True):
            if self.pin == Pin:
                print("1. Withdrawl Amount:")
                print("2. Check Balance:")
                chooice = int(input("Enter :"))
                match(chooice):
                    case 1:
                        amt = int(input("Enter your Amount : "))
                        self.WithdrawlAmt(amt)
                    case 2:
                        self.CheckBalance()
                    case _:
                        print("Invalid choice")

                # if chooice == 1:
                #     self.WithdrawlAmt()
                # elif chooice == 2:
                #     self.checkBalance()
                # else:
                #     print("Invalid choice")

            else:
                print("Invalid Pin: ")

    def WithdrawlAmt(self, W_Atm):
        if self.balance >= W_Atm:
            self.balance -= W_Atm
            print("Withdrawl is successfully done! \n(Kindly Collect Your Cash)")
        else:
            print("Insufficient Balance: ")

    def CheckBalance(self):
        print("Your Current Balance is: ", self.balance)


atm = ATM()

