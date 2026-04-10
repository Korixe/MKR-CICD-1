from population import read_population_data, calculate_population_change, display_changes

def main():
    filename = "population.txt"
    population_data = read_population_data(filename)

    if population_data:
        changes = calculate_population_change(population_data)

    display_changes(changes)

if __name__ == "__main__":
    main()