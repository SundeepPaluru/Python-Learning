class carMain:

    def get_car_type(self):
        carTypename = self
        return carTypename



carObj = carMain

carTypevalue = carObj.get_car_type("SUV")

print(f"Selected car type value is: {carTypevalue}")

