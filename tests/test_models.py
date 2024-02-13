#!/usr/bin/python3

import unittest
from backend.models.models import (
    City,
    County,
    Province,
    State,
    Continent,
    Suburb,
    Property,
    Review,
    Amenity,
    Place,
    Preference
)

class TestCityModel(unittest.TestCase):
    def test_city_creation(self):
        # Test city creation with valid data
        city = City(name="New York", state_id="12345")
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.state_id, "12345")

    def test_city_creation_invalid_data(self):
        # Test city creation with invalid data
        with self.assertRaises(ValueError):
            city = City(name=None, state_id="12345")

    def test_city_name_max_length(self):
        # Test maximum length of city name
        max_length = 255
        long_name = "a" * max_length
        city = City(name=long_name, state_id="12345")
        self.assertEqual(len(city.name), max_length)

    def test_city_name_type(self):
        # Test city name data type
        with self.assertRaises(TypeError):
            city = City(name=123, state_id="12345")

    def test_state_id_type(self):
        # Test state_id data type
        with self.assertRaises(TypeError):
            city = City(name="New York", state_id=None)

   
class TestCountyModel(unittest.TestCase):
    def test_county_creation(self):
        # Test county creation with valid data
        county = County(name="XYZ County", province_id="67890")
        self.assertEqual(county.name, "XYZ County")
        self.assertEqual(county.province_id, "67890")

    def test_county_creation_invalid_data(self):
        # Test county creation with invalid data
        with self.assertRaises(ValueError):
            county = County(name=None, province_id="54321")

    def test_county_name_max_length(self):
        # Test maximum length of county name
        max_length = 255
        long_name = "a" * max_length
        county = County(name=long_name, province_id="54321")
        self.assertEqual(len(county.name), max_length)

    def test_county_name_type(self):
        # Test county name data type
        with self.assertRaises(TypeError):
            county = County(name=123, province_id="54321")

    def test_province_id_type(self):
        # Test province_id data type
        with self.assertRaises(TypeError):
            county = County(name="Los Angeles", province_id=None)

class TestProvinceModel(unittest.TestCase):
    def test_province_creation(self):
        # Test province creation with valid data
        province = Province(name="ABC Province", country_id="54321")
        self.assertEqual(province.name, "ABC Province")
        self.assertEqual(province.country_id, "54321")

    def test_province_creation_invalid_data(self):
        # Test province creation with invalid data
        with self.assertRaises(ValueError):
            province = Province(name=None, country_id="12345")

    def test_province_name_max_length(self):
        # Test maximum length of province name
        max_length = 255
        long_name = "a" * max_length
        province = Province(name=long_name, country_id="12345")
        self.assertEqual(len(province.name), max_length)

    def test_province_name_type(self):
        # Test province name data type
        with self.assertRaises(TypeError):
            province = Province(name=123, country_id="12345")

    def test_country_id_type(self):
        # Test country_id data type
        with self.assertRaises(TypeError):
            province = Province(name="California", country_id=None)

class TestStateModel(unittest.TestCase):
    def test_state_creation(self):
        # Test state creation with valid data
        state = State(name="California", province_id="67890")
        self.assertEqual(state.name, "California")
        self.assertEqual(state.province_id, "67890")

    def test_state_creation_invalid_data(self):
        # Test state creation with invalid data
        with self.assertRaises(ValueError):
            state = State(name=None, province_id="12345")

    def test_state_name_max_length(self):
        # Test maximum length of state name
        max_length = 255
        long_name = "a" * max_length
        state = State(name=long_name, province_id="12345")
        self.assertEqual(len(state.name), max_length)

    def test_state_name_type(self):
        # Test state name data type
        with self.assertRaises(TypeError):
            state = State(name=123, province_id="12345")

    def test_province_id_type(self):
        # Test province_id data type
        with self.assertRaises(TypeError):
            state = State(name="California", province_id=None)

class TestContinentModel(unittest.TestCase):
    def test_continent_creation(self):
        # Test continent creation with valid data
        continent = Continent(name="North America")
        self.assertEqual(continent.name, "North America")

    def test_continent_creation_invalid_data(self):
        # Test continent creation with invalid data
        with self.assertRaises(ValueError):
            continent = Continent(name=None)

    def test_continent_name_max_length(self):
        # Test maximum length of continent name
        max_length = 255
        long_name = "a" * max_length
        continent = Continent(name=long_name)
        self.assertEqual(len(continent.name), max_length)

    def test_continent_name_type(self):
        # Test continent name data type
        with self.assertRaises(TypeError):
            continent = Continent(name=123)

