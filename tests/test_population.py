import pytest
from population import read_population_data, calculate_population_change

@pytest.fixture
def sample_data():
    return {
        "Ukraine": {2000: 49000000, 2010: 45900000, 2020: 41000000},
        "Poland": {2000: 38600000, 2010: 38500000, 2020: 37800000},
    }

@pytest.fixture
def sample_file(tmp_path):
    content = (
        "Ukraine, 2000, 49000000\n"
        "Ukraine, 2010, 45900000\n"
        "Poland, 2000, 38600000\n"
        "Poland, 2010, 38500000\n"
    )
    test_file = tmp_path / "test_population.txt"
    test_file.write_text(content, encoding="utf-8")
    return str(test_file)

def test_read_population_data(sample_file):
    data = read_population_data(sample_file)
    assert "Ukraine" in data
    assert data["Ukraine"][2000] == 49000000

@pytest.mark.parametrize("country, period, expected", [
    ("Ukraine", "2000-2010", -3100000),
    ("Ukraine", "2010-2020", -4900000),
    ("Poland", "2000-2010", -100000),
    ("Poland", "2010-2020", -700000),
])
def test_calculate_population_change_parametrized(sample_data, country, period, expected):
    changes = calculate_population_change(sample_data)
    assert changes[country][period] == expected