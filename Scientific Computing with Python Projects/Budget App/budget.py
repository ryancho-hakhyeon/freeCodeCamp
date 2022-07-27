class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self._balance = 0.0

    def __repr__(self):
        header = self.description.center(30, "*") + "\n"
        res = ""
        for item in self.ledger:
            described = "{:<23}".format(item["description"])
            balance = "{:>7.2f}".format(item["amount"])
            res += "{}{}".format(described[:23], balance[:7]) + "\n"

        total = "Total: {:.2f}".format(self._balance)

        return header + res + total

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self._balance += amount

    def withdraw(self, amount, description=""):
        if self._balance - amount >= 0:
            self.ledger.append({"amount": -1*amount, "description": description})
            self._balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self._balance

    def transfer(self, transfer_amount, category):
        if self.withdraw(transfer_amount, f"Transfer to {category.description}"):
            category.deposit(transfer_amount, f"Transfer from {self.description}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self._balance >= amount:
            return True
        else:
            return False


def create_spend_chart(categories):
    res = []
    description = []
    head = "Percentage spent by category" + "\n"

    for category in categories:
        description.append(category.description)
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        res.append(round(spent, 2))

    total_spent = sum(res)

    spent_percentage = [int(n / total_spent * 10) * 10 for n in res]

    header = "Percentage spent by category\n"

    chart = ""

    for n in range(100, -1, -10):
        chart += str(n).rjust(3) + '|'
        for percentage in spent_percentage:
            if percentage >= n:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    divided = "    " + ("-" * ((3 * len(spent_percentage)) + 1)) + '\n'

    maxLen = 0
    for name in description:
        maxLen = max(maxLen, len(name))

    new_des = []
    for name in description:
        new_des.append(name.ljust(maxLen))

    category_name = ""
    for i in range(len(new_des[0])):
        category_name += "   "
        for j in range(len(new_des)):
            category_name += "  " + new_des[j][i]
        category_name += "  " + '\n'

    return (header + chart + divided + category_name).rstrip('\n')




