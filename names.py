import csv
import names_function as fc

filename = 'names-2000-2016.csv'
with open(filename) as f:
	
	reader = csv.reader(f)
	header_row = next(reader)
	years = []
	names = []
	numbers = []
	sexes = []
	
	for row in reader:
		
		years.append(row[0])
		names.append(row[1])
		numbers.append(row[2])
		sexes.append(row[3])

year = sorted(list(set(years)))
how_many = 10
name_M = ['JAKUB', 'ANTONI', 'MATEUSZ', 'KACPER', 'PIOTR']
name_K = ['JULIA', 'NATALIA', 'WIKTORIA', 'ALEKSANDRA', 'LENA']

fc.make_svg(15, year, 'M', 'most', years, names, numbers, sexes)
fc.make_svg(15, year, 'K', 'most', years, names, numbers, sexes)
fc.make_svg(50, year, 'M', 'less', years, names, numbers, sexes)
fc.make_svg(50, year, 'K', 'less', years, names, numbers, sexes)
fc.make_svg_mix(name_M, year, 'M', years, names, numbers, sexes)
fc.make_svg_mix(name_K, year, 'K', years, names, numbers, sexes)
