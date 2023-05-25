import pandas as pd


class CSVDataProcessor:
    def __init__(self, file_path, delimiter=',', has_header=True):
        # Class constructor
        self.file_path = file_path
        self.delimiter = delimiter
        self.has_header = has_header
        self.data_frame = self._read_csv_file()

    def _read_csv_file(self):
        # Read the CSV file into a DataFrame
        try:
            if self.has_header:
                data_frame = pd.read_csv(self.file_path, delimiter=self.delimiter)
            else:
                data_frame = pd.read_csv(self.file_path, delimiter=self.delimiter, header=None)
            return data_frame
        except FileNotFoundError:
            raise Exception(f"File not found: {self.file_path}")
        except pd.errors.ParserError:
            raise Exception(f"Unable to parse CSV file: {self.file_path}")

    def get_data_frame(self):
        # Return the DataFrame
        return self.data_frame

    def get_all_countries(self):
        # Get a string representation of all countries
        countries = self.data_frame['Country'].to_string()
        return countries

    def get_countries_with_larger_area_than_ukraine(self, title_column, comparisons):
        # Get countries with a larger area than Ukraine based on a specified column
        ukraine_area = self.data_frame.loc[self.data_frame['Country'] == 'Ukraine ', title_column].item()
        if comparisons == '>':
            larger_countries = self.data_frame.loc[self.data_frame['Area (sq. mi.)'] > ukraine_area, 'Country']
        elif comparisons == '<':
            larger_countries = self.data_frame.loc[self.data_frame['Area (sq. mi.)'] < ukraine_area, 'Country']
        else:
            return "Invalid symbol entered"
        return larger_countries

    def get_countries_with_population_over_and_larger_area_than(self, country, population):
        # Get countries with a population over a certain value and a larger area than a specified country
        country_area = self.data_frame.loc[self.data_frame['Country'] == country, 'Area (sq. mi.)'].item()
        large_population_countries = self.data_frame.loc[(self.data_frame['Population'] > population) & (
                    self.data_frame['Area (sq. mi.)'] > country_area), 'Country']
        return large_population_countries

    def get_countries_without_coastline(self, boolean=True):
        # Get countries with or without a coastline based on a boolean value
        if boolean:
            no_coast_countries = self.data_frame.loc[self.data_frame['Coastline (coast/area ratio)'] != 0, 'Country']
        elif boolean is False:
            no_coast_countries = self.data_frame.loc[self.data_frame['Coastline (coast/area ratio)'] == 0, 'Country']
        else:
            return "Invalid logical value entered"
        return no_coast_countries

    def get_top_most_densely_populated_countries(self, top=10):
        # Get the top N densely populated countries based on population density
        top_10_densely_populated = self.data_frame.nlargest(top, 'Pop. Density (per sq. mi.)')['Country']
        return top_10_densely_populated


# Create an instance of the CSVDataProcessor class and perform operations
data = CSVDataProcessor('countries_of_the_world.csv')

# Get all countries
print("List of all countries")
print("-" * 100)
print(data.get_all_countries())
print("-" * 100)

# Get countries with a larger area than Ukraine
print("Countries with a larger area than Ukraine")
print("-" * 100)
print(data.get_countries_with_larger_area_than_ukraine('Area (sq. mi.)', '>'))
print("-" * 100)

# Get countries with a population over 10 million and a larger area than Ukraine
print("Countries with a population over 10 million and a larger area than Ukraine")
print("-" * 100)
print(data.get_countries_with_population_over_and_larger_area_than('Ukraine ', 10000000))
print("-" * 100)

# Get countries without a coastline
print("Countries without a coastline")
print("-" * 100)
print(data.get_countries_without_coastline(boolean=False))
print("-" * 100)

# Get the top 10 most densely populated countries
print("Top 10 most densely populated countries")
print("-" * 100)
print(data.get_top_most_densely_populated_countries(top=10))
print("-" * 100)
