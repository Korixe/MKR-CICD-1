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