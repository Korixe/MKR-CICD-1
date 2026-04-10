def read_population_data(filename):
    data = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                country, year, population = line.split(",")
                country = country.strip()
                year = int(year.strip())
                population = int(population.strip())

                if country not in data:
                    data[country] = {}

                data[country].append({"year": year, "population": population})
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    
    return data

def calculate_population_change(data):
    changes = {}
    for country, years in data.items():

        sorted_years = sorted(years.keys())
        changes[country] = {}

        for i in range(1, len(sorted_years)):
            prev_year = sorted_years[i - 1]
            curr_year = sorted_years[i]
            change = years[curr_year] - years[prev_year]
            changes[country][f"{prev_year}-{curr_year}"] = change

    return changes

def display_changes(changes):
    for country, periods in changes.items():
        print(f"\n{country}:")

        for period, change in periods.items():
            sign = "+" if change > 0 else ""

            print(f"  {period}: {sign}{change}")