#!/usr/bin/python3

import pytest
from backend.models.models import (
    City, County, Province, State, Continent, Suburb, Property, Review,
    Amenity, Place, Preference
)

# Test City Model
def test_city_creation():
    city = City(name="New York", state_id="12345")
    assert city.name == "New York"
    assert city.state_id == "12345"

def test_city_creation_invalid_data():
    with pytest.raises(ValueError):
        City(name=None, state_id="12345")

def test_city_name_max_length():
    max_length = 255
    long_name = "a" * max_length
    city = City(name=long_name, state_id="12345")
    assert len(city.name) == max_length

def test_city_name_type():
    with pytest.raises(TypeError):
        City(name=123, state_id="12345")

def test_state_id_type():
    with pytest.raises(TypeError):
        City(name="New York", state_id=None)

# Test County Model
def test_county_creation():
    county = County(name="XYZ County", province_id="67890")
    assert county.name == "XYZ County"
    assert county.province_id == "67890"

def test_county_creation_invalid_data():
    with pytest.raises(ValueError):
        County(name=None, province_id="54321")

def test_county_name_max_length():
    max_length = 255
    long_name = "a" * max_length
    county = County(name=long_name, province_id="54321")
    assert len(county.name) == max_length

def test_county_name_type():
    with pytest.raises(TypeError):
        County(name=123, province_id="54321")

def test_province_id_type():
    with pytest.raises(TypeError):
        County(name="Los Angeles", province_id=None)

# Test Province Model
def test_province_creation():
    province = Province(name="ABC Province", country_id="54321")
    assert province.name == "ABC Province"
    assert province.country_id == "54321"

def test_province_creation_invalid_data():
    with pytest.raises(ValueError):
        Province(name=None, country_id="12345")

def test_province_name_max_length():
    max_length = 255
    long_name = "a" * max_length
    province = Province(name=long_name, country_id="12345")
    assert len(province.name) == max_length

def test_province_name_type():
    with pytest.raises(TypeError):
        Province(name=123, country_id="12345")

def test_country_id_type():
    with pytest.raises(TypeError):
        Province(name="California", country_id=None)

# Test State Model
def test_state_creation():
    state = State(name="California", province_id="67890")
    assert state.name == "California"
    assert state.province_id == "67890"

def test_state_creation_invalid_data():
    with pytest.raises(ValueError):
        State(name=None, province_id="12345")

def test_state_name_max_length():
    max_length = 255
    long_name = "a" * max_length
    state = State(name=long_name, province_id="12345")
    assert len(state.name) == max_length

def test_state_name_type():
    with pytest.raises(TypeError):
        State(name=123, province_id="12345")

def test_province_id_type():
    with pytest.raises(TypeError):
        State(name="California", province_id=None)

# Test Continent Model
def test_continent_creation():
    continent = Continent(name="North America")
    assert continent.name == "North America"

def test_continent_creation_invalid_data():
    with pytest.raises(ValueError):
        Continent(name=None)

def test_continent_name_max_length():
    max_length = 255
    long_name = "a" * max_length
    continent = Continent(name=long_name)
    assert len(continent.name) == max_length

def test_continent_name_type():
    with pytest.raises(TypeError):
        Continent(name=123)

# Test Suburb Model
def test_suburb_creation():
    suburb = Suburb(name="Suburbia", city_id="12345")
    assert suburb.name == "Suburbia"
    assert suburb.city_id == "12345"

def test_suburb_creation_invalid_data():
    with pytest.raises(ValueError):
        Suburb(name=None)

def test_suburb_name_max_length():
    max_length = 255
    long_name = "a" * max_length
    suburb = Suburb(name=long_name)
    assert len(suburb.name) == max_length

def test_suburb_name_type():
    with pytest.raises(TypeError):
        Suburb(name=123)

# Test Property Model
def test_property_creation():
    property = Property(title="Cozy House", price=100000, bedrooms=2,
                        bathrooms=1, area=100, address="123 Main St",
                        city_id="12345", user_id="67890")
    assert property.title == "Cozy House"
    assert property.price == 100000
    assert property.bedrooms == 2
    assert property.bathrooms == 1
    assert property.area == 100
    assert property.address == "123 Main St"
    assert property.city_id == "12345"
    assert property.user_id == "67890"

def test_property_creation_invalid_data():
    with pytest.raises(ValueError):
        Property(title=None, price=100000, bedrooms=3, bathrooms=2,
                 area=150.5, address="123 Test St", city_id="12345",
                 user_id="54321")

def test_property_price_negative():
    with pytest.raises(ValueError):
        Property(title="Test Property", price=-100000, bedrooms=3,
                 bathrooms=2, area=150.5, address="123 Test St",
                 city_id="12345", user_id="54321")

