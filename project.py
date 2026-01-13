# Wendpouire Nafissa Ouedraogo 191977


import pandas as pd
df = pd.read_csv("co2 Emission Africa.csv")
# import pandas library to load and read the csv file




# 1. Search emission records by year and sector for a specific country
# Retrieve columns where the sectors are
# Allows the user to input a country name and view CO₂ emissions by sector.
# The user can enter a specific year or leave it blank to view data for all years.
# Sector names are matched case-insensitively, allowing input flexibility.

sector_columns = [ "Transportation (Mt)", "Other Fuel Combustion (Mt)", "Manufacturing/Construction (Mt)", "Land-Use Change and Forestry (Mt)","Industrial Processes (Mt)", "Fugitive Emissions (Mt)","Energy (Mt)","Electricity/Heat (Mt)","Bunker Fuels (Mt)", "Building (Mt)"]
sector_lookup = {s.lower().replace(" (mt)", "").strip(): s for s in sector_columns}
country_input = input("Enter an African country name: ").lower().strip()
input_yr = input("Enter a specific year to view emission by sector or press enter to view for all years:")
if country_input not in df["Country"].str.lower().unique():
    print("Country not found. Please enter an African country name.")
else:
      if input_yr == "":
         table = df[df["Country"].str.lower() == country_input].groupby("Year")[sector_columns].sum()
         print(f"Emission table by year and sector for {country_input.title()}:")
         print(table)
      else: 
        try:
           year = int(input_yr) 
           if year < 2000 or year > 2020:
            raise ValueError
           country_df = df[(df["Country"].str.lower() == country_input) & (df["Year"] == year)]
           if country_df.empty:
              print(f"No data found for {country_input.title()} in {year}.")
           else:
               print(f"\nEmission data for {country_input.title()} in {year}:")
               print(country_df[sector_columns].sum())
        except ValueError:
           print("Invalid year entered. Please enter a number between 2000 and 2020.")


 


# 2. Computes total CO₂ emissions for each year across all African countries.
# Create a dictionary to holds year with total emission.
# Iterrates trough csv file to retrieve rows containing year and emission, store them in the dictionary then sum up emission for each year.
# The user can input a specific year or leave it blank to see totals for all years.

year_lists = {}
for index, row in df.iterrows():
    year = int(row["Year"])
    emission = row["Total CO2 Emission including LUCF (Mt)"]
    if year in year_lists:
       year_lists[year] += emission
    else:
       year_lists[year] = emission
input_year = input("Enter a specific year between 2000 and 2020 or press enter to view all years emission:")
if input_year == "":
    print(f"Total emission in Africa from 2000 t0 2020:")
    for year in sorted(year_lists):
        print(f"{year} : {year_lists[year]:.2f} Mt")
else:
    try:
        year = int(input_year)
        if year in year_lists:
            print(f"Total emisssion in Africa in {year} is {year_lists[year]:.2f} Mt")
        else:
            print(f"No emission record found for {year}")
    except ValueError:
        print("Please enter a valid numeric year")




# 3. Identify country with highest emissions for a selected year
# Creates a dictionary. 
# Iterates through our data then retrieve rows containing country, emission and year then store then in the dictionary.
# Compares emissions for a year, get the highest emission then return the country with the highest emission for that year and the emission
# The user can choose a specific year or view the highest emitter across all years.
N_emitting_countries= {}
for index, row in df.iterrows():
    country = row["Country"]
    emission = row["Total CO2 Emission including LUCF (Mt)"]
    year = row["Year"]
    if year not in N_emitting_countries:
        N_emitting_countries[year]= (country,emission)
    else:
        if emission > N_emitting_countries[year][1]:
            N_emitting_countries[year] = (country, emission)
yr_input = input("Enter a specific year to view highest emitting country or press enter to view top emitting countries for all years:")

if yr_input == "":
    print(f"N_emitting_countries from 2000 to 2020 are:")
    for year in sorted(N_emitting_countries):
        print(f"{year}: {N_emitting_countries[year][0]} ({N_emitting_countries[year][1]} Mt)")
else:
    yr_input= int(yr_input)   
    if yr_input in N_emitting_countries:
        country, emission = N_emitting_countries[yr_input] 
        print(f"Country with highest emission in {yr_input} is {country}")    
    else:
        print("No data found for this year")




