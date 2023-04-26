#from tabulate import tabulate
class Payment:
    def __init__(self, name):
        self.name = name
        self.payment_list = []
        self.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    def add_payment(self, pay_amount):
        self.payment_list.append(pay_amount)
    def print_paylist(self):
        # print(self.name, "'s payment list:")
        # table = [["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], self.payment_list]
        # print(tabulate(table))
        pass

    @classmethod
    def read_from_database(cls, payment_filename):
        pass
