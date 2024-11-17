'''
OVEN => AIR FRYER
Temperature = Reduced by 20-30 degrees C
Time = Reduced by 20%
'''
class Converter:

    changeTemperature = 20
    changeTime = .20

    def __init__(self, appliance, temperature, time):
        self.appliance = appliance
        self.temperature = temperature
        self.time = time

    @classmethod
    def toString(cls, temperature, time):
        print("New temperature: {} C\nNew time: {} minutes".format(temperature, time))

    @classmethod
    def convertToAirFryer(cls, temperature, time):
        newTemp = temperature - Converter.changeTemperature
        newTime = time - (time * Converter.changeTime)

        Converter.toString(newTemp, newTime)
    
    @classmethod
    def convertToOven(cls, temperature, time):
        newTemp = temperature + Converter.changeTemperature
        newTime = time + (time * Converter.changeTime)

        Converter.toString(newTemp, newTime)

oven = Converter('oven', 220, 15)
Converter.convertToAirFryer(oven.temperature, oven.time)

airfryer = Converter('airfryer', 220, 20)
Converter.convertToOven(airfryer.temperature, airfryer.time)
