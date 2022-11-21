#Object Oriented Programming - Calculation of Rental Income/// 

class incomecalulation():
    ##calulation of rental income
    def __init__(self):
        self.monthlyincome12 = 0
        self.monthlyexpences1 = 0
        self.monthlycashflow = 0
        self.allinvestment = 0
        self.cashoncashroi = 0
    #now let define revenu from rental income 
    def income(self):
        self.mrentals = int(input(f'Please enter your rental income for your property: '))
        self.mstorage = int(input(f'what is the montly income from storage services: '))
        self.mlaundry = int(input(f'What is the toal monthly income from laundry: '))
        self.miscellaneousincome = int(input("Please enter the estimated miscellaneous income: "))
    #now using if and elif statment for income

        if self.mrentals > 0:
          print(f'your monthly rent income is {self.mrentals}')
        elif self.mrentals < 0:
            print(f'Try again wrong input')

        if self.mstorage > 0:
            print(f'Your monthly income for for storage is {self.mstorage}')
        elif self.mstorage < 0:
            print(f'wrong input please try again')
        if self.mlaundry > 0:
            print(f'The laundry income for your rental property is {self.mlaundry} ')
        elif self.mlaundry < 0:
            print(f'wrong response plase try again later')
        if self.miscellaneousincome > 0:
            print(f'Your miscellaneous income is {self.miscellaneousincome}')
        
        # now we will add the input from the user to calulate the monthly income from rental, storage, laundry and miscellaneousincome
        self.totalmonthincome = self.mrentals + self.mstorage + self.mlaundry + self.miscellaneousincome
        print(f"The total monthly income is: {self.totalmonthincome}")
         #get monthly expenses


    def expences(self):
        self.morgage = int(input(f'what is your expence for morgage'))
        self.tax = int(input(f'what is your monthly tax expence'))
        self.propertymanager = int(input(f'what is your exence for property managers'))
        self.insurance = int(input(f'what is your insurance expenses'))
        self.vacancy = int(input(f'what is your vacancy monthly expense for your property'))

        if self.morgage >= 0:
            print(f"Your monthly morgage is {self.morgage}")
        elif self.morgage < 0:
            print("Invalid input, please try again.")

        if self.tax >= 0:
            print(f"Your montly tax expense is {self.tax} ")
        elif self.tax < 0:
            print("Invalid Input, check your info please try again.")
        if self.propertymanager >= 0:
            print(f" Your monthly fee for the poperty manager is {self.propertymanager}")
        elif self.propertymanager < 0:
            print("Invalid Input, please try again.")
        if self.insurance >= 0:
            print(f'your insurance expense is: {self.insurance}')
        elif self.insurance > 0:
            print(f'your expenses for insurance is: {self.insurance} ')
        if self.vacancy > 0:
            print(f'the vacancy expense for your property is: {self.vacancy}')

        self.totalexpense = self.morgage + self.tax + self.propertymanager + self.insurance + self.vacancy
        print('Your total monthly expense: {self.totalexpense}')

        #now I am looking for a method to caluate to subtract monthly income with total expense
        #The monthly available cash flow is subracting monthly income with expense

        totalmonthlycashflow = self.totalmonthincome - self.totalexpense
        print(f' Your total monthly cash flow is: {totalmonthlycashflow}')


         #total investment  on the property
    def totalpropertyinvestments(self):
        self.downpayment = int(input(f'how much is your downpayment'))
        self.closeingcost = int(input(f'how much was your closing cost'))
        self.rehabbudget = int(input(f'how much do you pay for property rehab budget'))

        #adding up all of the investments for the property
        self.totalinvestments = self.downpayment + self.closeingcost + self.rehabbudget
        print(f'Your total investment for the property is: {self.totalinvestments}' )

        
   
    def totalroiinvestment():
        yearlycashflow = self.totalmonthlycashflow * 12
        print(yearlycashflow)

incomecalulation()


        
    






    
    


        



     


