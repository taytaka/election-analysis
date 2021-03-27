counties = ["Arapahoe", "Denver", "Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

if "Arapahoe" in counties or "El Paso" in counties:
  print("Arapahoe or El Paso is in the list of counties.")
else:
  print("Arapahoe and El Paso are not in the list of counties.")

for county, voters in counties_dict.items():
  print(county, "county has", voters, "registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
  for value in county_dict.values():
    print(value)

# Using the with statement, open the file as a text file
# with open(file_to_save, "w") as txt_file:

    # Write three counties to the file
    # txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

