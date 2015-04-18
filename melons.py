"""This file should have our melon-type classes in it."""

import datetime

class AbstractMelon(object):
    """Find the comonalities and group under this parent class. """
    
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def __init__(self):                                             # will raise an error if there is an attempt to create an instance of the base class
        
        if type(self) == AbstractMelon:
            raise Exception
    
    def is_available(self, month = datetime.date.today().month):    # will determine if the melon is available on a given date, or at today's date
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        current_month = months[month]
        seasons_dict = {'Winter': months[0:3], 'Spring': months [3:6], 'Summer': months[6:9], 'Fall': months[9:12] }
        for season in self.seasons:
            if current_month in seasons_dict[season]:
                return True
            else:
                return False
        
    def get_price(self, price_bump = 0):
        base_cost = 5
        price = base_cost + price_bump
        
        if self.shape == 'square':
            price = price * 2
        if self.imported == True:
            price = price * 1.5
            
        return price
        

class WatermelonOrder(AbstractMelon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_total(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_price() * qty

        if qty >= 3:
                total = total * .75

        return total

class CantaloupeOrder(AbstractMelon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_total(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_price() * qty

        if qty >= 5:
                total = total * .5

        return total

class CasabaOrder(AbstractMelon):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    price_bump = 1

    def get_total(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_price(self.price_bump) * qty

        return total

class SharlynOrder(AbstractMelon):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_total(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_price() * qty

        return total

class SantaClausOrder(AbstractMelon):
    species = "SantaClaus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_total(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_price() * qty

        return total

class ChristmasOrder(AbstractMelon):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_total(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_price() * qty

        return total

class HornedMelonOrder(AbstractMelon):
    species = "Horned melons"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_total(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_price() * qty

        return total

class XiguaOrder(AbstractMelon):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_total(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_price() * qty

        return total

class OgenOrder(AbstractMelon):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring','Summer']
    price_bump = 1

    def get_total(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_price(self.price_bump) * qty

        return total

w = WatermelonOrder()
print w.get_total(2)        # 10
print w.get_total(3)        # 11.25

c = CasabaOrder()
print c.get_total(2)        #18

h = HornedMelonOrder()
print h.get_total(2)        #15

x = XiguaOrder()
print x.get_total(1)        #15

q = OgenOrder()
print q.get_total(1)        #6
print q.price_bump          #1

print q.is_available()      #true

m = AbstractMelon()                 # Should trigger error