# 4. Aggregate and displays emissions by sector
# Retrieve sectors columns.
# Accepts lowercase sector names and ignores the "(Mt)" suffix for flexibility.
# The user can either view emissions for all sectors in a table or view emission for a specific sector 
# When the user chooses option 2, available sectors are printed to allow him to choose the sector he want to view and avoid typo
# Then the user can view emission for that specific sector either yearly and for all years or for a specific year that he will input
sector_columns = [ "Transportation (Mt)", "Other Fuel Combustion (Mt)", "Manufacturing/Construction (Mt)", "Land-Use Change and Forestry (Mt)","Industrial Processes (Mt)", "Fugitive Emissions (Mt)","Energy (Mt)","Electricity/Heat (Mt)","Bunker Fuels (Mt)", "Building (Mt)"]
sector_lookup = {s.lower().replace(" (mt)", "").strip(): s for s in sector_columns}
print("Available sectors:")
for key in sector_lookup:
    print("-", key.title())
sector_input = input("Enter sector name (or press Enter to see full table): ").lower().strip()
if sector_input == "":
   table = df.groupby("Year")[sector_columns].sum()
   print(f"Emission table by year and sector:")
   print(table)
elif sector_input not in sector_lookup:
        print("Invalid sector name")
else:
        sector = sector_lookup[sector_input]
        year_input = input("Enter a year between 2000 and 2020(or press Enter to see total for all years): ").strip()
        if year_input =="":
           yearly_totals = df[df["Year"].between(2000,2020)].groupby("Year")[sector].sum()
           total = yearly_totals.sum()
           print(f"Yearly emissions for {sector} from 2000 to 2020:")
           for year, value in yearly_totals.items():
               print(f"{year}: {value:.2f} Mt")
           print(f"Total emisssions for {sector} from 2000 to 2020: {total:.2f} Mt")
        else:
            try:
                year = int(year_input)
                if year not in df["Year"].values:
                   print("Year not found in dataset.")
                else:
                    value = df[df["Year"]==year][sector].sum()
                    print(f"Total emission in {sector} in {year} is: {value:.2f}")
            except ValueError:
                 print("Invalid year input")




# 5. Tracks CO2 emissions trend for a selected country over the years.
# Creates a dictionary to store emissions by country
# Iterates through csv file to retrieve rows containing country, year and emission them store them in the dictionary
# The user can view emissions accross all years or for a specific year 
emissions_by_country = {}
for index, row in df.iterrows():
    country = row["Country"].strip().title()
    year = int(row["Year"])
    emission = row["Total CO2 Emission including LUCF (Mt)"]
    if country not in emissions_by_country:
       emissions_by_country[country]={}
    emissions_by_country[country][year] = emission
country_input = input("Enter an African country name:").strip().title()
year_input = input("Enter a specific year (or press Enter to view all years):")

if country_input in emissions_by_country:
    if year_input == "":
        print(f"Total CO2 emissions in {country_input} from 2000 to 2020:")
        for year in sorted(emissions_by_country[country_input]):
            emission = emissions_by_country[country_input][year]
            print(f"{year}: {emission:.2f} Mt")
    else:
        try:
            year = int(year_input)
            if year in emissions_by_country[country_input]:
                emission = emissions_by_country[country_input][year]
                print(f"Total CO2 emission in {country_input} in {year} is: {emission:.2f} Mt")
            else:
                print(f"No emission record found for {country_input} in {year}.")
        except ValueError:
            print("Please enter a valid numeric year.")
else:
    print(f"No data found for country: {country_input}")




# 6. Insert New Emission Record: Simulates real-time input by allowing user input
# Headers are retrieved and soter in a list (headers)
# The user input a new emission record
# If the user leave a blank space a missing value is stored
# When input data is numeric if there is a dot it is converted to a float else it is converted to an integer. Elsewhere None is stored
# The new record is added to the csv file
# Few last rows of csv file are printed

headers = df.columns.tolist()
new_record = {}
print("Please enter data for the following fields or press enter to skip field")

for header in headers:
    user_input = input(f"Enter {header}: ").strip()
    if user_input == "":
        new_record[header] = None
    else:
        if pd.api.types.is_numeric_dtype(df[header]):
            try:
                if '.' in user_input:
                    new_record[header] = float(user_input)
                else:
                    new_record[header] = int(user_input)
            except ValueError:
                new_record[header] = None 
        else:
            new_record[header] = user_input

df = pd.concat([df, pd.DataFrame([new_record]).dropna(axis=1, how ="all")], ignore_index=True)

print(" New emission record:")
print(df.tail) 




#7.Undo last insertion : remove new emission record
# Return all rows except the last row
# Few last rows of csv file are printed
df = df.iloc[:-1]
print("Last insertion is removed")
print(df.tail)



