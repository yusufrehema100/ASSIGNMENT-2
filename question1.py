from abc import ABC, abstractmethod

# Step a: Create the abstract parent class
class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount  # Original base amount

    @abstractmethod
    def calculate_amount(self):
        pass


# Step b & c: Create the subclasses with their specific fee rules
class TuitionPayment(Payment):
    def calculate_amount(self):
        # 5% technology fee
        return self.amount * 1.05

class AccommodationPayment(Payment):
    def calculate_amount(self):
        # 10% service fee
        return self.amount * 1.10

class LibraryFine(Payment):
    def calculate_amount(self):
        # 2% admin fee
        return self.amount * 1.02


# Step d: Put the different payment objects into a single list
payment_list = [
    TuitionPayment(4500),
    AccommodationPayment(1500),
    LibraryFine(35)
]

print("--- Student Payment Report ---")

for p in payment_list:
    final_total = p.calculate_amount()
    name = p.__class__.__name__
    
    print("Type:", name)
    print("Original: $", p.amount)
    print("Final Total: $", round(final_total, 2))
    print("-" * 30)
