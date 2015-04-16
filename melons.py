"""This file should have our melon-type classes in it."""


class Melon(object):
    """Find the comonalities and group under this parent class. """
 
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_base_price (self):       
        return 5.00        

class WatermelonOrder(Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_base_price() * qty

        if qty >= 3:
                total = total * .75

        return total

class CantaloupeOrder(Melon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_base_price() * qty

        if qty >= 5:
                total = total * .5
       # TODO, calculate the real amount!

        return total

class CasabaOrder(Melon):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = ((self.get_base_price() + 1)*1.5) * qty

        return total

class SharlynOrder(Melon):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = (self.get_base_price()*1.5) * qty

        return total

class SantaClausOrder(Melon):
    species = "SantaClaus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = (self.get_base_price()*1.5) * qty

        return total

class ChristmasOrder(Melon):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_base_price() * qty

        return total

class HornedMelonOrder(Melon):
    species = "Horned melons"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = (self.get_base_price()*1.5) * qty

        return total

class XiguaOrder(Melon):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = ((self.get_base_price()*1.5)*2.0) * qty

        return total

class OgenOrder(Melon):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring','Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = (self.get_base_price()+1) * qty

        return total

w = WatermelonOrder()
print w.get_base_price()
print w.get_price(2)

Casaba = CasabaOrder()
HornedMelon = HornedMelonOrder()

print Casaba.get_price(2)
print HornedMelon.get_price(2)