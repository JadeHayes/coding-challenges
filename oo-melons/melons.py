"""Classes for melon orders."""


class AbsrtractMelonClass(object):
    """An abstract class for melons"""

    def __init__(self, species, order_type, qty):
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species == "Christmas melon":
            base_price *= 1.5
        
        if self.quantity < 10:
            base_price += 3

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class GovernmentMelonOrder(AbsrtractMelonClass):

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species,
                                                   qty, "government",
                                                   0.0)
        self.passed_inspection = False


    def marked_inspection(self, passed):
        """Records if the melon passed inspection or not"""
        self.passed_inspection = passed



class DomesticMelonOrder(AbsrtractMelonClass):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty,
                                                 "domestic", 0.08)


class InternationalMelonOrder(AbsrtractMelonClass):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty,
                                                      "international",
                                                      0.17)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
