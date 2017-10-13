"""Classes for melon orders."""
import random
import datetime


class AbstractMelonOrder(object):
    """Abstract for both domestic and international melon orders."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        """randomly get a base price between 5 and 9 and return it."""
        # in progress
        # day = datetime.date.weekday()
        # print day
        # time = datetime.time()
        # print time
        base_price = random.randint(5, 9)

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        if self.species == "Christmas":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        self.country_code = country_code
        return super(InternationalMelonOrder, self).__init__(species, qty)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3
        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """Special orders from the Government."""

    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        """Updates inspection status."""

        self.passed_inspection = passed
