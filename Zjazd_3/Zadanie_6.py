class CashMachine:

    def __init__(self):
        self.amount = []
        self.withdraw = []

    def put_money(self, amount):
        self.amount += amount
        return self.amount

    def is_available(self):
        return bool(self.amount)

    def withdraw_money(self, withdraw):
        total_withdraw = []
        for bill in sorted(self.amount, reverse = True):
            if sum(total_withdraw) + bill <= withdraw:
                total_withdraw.append(bill)
        if sum(total_withdraw) == withdraw:
            for bill in total_withdraw:
                self.amount.remove(bill)
            return total_withdraw
        return []



def test_cash_machine_is_available():
    cash_machine = CashMachine()
    assert not cash_machine.is_available()

def test_cash_machine_is_available_put_money():
    cash_machine = CashMachine()
    assert cash_machine.put_money([100, 200, 50, 10, 30, 50]) == ([100, 200, 50, 10, 30, 50])
    assert cash_machine.put_money([10, 20, 30]) == ([100, 200, 50, 10, 30, 50, 10, 20, 30])

def test_cash_machine_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == ([100, 50])

def test_cash_machine_order_matter():
    cash_machine = CashMachine()
    cash_machine.put_money([20, 20, 50, 50])
    assert cash_machine.withdraw_money(100) == ([50, 50])




# cash_machine.is_available
# False
# cash_machine.put_money([100, 100, 100, 50])
# cash_machine.is_available
# True
# cash_machine.withdraw_money(150)
# [100,50]