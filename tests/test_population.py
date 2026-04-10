import pytest
from population import read_population_data, calculate_population_change

@pytest.fixture
def sample_data():
    return {
        "Ukraine": {2000: 49000000, 2010: 45900000, 2020: 41000000},
        "Poland": {2000: 38600000, 2010: 38500000, 2020: 37800000},
    }