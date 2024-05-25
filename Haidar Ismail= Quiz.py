L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]
DD = dict(zip(L1, L2))
print(DD)



x = int(input("the number: "))
def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)    
fact = factorial(x)
print(f"The factorial of {x} is {fact}")


L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']
for z in L:
    if z.startswith('B'):
        print(z)

H = {i: i+1 for i in range(11)}
print(H)



def binary_to_decimal(binary_str):
    try:
        for digital in binary_str:
            if digital not in ['0', '1']:
                raise ValueError("Input must be only 1s or 0s.")
        decim = int(binary_str, 2)
        return decim
    except ValueError as y:
        print(y)
        return None
binary_numberber = input("Enter a binary numberber: ")
decimal_numberber = binary_to_decimal(binary_numberber)
if decimal_numberber is not None:
    print(f"The equivalent decimal numberber is: {decimal_numberber}")


import json
import csv

def calculate_score(user_answers, correct_answers):
    score = 0
    for question, answer in user_answers.items():
        if answer == correct_answers.get(question):
            score += 1
    return score

def save_results(user_name, user_answers, score, file_format):
    file_name = f'{user_name}_quiz_results.{file_format}'
    if file_format == 'json':
        with open(file_name, 'w') as json_file:
            json.dump({'User': user_name, 'Score': f'{score}/20', 'User Answers': user_answers}, json_file)
        print('Quiz results saved in JSON format.')
    elif file_format == 'csv':
        with open(file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Question', 'User Answer'])
            for question, answer in user_answers.items():
                csv_writer.writerow([question, answer])
            csv_writer.writerow(['Score', f'{score}/20'])
        print('Quiz results saved in CSV format.')
    else:
        print('Invalid file format. Results not saved.')

user_name = input('Enter your name: ')

file_name = input('Enter the file name with questions and answers: ')

with open(file_name, 'r') as file:
    data = file.read()

questions_and_answers = json.loads(data)

user_answers = {}
for question in questions_and_answers.keys():
    user_answer = input(f'Your answer for "{question}": ')
    user_answers[question] = user_answer

score = calculate_score(user_answers, questions_and_answers)
print(f'Your score is: {score}/20')

file_format = input('Choose the file format to save the results (JSON or CSV): ')
save_results(user_name, user_answers, score, file_format)



class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insu funds.")
    def get_balance(self):
        return self.balance
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
    def __str__(self):
        return f"Account holder: {self.account_holder}\nAccount Balance: ${self.balance:.2f}\nInterest Rate: {self.interest_rate*100:.2f}%"
bank_account = BankAccount("11223344", "Ismail")
bank_account.deposit(1000)
print(f"Current Balance: ${bank_account.get_balance():.2f}")
bank_account.withdraw(500)
print(f"Current Balance: ${bank_account.get_balance():.2f}")
savings_account = SavingsAccount("44556677", "Haidar ", 0.05)
savings_account.apply_interest()
print(savings_account)
    