# Test Review Model
def test_review_creation():
    review = Review(text="Great place to stay", place_id="12345",
                    user_id="67890")
    assert review.text == "Great place to stay"
    assert review.place_id == "12345"
    assert review.user_id == "67890"

def test_review_creation_invalid_data():
    with pytest.raises(ValueError):
        Review(text=None, place_id="123456", user_id="54321")

def test_review_representation():
    review = Review(text="This is a test review", place_id="123456",
                    user_id="54321")
    expected_str = f"[Review] ({review.id}) {{'text': 'This is a test review', 'place_id': '123456', 'user_id': '54321'}}"
    assert str(review) == expected_str

def test_review_save_method():
    review = Review(text="This is a test review", place_id="123456",
                    user_id="54321")
    review.save()
    assert review.id is not None

# Test Amenity Model
def test_amenity_creation():
    amenity = Amenity(name="WiFi")
    assert amenity.name == "WiFi"

def test_amenity_creation_invalid_data():
    with pytest.raises(ValueError):
        Amenity(name=None)

def test_amenity_representation():
    amenity = Amenity(name="Gym")
    expected_str = f"[Amenity] ({amenity.id}) {{'name': 'Gym'}}"
    assert str(amenity) == expected_str

def test_amenity_save_method():
    amenity = Amenity(name="Tennis Court")
    amenity.save()
    assert amenity.id is not None

# Test Place Model
def test_place_creation():
    place = Place(name="Cozy Cottage",
                  description="A charming cottage in the countryside",
                  number_rooms=2, number_bathrooms=1, max_guest=4,
                  price_by_night=100, latitude=123.456, longitude=456.789,
                  city_id="12345", user_id="67890")
    assert place.name == "Cozy Cottage"
    assert place.description == "A charming cottage in the countryside"
    assert place.number_rooms == 2
    assert place.number_bathrooms == 1
    assert place.max_guest == 4
    assert place.price_by_night == 100
    assert place.latitude == 123.456
    assert place.longitude == 456.789
    assert place.city_id == "12345"
    assert place.user_id == "67890"

def test_place_creation_invalid_data():
    with pytest.raises(ValueError):
        Place(name=None, description="A cozy apartment", number_rooms=2,
              number_bathrooms=1, max_guest=4, price_by_night=100,
              latitude=123.456, longitude=-78.901, city="Test City",
              user="Test User")

def test_place_representation():
    place = Place(name="Test Place", description="A cozy apartment",
                  number_rooms=2, number_bathrooms=1, max_guest=4,
                  price_by_night=100, latitude=123.456, longitude=-78.901,
                  city="Test City", user="Test User")
    expected_str = f"[Place] ({place.id}) {{'name': 'Test Place', 'description': 'A cozy apartment'}}"
    assert str(place) == expected_str

def test_place_save_method():
    place = Place(name="Test Place", description="A cozy apartment",
                  number_rooms=2, number_bathrooms=1, max_guest=4,
                  price_by_night=100, latitude=123.456, longitude=-78.901,
                  city="Test City", user="Test User")
    place.save()
    assert place.id is not None

# Test Preference Model
def test_preference_creation():
    preference = Preference(user_id="67890", min_price=50, max_price=200,
                             min_bedrooms=1, min_bathrooms=1, min_area=50,
                             city_id="12345")
    assert preference.user_id == "67890"
    assert preference.min_price == 50
    assert preference.max_price == 200
    assert preference.min_bedrooms == 1
    assert preference.min_bathrooms == 1
    assert preference.min_area == 50
    assert preference.city_id == "12345"

def test_preference_creation_invalid_data():
    with pytest.raises(ValueError):
        Preference(user="Test User", min_price="1000.00", max_price=2000.00,
                    min_bedrooms=2, min_bathrooms=1, min_area=100.00,
                    city="Test City", amenities=["Test Amenity"])

def test_preference_representation():
    preference = Preference(user="Test User", min_price=1000.00,
                             max_price=2000.00, min_bedrooms=2, min_bathrooms=1,
                             min_area=100.00, city="Test City",
                             amenities=["Test Amenity"])
    expected_str = f"[Preference] ({preference.id}) {{'user': 'Test User', 'city': 'Test City'}}"
    assert str(preference) == expected_str

def test_preference_save_method():
    preference = Preference(user="Test User", min_price=1000.00,
                             max_price=2000.00, min_bedrooms=2, min_bathrooms=1,
                             min_area=100.00, city="Test City",
                             amenities=["Test Amenity"])
    preference.save()
    assert preference.id is not None

