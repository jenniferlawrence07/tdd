import csv


def get_data(file_name,
             query_column=None,
             query_value=None,
             return_header=False):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)

    if query_column is not None and query_value is not None:
        rows = [
            row for row in rows
            if row[query_column] == query_value
        ]

    if return_header:
        return header, rows

    return rows


def get_column_index(header, column_name):
    try:
        return header.index(column_name)
    except ValueError:
        return None


def get_fire_gdp_year_data(co2_file, gdp_file, country):
    co2_header, co2_rows = get_data(
        co2_file,
        query_column=0,
        query_value=country,
        return_header=True
    )

    gdp_header, gdp_rows = get_data(
        gdp_file,
        query_column=0,
        query_value=country,
        return_header=True
    )

    forest_fire_index = get_column_index(
        co2_header,
        "Forest fires"
    )

    if len(gdp_rows) == 0:
        return []

    gdp_row = gdp_rows[0]
    results = []

    for row in co2_rows:
        year = row[1]
        fire_value = row[forest_fire_index]
        gdp_index = get_column_index(gdp_header, year)

        if gdp_index is None:
            continue

        gdp_value = gdp_row[gdp_index]

        if fire_value == "" or gdp_value == "":
            continue

        results.append([
            int(year),
            float(fire_value),
            float(gdp_value)
        ])

    return results
