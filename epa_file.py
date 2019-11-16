# -#mileage data
#from http://www.fueleconomy.gov/FEG/download.shtml
#store in the same folder where your program is

def create_milage_list(epa_file):
  mileage_list = []
  header = epa_file.readline()
  for line in epa_file:
      line_list = line.split(',')
      if 'Car' in line_list[70]:
          mileage_list.append((int(line_list[10]), line_list[2], line_list[3]))
  return mileage_list
epa_file = open('epa_data.csv' , 'r')
mileage_list = create_milage_list(epa_file)
max_mileage = max(mileage_list)
min_mileage = min(mileage_list)
print('Max and Min milage: ', max_mileage, min_mileage)