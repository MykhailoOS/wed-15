# Task 2
# Створіть абстрактний базовий клас "ПлатіжнийЗасіб" з методом "здійснити_платіж()". Створіть підкласи "КредитнаКарта", "БанківськийПереказ", "ЕлектроннийГаманець" і т.д., які успадковують цей метод та реалізовують його відповідно до специфіки кожного платіжного засобу. Створіть клас "ПлатіжнийПроцесор", який містить список доступних платіжних засобів та метод для виконання платежу через вибраний засіб. Можна створити об'єкти різних платіжних засобів, додати їх до платіжного процесора і здійснити платежі через них
from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self):
        ...


class CreditCard(PaymentMethod):
    def __init__(self, name_id):
        self.name_id = name_id

    def pay(self):
        return f"{self.name_id} payed.\nPayment method: credit"


class BankTransfer(PaymentMethod):
    def __init__(self, name_id):
        self.name_id = name_id

    def pay(self):
        return f"{self.name_id} payed.\nPayment method: BankTransfer"


class AppPayment(PaymentMethod):
    def __init__(self, name_id):
        self.name_id = name_id

    def pay(self):
        return f"{self.name_id} payed.\nPayment method: AppPayment"


class PayProcess():
    def __init__(self, method):
        self.method = method

    def pay_status(self):
        return f"User: {self.method}"


x = PayProcess(AppPayment("Vasiliy").pay())
print(x.pay_status())
