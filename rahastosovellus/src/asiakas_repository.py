from pathlib import Path
from asiakas import Asiakas


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
                row = row.replace("\n", "")
                parts = row.split(",")
                
                name = parts[1]
                balance = parts[0]

                customers.append(
                    Asiakas(balance, name)
                )

        return customers
    
    def pay_money(self, name, amount):
        customers = self._read()
        for customer in customers:
            if customer.name == name:
                customer.balance = int(customer.balance) - amount
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
            balance = balance + int(customer.balance)
        
        return balance
    
    def add_money(self, person):
        customers = self.find_all()
        for customer in customers:
            if customer.name == person.name:
                customer.balance = int(customer.balance) + person.balance
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
