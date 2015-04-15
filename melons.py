"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    base_cost = 5


    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if self.imported == True:
            self.cost = self.base_cost * 1.5
        elif self.shape == "square":
            self.cost = self.base_cost * 2
        else:
            self.cost = self.base_cost


        if qty >= 3:
            self.cost = self.cost * .75
        if qty >= 5:
            self.cost = self.cost * .5

        total = qty * self.cost   # TODO, calculate the real amount!

        return total

Watermelon = WatermelonOrder()
Cantaloupe = WatermelonOrder()
Casaba = WatermelonOrder()
Sharlyn = WatermelonOrder()
SantaClaus = WatermelonOrder()
Christmas = WatermelonOrder()
HornedMelon = WatermelonOrder()
Xigua = WatermelonOrder()
Ogen = WatermelonOrder()

Cantaloupe.color = "tan"
Casaba.color = "green"
Sharlyn.color = "tan"
SantaClaus.color = "green"
HornedMelon.color = "yellow"
Xigua.color = "black"
Ogen.color = "tan" 

Casaba.imported = True
Sharlyn.imported = True
SantaClaus.imported = True
HornedMelon.imported = True
Xigua.imported = True

Xigua.shape = "square"

Cantaloupe.seasons =["Spring", "Summer"]
Casaba.seasons = ["Spring", "Summer", "Fall", "Winter"]
Sharlyn.seasons = ["Summer"]
SantaClaus.seasons = ["Winter", "Spring"]
Christmas.seasons = ["Winter", "Spring"]
HornedMelon.seasons = ["Summer"]
Xigua.seasons = ["Summer"]
Ogen.seasons = ["Spring", "Summer"]

Casaba.base_cost = Casaba.base_cost + 1
Ogen.base_cost = Ogen.base_cost + 1


print HornedMelon.get_price(2)
print Casaba.get_price(2)
