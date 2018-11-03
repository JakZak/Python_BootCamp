class Employee:

    def __init__(self, imie, nazwisko, stawka):
        self.stawka = stawka
        self.imie = imie
        self.nazwisko = nazwisko
        self.time = 0
        self.nadgodziny = 0

    def register_time(self, time):
        self.time += time
        self.nadgodziny = self.time - 8

    def pay_salary(self):
        if self.nadgodziny > 0:
            to_pay = 8 * self.stawka + self.nadgodziny * 2 * self.stawka
        else:
            to_pay = self.time * self.stawka
        self.time = 0
        return to_pay

class PremiumEmployee(Employee):

    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus = bonus

    def pay_salary(self):
        to_pay = super().pay_salary()
        return to_pay + self.bonus

#Utworz klase comapny ktora inicjaluzuje sie nazwa.
#employee = Employee('Jan', 'Nowak', 100.0)
#employee.register_time(5)
#>>>google = company.('google')
#>>>google.add_employee(employee)
#>>>google.size()
#1
#>>>google.pay_all_salary()
#500
#>>>google.pay_all_salary()
#0
#>>>employee2 = Employee('Krzysztof', 'Nowak', 200.0)
#>>>employee.register_time(5)
#>>>google.add_employee(empployee)
#>>>google.pay_all_salary()
#1000

class company:

    def __init__(self, company):
        self.company = company
        self.company_size = 0

    def add_employee(self, employee):
        for company in self.company:
            company = set()
            company.add(employee)
    def company_size(self):
        self.company_size = len(self.company)

    def pay_all_salary(self):
        pass


    # @classmethod
    # def company_size(cls):
    #      cls.size_company += 1

#Utworz klase comapny ktora inicjaluzuje sie nazwa.
def test_company():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    google = company('google')
    google.add_employee(employee)
    assert google.size() == 1
    assert
1
>>>google.pay_all_salary()
500
>>>google.pay_all_salary()
0
>>>employee2 = Employee('Krzysztof', 'Nowak', 200.0)
>>>employee.register_time(5)
>>>google.add_employee(empployee)
>>>google.pay_all_salary()
1000










# def test_premiumemployee_z_bonusem():
#     employee = PremiumEmployee('Jan', 'Nowak', 100.0)
#     employee.register_time(5)
#     employee.give_bonus(1000.0)
#     assert employee.pay_salary() == 1500.0
#
# def test_pracownik():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     assert employee.imie == 'Jan'
#     assert employee.nazwisko == 'Nowak'
#     assert employee.stawka == 100.0
#
# def test_Employee():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     employee.register_time(5)
#     assert employee.pay_salary() == 500.0
#
# def test_bezgodzin():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     assert employee.pay_salary() == 0.0
#
# def test_nadgodziny():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     employee.register_time(10)
#     assert employee.pay_salary() == 8*100.0 + 2*2*100.0
#     assert employee.pay_salary() == 1200.0
#
# def test_wyplacania():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     employee.register_time(5)
#     assert employee.pay_salary() == 500.0
#     assert employee.pay_salary() == 0
#
# def test_nadgodziny__kilka_wpisow():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     employee.register_time(5)
#     employee.register_time(5)
#     assert employee.pay_salary() == 8*100.0 + 2*2*100.0
#     assert employee.pay_salary() == 1200.0
