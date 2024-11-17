class Converter:

    changeTemperature = -20
    changeTime = .20

    def __init__(self, appliance, temperature, time):
        self.appliance = appliance
        self.temperature = temperature
        self.time = time

    @classmethod
    def convertToAirFryer(cls, temperature, time):
        newTemp = temperature + Converter.changeTemperature
        newTime = time * Converter.changeTime

        print(newTemp, newTime)