class TestSuburbModel(unittest.TestCase):
    def test_suburb_creation(self):
        # Test suburb creation with valid data
        suburb = Suburb(name="Suburbia", city_id="12345")
        self.assertEqual(suburb.name, "Suburbia")
        self.assertEqual(suburb.city_id, "12345")

    def test_suburb_creation_invalid_data(self):
        # Test suburb creation with invalid data
        with self.assertRaises(ValueError):
            suburb = Suburb(name=None)

    def test_suburb_name_max_length(self):
        # Test maximum length of suburb name
        max_length = 255
        long_name = "a" * max_length
        suburb = Suburb(name=long_name)
        self.assertEqual(len(suburb.name), max_length)

    def test_suburb_name_type(self):
        # Test suburb name data type
        with self.assertRaises(TypeError):
            suburb = Suburb(name=123)


class TestPropertyModel(unittest.TestCase):
    def test_property_creation(self):
        # Test property creation with valid data
        property = Property(title="Cozy House", price=100000, bedrooms=2, bathrooms=1, area=100, address="123 Main St", city_id="12345", user_id="67890")
        self.assertEqual(property.title, "Cozy House")
        self.assertEqual(property.price, 100000)
        self.assertEqual(property.bedrooms, 2)
        self.assertEqual(property.bathrooms, 1)
        self.assertEqual(property.area, 100)
        self.assertEqual(property.address, "123 Main St")
        self.assertEqual(property.city_id, "12345")
        self.assertEqual(property.user_id, "67890")

    def test_property_creation_invalid_data(self):
        # Test property creation with invalid data
        with self.assertRaises(ValueError):
            property_data = {
                "title": None,
                "description": "This is a test property",
                "price": 100000,
                "bedrooms": 3,
                "bathrooms": 2,
                "area": 150.5,
                "address": "123 Test St",
                "city_id": "12345",
                "user_id": "54321"
            }
            property_obj = Property(**property_data)

    def test_property_price_negative(self):
        # Test property creation with negative price
        with self.assertRaises(ValueError):
            property_data = {
                "title": "Test Property",
                "description": "This is a test property",
                "price": -100000,
                "bedrooms": 3,
                "bathrooms": 2,
                "area": 150.5,
                "address": "123 Test St",
                "city_id": "12345",
                "user_id": "54321"
            }
            property_obj = Property(**property_data)

class TestReviewModel(unittest.TestCase):
    def test_review_creation(self):
        # Test review creation with valid data
        review = Review(text="Great place to stay", place_id="12345", user_id="67890")
        self.assertEqual(review.text, "Great place to stay")
        self.assertEqual(review.place_id, "12345")
        self.assertEqual(review.user_id, "67890")

    def test_review_creation_invalid_data(self):
        # Test review creation with invalid data
        with self.assertRaises(ValueError):
            review_data = {
                "text": None,
                "place_id": "123456",
                "user_id": "54321"
            }
            review_obj = Review(**review_data)

    def test_review_representation(self):
        # Test string representation of review object
        review_data = {
            "text": "This is a test review",
            "place_id": "123456",
            "user_id": "54321"
        }
        review_obj = Review(**review_data)
        expected_str = f"[Review] ({review_obj.id}) {{'text': 'This is a test review', 'place_id': '123456', 'user_id': '54321'}}"
        self.assertEqual(str(review_obj), expected_str)

    def test_review_save_method(self):
        # Test saving review object
        review_data = {
            "text": "This is a test review",
            "place_id": "123456",
            "user_id": "54321"
        }
        review_obj = Review(**review_data)
        review_obj.save()
        self.assertIsNotNone(review_obj.id)

class TestAmenityModel(unittest.TestCase):
    def test_amenity_creation(self):
        # Test amenity creation with valid data
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")

    def test_amenity_creation_invalid_data(self):
        # Test amenity creation with invalid data
        with self.assertRaises(ValueError):
            amenity_data = {
                "name": None
            }
            amenity_obj = Amenity(**amenity_data)

    def test_amenity_representation(self):
        # Test string representation of amenity object
        amenity_data = {
            "name": "Gym"
        }
        amenity_obj = Amenity(**amenity_data)
        expected_str = f"[Amenity] ({amenity_obj.id}) {{'name': 'Gym'}}"
        self.assertEqual(str(amenity_obj), expected_str)

    def test_amenity_save_method(self):
        # Test saving amenity object
        amenity_data = {
            "name": "Tennis Court"
        }
        amenity_obj = Amenity(**amenity_data)
        amenity_obj.save()
        self.assertIsNotNone(amenity_obj.id)

