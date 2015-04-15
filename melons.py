"""This file should have our melon-type classes in it."""


class Melon(object):
    """Find the comonalities and group under this parent class. """
 
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    base_cost = 5
    cost = 1

    def get_base_price (self):       

        if self.imported == True:
            self.cost = self.base_cost * 1.5
        elif self.shape == "square":
            self.cost = self.base_cost * 2
        else:
            self.cost = self.base_cost

        return self.cost         
  
    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty >= 3:
            self.cost = get_base_price(self) * .75
        if qty >= 5:
            self.cost = get_base_price(self) * .5

        total = qty * self.cost   # TODO, calculate the real amount!

        return total

class WatermelonOrder(Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    base_cost = 5

class CantaloupeOrder(Melon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    base_cost = 5

class CasabaOrder(Melon):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    base_cost = 6

class SharlynOrder(Melon):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    base_cost = 5

class SantaClausOrder(Melon):
    species = "SantaClaus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']
    base_cost = 5

class ChristmasOrder(Melon):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']
    base_cost = 5

class HornedMelonOrder(Melon):
    species = "Horned melons"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    base_cost = 5

class XiguaOrder(Melon):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']
    base_cost = 5

class OgenOrder(Melon):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring','Summer']
    base_cost = 6

w = WatermelonOrder()
print w.get_price(2)
HornedMelon = HornedMelonOrder()
Casaba = CasabaOrder()

print HornedMelon.get_price(2)
print Casaba.get_price(2)