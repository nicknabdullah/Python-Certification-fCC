import math

class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.total_withdraw = 0

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'amount': -amount, 'description': description})
            self.total_withdraw += amount
            return True
        else:
            return False
    
    def get_total_withdraw(self):
        return self.total_withdraw

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {destination.name}'})
            destination.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        else: 
            return False

    def __str__(self):
        # Build the centered, asterisk-bordered title (e.g. "*****Food*****")
        star_count = math.floor((30 - len(self.name)) / 2)
        label = ('*' * star_count) + self.name + ('*' * star_count)

        ledger_lines = []     # collect each formatted line here instead of concatenating
        total_amount = 0

        for item in self.ledger:
            # Truncate descriptions over 23 chars, pad shorter ones with trailing spaces
            description_txt = item['description'][:23].ljust(23)

            # Format amount to 2 decimals, right-align within a 7-character field
            amount = item['amount']
            total_amount += amount
            amount_txt = f"{amount:.2f}".rjust(7)

            ledger_lines.append(description_txt + amount_txt)

        total = f'Total: {total_amount:.2f}'

        # Join everything with newlines in a single operation
        return label + '\n' + '\n'.join(ledger_lines) + '\n' + total


    
def create_spend_chart(categories):
    # total spent for all categories
    combined_withdraws = sum(cat.get_total_withdraw() for cat in categories)

    # calculate percents
    rounded_withdraw_percents = []
    for cat in categories:
        percent = (cat.get_total_withdraw() / combined_withdraws) * 100
        rounded = math.floor(percent / 10) * 10
        rounded_withdraw_percents.append(rounded)
    
    # drawing the y-axis and chart bars  
    chart_lines = ''
    line = ''
    print("Combined withdrawals:", combined_withdraws)

    for i in range(100, -10, -10):
        line = f'{str(i).rjust(3)}|'
        for j in range(len(categories)):
            if rounded_withdraw_percents[j] >= i:
                line += ' '+'o'+' '
            else:
                line += '   '
        line += ' '
        chart_lines += "\n"+line
    
    # x-axis
    horizontal_line = '\n    '
    horizontal_line += '-' * (len(categories) * 3 + 1)

    # vetical labels along x-axis
    label_lines = ''
    max_category_len = max(len(cat.name) for cat in categories)
    
    for i in range(max_category_len):          # loop the max length of category name
        row = '\n    '
        for j in range(len(categories)):        # loop every category 
        
            if i < len(categories[j].name) :    # check the index is within the category name length
                row += f' {categories[j].name[i]} '
            else: 
                row += '   '
        row += ' '
        label_lines += row
    
    return f'''Percentage spent by category{chart_lines}{horizontal_line}{label_lines}'''

def round_down(num):
    return math.floor(num / 10) * 10
    
food = Category('Food')
food.deposit(1000,'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
clothing.deposit(1000,'initial deposit')
clothing.withdraw(10, '')
clothing.withdraw(10, '')
clothing.withdraw(10, '')

auto = Category('Auto')
auto.deposit(1000,'initial deposit')
auto.withdraw(10)
auto.withdraw(10)

food.transfer(50, auto)

print(food)
print(clothing)
print(auto)

categories = [food, clothing, auto]

print(create_spend_chart(categories))
