class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer
        bank        the name of the bank
        acnt        the account number
        limit       credit limit
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return customer's name"""
        return self._customer

    def get_bank(self):
        """Return the bank's name"""
        return self._bank

    def get_account(self):
        """Return the card identifying number"""
        return self._account

    def get_limit(self):
        """Return current card's limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """Charge the given price to the card.

        Return True if charge was processed, False otherwise.
        """

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

    def __str__(self):
        """Returns a string representation of the card"""
        return "(" + self._customer + ", " + self._bank + ", " \
                + str(self._account) + ", " + str(self._balance) + ")"

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('Johnny', 'XYZ Bank', '2134543256939602', 10000))
    wallet.append(CreditCard('Kevin', 'ABC Bank', '8134543256939602', 10000))
    wallet.append(CreditCard('Jerie', 'IDC Bank', '6134543256939602', 10000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print(wallet[c])
        print("Customer =\t", wallet[c].get_customer())
        print("Bank =\t\t", wallet[c].get_bank())
        print("Account =\t", wallet[c].get_account())
        print("Limit =\t\t", wallet[c].get_limit())
        print("Balance =\t", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New balance =", wallet[c].get_balance())
        print()
