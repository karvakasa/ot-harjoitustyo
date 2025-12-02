from pathlib import Path
from entities.asiakas import Asiakas


class AsiakasRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        return self._read()

    def find_customer(self, name):
        person = None
        customers = self.find_all()
        for customer in customers:
            if customer.name == name:
                person = customer

        return person

    def create(self, henkilo):
        customers = self.find_all()

        for customer in customers:
            if customer.name == henkilo.name:
                print("Asiakas löytyy jo rahastosta")
                return henkilo

        customers.append(henkilo)

        self._write(customers)

        return henkilo

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        customers = []

        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                if len(row) == 0:
                    print("rahasto on tyhjä")
                else:
                    row = row.replace("\n", "")
                    parts = row.split(",")

                    name = parts[0]
                    balance = parts[1]

                    customers.append(Asiakas(name, balance))

        return customers

    def pay_money(self, name, amount):
        customers = self._read()
        for customer in customers:
            if customer.name == name:
                customer.balance = float(customer.balance) - amount
                break
        self._write(customers)

        return name

    def pay_all_money(self, name):
        customers = self._read()
        customers_without = []
        paid_customer = None
        for customer in customers:
            if customer.name != name:
                customers_without.append(customer)
            else:
                paid_customer = customer

        self._write(customers_without)

        return paid_customer

    def count_money(self):
        customers = self.find_all()
        balance = 0
        for customer in customers:
            balance = balance + float(customer.balance)

        return balance

    def add_money(self, person):
        customers = self.find_all()
        for customer in customers:
            if customer.name == person.name:
                customer.balance = float(customer.balance) + person.balance
                break
        self._write(customers)

        return person

    def _write(self, customers):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for customer in customers:

                name = customer.name
                amount = customer.balance

                row = f"{name},{amount}"

                file.write(row+"\n")

        return customers

    def delete_fund(self):
        with open(self._file_path, "w", encoding="utf-8") as file:
            file.close()

        print("rahasto tyhjennetty")