class TestPlaceModel(unittest.TestCase):
    def test_place_creation(self):
        # Test place creation with valid data
        place = Place(name="Cozy Cottage", description="A charming cottage in the countryside", number_rooms=2, number_bathrooms=1, max_guest=4, price_by_night=100, latitude=123.456, longitude=456.789, city_id="12345", user_id="67890")
        self.assertEqual(place.name, "Cozy Cottage")
        self.assertEqual(place.description, "A charming cottage in the countryside")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 123.456)
        self.assertEqual(place.longitude, 456.789)
        self.assertEqual(place.city_id, "12345")
        self.assertEqual(place.user_id, "67890")

    def test_place_creation_invalid_data(self):
        # Test place creation with invalid data
        with self.assertRaises(ValueError):
            place_data = {
                "name": None,
                "description": "A cozy apartment",
                "number_rooms": 2,
                "number_bathrooms": 1,
                "max_guest": 4,
                "price_by_night": 100,
                "latitude": 123.456,
                "longitude": -78.901,
                "city": self.city,
                "user": self.user
            }
            place_obj = Place(**place_data)

    def test_place_representation(self):
        # Test string representation of place object
        place_data = {
            "name": "Test Place",
            "description": "A cozy apartment",
            "number_rooms": 2,
            "number_bathrooms": 1,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 123.456,
            "longitude": -78.901,
            "city": self.city,
            "user": self.user
        }
        place_obj = Place(**place_data)
        expected_str = f"[Place] ({place_obj.id}) {{'name': 'Test Place', 'description': 'A cozy apartment'}}"
        self.assertEqual(str(place_obj), expected_str)

    def test_place_save_method(self):
        # Test saving place object
        place_data = {
            "name": "Test Place",
            "description": "A cozy apartment",
            "number_rooms": 2,
            "number_bathrooms": 1,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 123.456,
            "longitude": -78.901,
            "city": self.city,
            "user": self.user
        }
        place_obj = Place(**place_data)
        place_obj.save()
        self.assertIsNotNone(place_obj.id)

class TestPreferenceModel(unittest.TestCase):
    def test_preference_creation(self):
        # Test preference creation with valid data
        preference = Preference(user_id="67890", min_price=50, max_price=200, min_bedrooms=1, min_bathrooms=1, min_area=50, city_id="12345")
        self.assertEqual(preference.user_id, "67890")
        self.assertEqual(preference.min_price, 50)
        self.assertEqual(preference.max_price, 200)
        self.assertEqual(preference.min_bedrooms, 1)
        self.assertEqual(preference.min_bathrooms, 1)
        self.assertEqual(preference.min_area, 50)
        self.assertEqual(preference.city_id, "12345")

    def test_preference_creation_invalid_data(self):
        # Test preference creation with invalid data
        with self.assertRaises(ValueError):
            preference_data = {
                "user": self.user,
                "min_price": "1000.00",  # Price should be a float
                "max_price": 2000.00,
                "min_bedrooms": 2,
                "min_bathrooms": 1,
                "min_area": 100.00,
                "city": self.city,
                "amenities": [self.amenity]
            }
            preference_obj = Preference(**preference_data)

    def test_preference_representation(self):
        # Test string representation of preference object
        preference_data = {
            "user": self.user,
            "min_price": 1000.00,
            "max_price": 2000.00,
            "min_bedrooms": 2,
            "min_bathrooms": 1,
            "min_area": 100.00,
            "city": self.city,
            "amenities": [self.amenity]
        }
        preference_obj = Preference(**preference_data)
        expected_str = f"[Preference] ({preference_obj.id}) {{'user': '{self.user}', 'city': '{self.city}'}}"
        self.assertEqual(str(preference_obj), expected_str)

    def test_preference_save_method(self):
        # Test saving preference object
        preference_data = {
            "user": self.user,
            "min_price": 1000.00,
            "max_price": 2000.00,
            "min_bedrooms": 2,
            "min_bathrooms": 1,
            "min_area": 100.00,
            "city": self.city,
            "amenities": [self.amenity]
        }
        preference_obj = Preference(**preference_data)
        preference_obj.save()
        self.assertIsNotNone(preference_obj.id)

if __name__ == '__main__':
    unittest.main()
