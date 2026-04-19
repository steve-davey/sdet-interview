import pytest

# Creating the value for base_url
@pytest.fixture
def base_url():
   base_url = "https://jsonplaceholder.typicode.com"
   return base_url