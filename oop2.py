class Account:
    def __init__(self,  acc_no, acc_pass):
        self.acc_no = acc_no;
        self.__acc_pass = acc_pass;

    def reset_pass(self):
        print(self.__acc_pass);

ac1 = Account("Prathamesh", "123asd")

print(ac1.acc_no)
print(ac1.reset_pass())