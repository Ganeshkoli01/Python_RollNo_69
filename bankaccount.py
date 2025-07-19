class Account():
          def __init__(self,bal,acc):
                    self.bal=bal
                    self.acc=acc
                    
          def debit(self,amount):
                    self.bal-=amount
                    print("Rs",amount,"was debitet")
                    print("total balance:",self.get_balance())
                    

          def credit(self ,amount):
                    self.bal+=amount
                    print("Rs",amount,"was credited")
                    print("total balance:",self.get_balance())
                    
          def get_balance(self):
                    return self.bal 
          

initial_bal = int(input("Enter initial balance: "))
account_number = int(input("Enter account number: "))

acc1 = Account(initial_bal, account_number)

debit_amt = int(input("Enter amount to debit: "))
acc1.debit(debit_amt)

credit_amt = int(input("Enter amount to credit: "))
acc1.credit(credit_amt)

print("Final Balance:", acc1.get_balance())