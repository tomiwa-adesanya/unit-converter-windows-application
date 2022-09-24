class UnitConverter():
    def __init__(self):

        self.quantities = [
            "length", "area", "volume", "mass", "time", "temperature",
            "energy", "frequency", "pressure", "speed", "plane_angle",
            "fuel_economy", "data_transfer_rate", "digital_storage",
        ]

        #---------------------------------------------------------------------------
        self.__init_conversion_factors()
        self.__init_quantity_units()

    def __init_quantity_units(self):

        self.length_units = list(self.length_in_meters.keys())
        self.area_units = list(self.area_in_sqm.keys())

    def __init_conversion_factors(self):

        self.length_in_meters = { # With respect to meter as the standard
            "meter" : 1,
            "kilometer" : 0.001, 
            "centimeter" : 100,
            "millimeter" : 1000, 
            "micrometer" : 1e+6,
            "nanometer" : 1e+9, 
            "mile" : 0.000621371,
            "yard" : 1.09361,
            "foot" : 3.28084,
            "inch" : 39.3701,
            "nautical_mile" : 0.000539957,
        }

        self.area_in_sqm = {
            "square_meter" : 1,
            "square_kilometer" : 1e-6,
            "square_mile" : 3.861e-7, 
            "square_yard" : 1.19599,
            "square_foot" : 10.7639,
            "square_inch" : 1550,
            "hectare" : 1e-4,
            "acre" : 0.000247105
        }

        self.volume_in_liter = {
            "liter" : 1,
            "milliliter" : 1000,
            "us_liquid_gallon" : 0.264172,
            "us_liquid_quart" : 1.05569,
            "us_liquid_pint" : 2.11338,
            "us_legal_cup" : 4.16667,
            "fluid_ounce" : 33.814,
            "us_tablespoon" : 67.628,
            "us_teaspoon" : 202.884, 
            "cubic_meter" : 0.001,
            "imperial_gallon" : 0.219969,
            "imperial_quart" : 0.879877,
            "imperial_pint" : 1.75975,
            "imperial_cup" : 3.51951,
            "imperial_tablespoon" : 56.3121,
            "imperial_teaspoon" : 168.936,
            "cubic_foot" : 0.0353147,
            "cubic_inch" : 61.0237,
        }

        self.mass_in_gram = {
            "gram" : 1,
            "tonne" : 1e-6,
            "kilogram" : 0.001,
            "milligram" : 1000,
            "microgram" : 1e+6,
            "imperial_ton" : 9.8421e-7,
            "us_ton" : 1.1023e-6,
            "stone" : 0.000157473,
            "pound" : 0.00220462,
            "ounce" : 0.035274,
        }

        self.time_in_seconds = {
            "second" : 1,
            "nanosecond" : 1e+9, 
            "microsecond" : 1e+6,
            "millisecond" : 1000,
            "minute" : 0.0166667,
            "hour" : 0.000277778,
            "day" : 1.1574e-5,
            "week" : 1.6534e-6,
            "month" : 3.8052e-7,
            "calendar_year" : 3.171e-8,
            "decade" : 3.171e-9,
            "century" : 3.171e-10
        }

        self.energy_in_joule = {
            "joule" : 1,
            "kilejoule" : 0.001,
            "gram_calorie" : 0.239006,
            "kilo_calorie" : 0.000239006,
            "watt_hour" : 0.000277778,
            "kilowatt_hour" : 2.7778e-7,
            "electronvolt" : 6.242e+18,
            "british_thermal_unit" : 0.000947817,
            "us_therm" : 9.4804e-9,
            "foot_pound" : 0.737562,
        }

        self.frequency_in_hertz = {
            "hertz" : 1,
            "kilohertz" : 0.001, 
            "megahertz" : 1e-6,
            "gigahertz" : 1e-9,
        }

        self.pressure_in_pascal = {
            "pascal" : 1, 
            "kilopascal" : 0.001,
            "millimeter_of_mercury" : 0.007502,
            "bar" : 1e-5,
            "pound_per_square_inch" : 0.000145038,
            "standard_atmosphere" : 9.8692e-6, 
            "torr" : 0.00750062,
        }

        self.speed_in_knot = {
            "knot" : 1,
            "mach" : 0.001512,
            "miles_per_hour" : 1.15078,
            "foot_per_second" : 1.68781,
            "centimeter_per_second" : 51.44,
            "meter_per_second" : 0.514444,
            "kilometer_per_hour" : 1.852,
        }

        self.plane_angle_in_degree = {
            "degree" : 1,
            "radian" : 0.0174533,
            "gradian" : 1.11111,
            "milliradian" : 17.4533,
            "minute_of_arc" : 60,
            "second_of_arc" : 3600,
        }

        self.fuel_economy_in_mipga = { # mipga = Miles per Gallon
            "miles_per_gallon" : 1,
            "miles_per_gallon_(imperial)" : 1.20095,
            "kilometer_per_liter" : 0.425144,
            "liter_per_100_kilometers" : 235.215
        }

        self.data_transfer_rate_in_bitps = { # bitps = Bit per second
            "bit_per_second" : 1,
            "kilobit_per_second" : 0.001,
            "kilobyte_per_second" : 0.000125,
            "kibibit_per_second" : 0.000976563,
            "megabit_per_second" : 1e-6, 
            "megabyte_per_second" : 1.25e-7,
            "mebibit_per_second" : 9.5367e-7, 
            "gigabit_per_second" : 1e-9, 
            "gigabyte_per_second" : 1.25e-10, 
            "gibibit_per_second" : 9.3132e-10, 
            "terabit_per_second" : 1e-12, 
            "terabyte_per_second" : 1.25e-13, 
            "tebibit_per_second" : 9.0949e-13
        }

        self.digital_storage_in_bit = {
            "bit" : 1,
            "kilobit" : 0.001,
            "kibibit" : 0.000976563,
            "megabit" : 1e-6,
            "mebibit" : 9.5367e-7,
            "gigabit" : 1e-9,
            "gibibit" : 9.3132e-10,
            "terabit" : 1e-12,
            "tebibit" : 9.0949e-13,
            "petabit" : 1e-15,
            "pebibit" : 8.8818e-16,
            "byte" : 0.125,
            "kilobyte" : 0.000125,
            "kibibyte" : 0.00012207,
            "megabyte" : 1.25e-7,
            "mebibyte" : 1.1921e-7,
            "gigabyte" : 1.25e-10,
            "gibibyte" : 1.1642e-10,
            "terabyte" : 1.25e-13,
            "tebibyte" : 1.1369e-13,
            "petabyte" : 1.25e-16,
            "pebibyte" : 1.1102e-16
        }

        #-------------------------------------------------------------
        self.factors = {
            "length" : self.length_in_meters,
            "area" : self.area_in_sqm,
            "volume" : self.volume_in_liter,
            "mass" : self.mass_in_gram,
            "time" : self.time_in_seconds,
            "energy" : self.energy_in_joule,
            "frequency" : self.frequency_in_hertz,
            "pressure" : self.pressure_in_pascal,
            "speed" : self.speed_in_knot, 
            "plane_angle" : self.plane_angle_in_degree,
            "fuel_economy" : self.fuel_economy_in_mipga,
            "data_transfer_rate" : self.data_transfer_rate_in_bitps,
            "digital_storage" : self.digital_storage_in_bit
        }

    def _convert(self, quantity:str, value: float|int, _from: str, _to: str) -> float | int:

        if (quantity == "temperature"):
            return self._convert_temperature(
                value=value, _from=_from, _to=_to
            )

        factors = self.factors.get(quantity)

        if (factors):
            _to_standard = (1/factors.get(_from)) * value
            _to_final = factors.get(_to) * _to_standard

            return _to_final 
        else: 
            raise ValueError(
                f"Quantity : '{quantity}' not recognized"
            )
    
    def _convert_temperature(self, value: float|int, _from: str, _to: str) -> float | int:
        
        if ((_from == "celsius") and (_to == "fahrenheit")):
            _to_final = (value * 9/5) + 32
            return _to_final
        elif ((_from == "fahrenheit") and (_to == "celsius")):
            _to_final = (value - 32) * 9/5
            return _to_final
        elif ((_from == "celsius") and (_to == "kelvin")):
            _to_final = value + 273.15
            return _to_final
        elif ((_from == "fahrenheit") and (_to == "kelvin")): 
            _to_final = self._convert_temperature(value, _from="fahrenheit", _to="celsius") + 273.15
            return _to_final
        else:
            raise ValueError(
                f"Temperature unit not recognized"
            )




if __name__ == "__main__":
    unit = UnitConverter()
    final = unit._convert("length", 55, _from="nanometer", _to="micrometer")
    print(final)