from pathlib import Path
from entities.asiakas import Asiakas


class AsiakasRepository:

    def __init__(self, file_path):
        """finding file path for data saving"""
        self._file_path = file_path

    def find_all(self):
        """"print all data from file path"""
        return self._read()

    def find_customer(self, name):
        """print certain person from data file"""
        person = None
        customers = self.find_all()
        for customer in customers:
            if customer.name == name:
                person = customer

        return person

    def create(self, henkilo):
        """creating non used customer name to fund"""
        customers = self.find_all()

        for customer in customers:
            if customer.name == henkilo.name:
                print("Asiakas löytyy jo rahastosta")
                return henkilo

        customers.append(henkilo)

        self._write(customers)

        return henkilo

    def _ensure_file_exists(self):
        """self check for integrity of file path"""
        Path(self._file_path).touch()

    def _read(self):
        """reading data file and splitting data to list with [name,balance]
        "," is the divider of the data. and returning entire list"""
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
        """"reduce certain customer balance
        Args: 
            name: customer name who we pay
            amount: amount we pay to certain name
        """
        customers = self._read()
        for customer in customers:
            if customer.name == name:
                customer.balance = float(customer.balance) - amount
                break
        self._write(customers)

        return name

    def pay_all_money(self, name):
        """"remove certain customer from fund after paying his entire balance
        Args: 
            name: customer name
        """
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
        """count funds total balance"""
        customers = self.find_all()
        balance = 0
        for customer in customers:
            balance = balance + float(customer.balance)

        return balance

    def add_money(self, person):
        """adding balance for exisiting customer
        Args: 
            person: name, balance
        """
        customers = self.find_all()
        for customer in customers:
            if customer.name == person.name:
                customer.balance = float(customer.balance) + person.balance
                break
        self._write(customers)

        return person

    def _read_raw(self):
        rows = []
        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                rows.append(row)

        return rows

    def _write(self, customers):
        """write certain customer to data file
        Args: 
            list[customer], customer:name, balance
        """
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for customer in customers:

                name = customer.name
                amount = customer.balance

                row = f"{name},{amount}"

                file.write(row+"\n")

        return customers

    def delete_fund(self):
        """delete entire fund and data"""
        with open(self._file_path, "w", encoding="utf-8") as file:
            file.close()

        print("rahasto tyhjennetty")
