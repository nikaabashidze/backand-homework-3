class Car:

    def __init__(self, brand, model, production_year, color, horse_power, is_sport_car=False):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def production_year(self):
        return self.__production_year

    @property
    def color(self):
        return self.__color

    @property
    def horse_power(self):
        return self.__horse_power

    @property
    def is_sport_car(self):
        return self.__is_sport_car

    def change_color(self, new_color):
        if self.__color != new_color:
            self.__color = new_color
            return True
        return False

    def increase_horse_power(self, hp):
        if hp > 0:
            self.__horse_power += hp
            return True
        return False


car = Car("Chevrolet ", "Camaro", 1969, "Red", 290)


print (car.__dict__)


color_changed = car.change_color("black")
print("color changed","to" , car.color ,"-", color_changed ) 

color_changed = car.change_color("black")
print("color changed -" ,color_changed, ". because color is already", car.color) 

hp_increased = car.increase_horse_power(20)
print("hp increased to", car.horse_power,"-", hp_increased)  

hp_increased = car.increase_horse_power(-10)
print("hp increased -", hp_increased,". because hp <= 0 ")  
