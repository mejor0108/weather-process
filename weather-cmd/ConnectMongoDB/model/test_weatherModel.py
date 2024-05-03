import unittest
from weatherModel import WeatherModel

class TestWeatherModel(unittest.TestCase):
    def test_str_method(self):
        weather = WeatherModel()
        weather._estacion = "Station 1"
        # Set other parameters as needed
        
        expected_output = "estación : Station 1\n"  # Update with expected output
        
        self.assertEqual(str(weather), expected_output)

if __name__ == '__main__':
    unittest.main()