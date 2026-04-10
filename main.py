from population import (
    read_population_data,
    calculate_population_change,
    display_changes,
)


def main():
    filename="population.txt"
    data = read_population_data(filename)
    changes = calculate_population_change(data)
    display_changes(changes)


if __name__ == "__main__":
    main()
    