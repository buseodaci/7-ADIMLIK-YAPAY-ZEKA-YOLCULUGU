# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:57:43 2020

@author: buse
"""

import datetime


class VehicleRent:
    def __init__(self, stock):
        self.stock = stock
        self.now = 0

    def displayStock(self):
        print("{} vehicle available to rent".format(self.stock))
        return self.stock

    def rentHourly(self, n):
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicle to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours".format(n, self.now.hour))
            self.stock -= n
            return self.now

    def rentDaily(self, n):
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicle to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours".format(n, self.now.hour))
            self.stock -= n
            return self.now

    def returnVehicle(self, request, brand):
        car_h_price = 10
        car_d_price = car_h_price * 8 / 10 * 24
        bike_h_price = 5
        bike_d_price = bike_h_price * 7 / 10 * 24

        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0
        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                if rentalBasis == 1:
                    bill = rentalPeriod.seconds / 3600 * car_h_price * numOfVehicle
                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds / (3600 * 24) * car_d_price * numOfVehicle
                if (2 <= numOfVehicle):
                    print("You have extra 20% discount!")
                    bill = bill * 0.8
                print("Thank you for returning your car")
                print("Price: $ {}".format(bill))
                return bill
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                if rentalBasis == 1:
                    bill = rentalPeriod.seconds / 3600 * bike_h_price * numOfVehicle
                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds / (3600 * 24) * bike_d_price * numOfVehicle
                if (4 <= numOfVehicle):
                    print("You have extra 20% discount!")
                    bill = bill * 0.8
                print("Thank you for returning your bike")
                print("Price: $ {}".format(bill))
                return bill

            else:
                print("You dont rent a vehicle")
                return None


class CarRent(VehicleRent):

    def __init__(self, stock):
        super().__init__(stock)

    def discount(self, b):
        bill = b - (b * 15) / 100
        return bill


class BikeRent(VehicleRent):
    def __init__(self, stock):
        super().__init__(stock)


class Customer:
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0

        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0

    def requestVehicle(self, brand):
        if brand == "bike":
            bikes = input("How many bikes would you like to rent? :")
            try:
                bikes = int(bikes)
            except ValueError:
                print("Input should be number")
                return -1

            if bikes < 1:
                print("Number of bikes should be greater than zero")
                return -1
            else:
                self.bikes = bikes
            return self.bikes

        elif brand == "car":
            cars = input("How many cars would you like to rent? :")
            try:
                cars = int(cars)
            except ValueError:
                print("Input should be number")
                return -1

            if bikes < 1:
                print("Number of cars should be greater than zero")
                return -1
            else:
                self.cars = cars
            return self.cars
        else:
            print("Request vehicle error")

    def returnVehicle(self, brand):
        if brand == "bike":
            if self.rentalBasis_b and self.rentalTime_b and self.bikes:
                return self.rentalBasis_b and self.rentalTime_b and self.bikes
            else:
                return 0, 0, 0
        elif brand == "cars":
            if self.rentalBasis_c and self.rentalTime_c and self.cars:
                return self.rentalBasis_c and self.rentalTime_c and self.cars
            else:
                return 0, 0, 0
        else:
            print("Return vehicle error")
