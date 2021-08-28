class Calculator():
    def add(self,num1,num2):
        return num1+num2
    def substract(self,num1,num2):
        return num1-num2
    def multiple(self,num1,num2):
        return num1*num2
    def division(self,num1,num2):
        if num2==0:
            return 0
        else:
            return num1/num2


if __name__=="__main__":
    calculator=Calculator()
    print(calculator.add(1,2))
