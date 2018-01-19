import pygal

#Czyszczenie tablicy

def clean_tab(tab):
	empty_tab = []
	tab = empty_tab
	
	return tab
	
#Sprawdzenie określonego imienia
	
def spec_name(name, year, sex, years, names, numbers, sexes, men_names, how_many_men, women_names, how_many_women):
	if sex == 'M':
		for i in range(0, len(years)):
			if years[i] == year and sexes[i] == sex and names[i] == name:
				men_names.append(names[i])
				how_many_men.append(numbers[i])
				break
	elif sex == 'K':
		for i in range(0, len(years)):
			if years[i] == year and sexes[i] == sex and names[i] == name:
				women_names.append(names[i])
				how_many_women.append(numbers[i])
				break
	else:
		print("Zła płeć")

#Najpopularniejsze imię w danym roku

def most_popular_name(year, sex, years, names, numbers, sexes, men_names, how_many_men, women_names, how_many_women):
	
	if sex == 'M':
		for i in range(0, len(years)):
			if years[i] == year and sexes[i] == sex:
				men_names.append(names[i])
				how_many_men.append(numbers[i])
				break
	elif sex == 'K':
		for i in range(0, len(years)):
			if years[i] == year and sexes[i] == sex:
				women_names.append(names[i])
				how_many_women.append(numbers[i])
				break
	else:
		print("Zła płeć")
		
# $how_many najpopularniejszych imion w danym roku
		
def most_popular_names(how_many, year, sex, years, names, numbers, sexes, men_names, how_many_men, women_names, how_many_women):
	
	if sex == 'M':
		for i in range(0, len(years)):
			if years[i] == year and sexes[i] == sex:
				for j in range(i, i + how_many):
					men_names.append(names[j])
					how_many_men.append(numbers[j])
				break
	elif sex == 'K':
		for i in range(0, len(years)):
			if years[i] == year and sexes[i] == sex:
				for j in range(i, i + how_many):
					women_names.append(names[j])
					how_many_women.append(numbers[j])
				break
	else:
		print("Zła płeć")

#Najmniej popularne imię w danym roku

def less_popular_name(year, sex, years, names, numbers, sexes, men_names, how_many_men, women_names, how_many_women):
	
	if sex == 'M':
		for i in range(0, len(years)):
			if years[i] == year and sexes[i] == sex:
				men_names.insert(0, names[i])
				how_many_men.insert(0, numbers[i])
	elif sex == 'K':
		for i in range(0, len(years)):
			if years[i] == year and sexes[i] == sex:
				women_names.insert(0, names[i])
				how_many_women.insert(0, numbers[i])
	else:
		print("Zła płeć")
		
		
# $how_many najmniej popularnych imion w danym roku

def less_popular_names(how_many, year, sex, years, names, numbers, sexes, men_names, how_many_men, women_names, how_many_women):
	
	if sex == 'M':
		j, k = -1, -1
		for i in range(0, len(years)):
			j += 1
			if years[i] == year and sexes[i] == sex:
				while years[i] == year and sexes[i] == sex:
					k += 1
					i += 1
				break
		for i in range(j+k, j+k-how_many, -1):
			men_names.append(names[i])
			how_many_men.append(numbers[i])
	elif sex == 'K':
		j, k = -1, -1
		for i in range(0, len(years)):
			j += 1
			if years[i] == year and sexes[i] == sex:
				while years[i] == year and sexes[i] == sex:
					k += 1
					i += 1
					if i == len(years):
						break
				break
		for i in range(j+k, j+k-how_many, -1):
			women_names.append(names[i])
			how_many_women.append(numbers[i])
	else:
		print("Zła płeć")

#Tworzenie svg most i less

def make_svg(how_many, year, sex, mode, years, names, numbers, sexes):
	
	men_names = []
	women_names = []
	how_many_men = []
	how_many_women = []	
	
	for i in range(0, int(year[-1])-int(year[0])+1):
		
		if mode == 'most':
			most_popular_names(how_many, year[i], sex, years, names, numbers, sexes, men_names, how_many_men, women_names, how_many_women)
		elif mode == 'less':
			less_popular_names(how_many, year[i], sex, years, names, numbers, sexes, men_names, how_many_men, women_names, how_many_women)
		
		line_chart = pygal.Bar()
		line_chart.force_url_protocol = 'http'
		if sex == 'M':
			if mode == 'most':
				line_chart.title = str(how_many) + " najpopularniejszych imion męskich w roku " + str(year[i])
				line_chart.x_labels = men_names
				line_chart.x_title = "Imię"
				line_chart.y_title = "Ile imion nadano w roku " + str(year[i])
				file_name =  mode + "_men_" + str(how_many) + "_" + str(year[i]) + ".svg"
			elif mode == 'less':
				line_chart.title = str(how_many) + " najmniej popularnych imion męskich w roku " + str(year[i])
				line_chart.x_labels = men_names
				line_chart.x_title = "Imię"
				line_chart.y_title = "Ile imion nadano w roku " + str(year[i])
				file_name =  mode + "_men_" + str(how_many) + "_" + str(year[i]) + ".svg"
			
			for j in range(0, len(men_names)):
				how_many_men[j] = int(how_many_men[j])
			
			if mode != 'mix':
				line_chart.add(str(year[i]), how_many_men)
				if mode == 'less':
					line_chart.render_to_file("svg/svg_men_less/" + file_name)
				elif mode == 'most':
					line_chart.render_to_file("svg/svg_men_most/" + file_name)
				men_names = clean_tab(men_names)
				how_many_men = clean_tab(how_many_men)
			
			
		elif sex == 'K':
			if mode == 'most':
				line_chart.title = str(how_many) + " najpopularniejszych imion damskich w roku " + str(year[i])
				line_chart.x_labels = women_names
				line_chart.x_title = "Imię"
				line_chart.y_title = "Ile imion nadano w roku " + str(year[i])
				file_name =  mode + "_women_" + str(how_many) + "_" + str(year[i]) + ".svg"
			elif mode == 'less':
				line_chart.title = str(how_many) + " najmniej popularnych imion damskich w roku " + str(year[i])
				line_chart.x_labels = women_names
				line_chart.x_title = "Imię"
				line_chart.y_title = "Ile imion nadano w roku " + str(year[i])
				file_name =  mode + "_women_" + str(how_many) + "_" + str(year[i]) + ".svg"
			
			for j in range(0, len(women_names)):
				how_many_women[j] = int(how_many_women[j])

			if mode != 'mix':
				line_chart.add(str(year[i]), how_many_women)
				if mode == 'less':
					line_chart.render_to_file("svg/svg_women_less/" + file_name)
				elif mode == 'most':
					line_chart.render_to_file("svg/svg_women_most/" + file_name)
				women_names = clean_tab(women_names)
				how_many_women = clean_tab(how_many_women)			
			
		else:
			print("Zła płeć")

#Tworzenie svg mix

def make_svg_mix(name, year, sex, years, names, numbers, sexes):
	
	men_names = []
	women_names = []
	how_many_men = []
	how_many_women = []
	
	line_chart = pygal.Bar()
	line_chart.force_url_protocol = 'http'
	line_chart.x_title = "Imię"
	line_chart.y_title = "Ile imion nadano"
	line_chart.x_labels = name
	
	if sex == 'M':
		file_name = "mix_M.svg"
		line_chart.title = "Popularne imiona męskie w latach 2000-2016"
		
		for j in range(0, len(year)):
			for i in range(0,len(name)):
				spec_name(name[i], year[j], sex, years, names, numbers, sexes, men_names, how_many_men, women_names, how_many_women)

			for k in range(0, len(men_names)):
				how_many_men[k] = int(how_many_men[k])
			
			line_chart.add(str(year[j]), how_many_men)

			men_names = clean_tab(men_names)
			how_many_men = clean_tab(how_many_men)

		line_chart.render_to_file("svg/mix/" + file_name)
		
	elif sex == 'K':
		file_name = "mix_K.svg"
		line_chart.title = "Popularne imiona damskie w latach 2000-2016"
		
		for j in range(0, len(year)):
			for i in range(0,len(name)):
				spec_name(name[i], year[j], sex, years, names, numbers, sexes, men_names, how_many_men, women_names, how_many_women)

			for k in range(0, len(women_names)):
				how_many_women[k] = int(how_many_women[k])
			
			line_chart.add(str(year[j]), how_many_women)

			women_names = clean_tab(women_names)
			how_many_women = clean_tab(how_many_women)

		line_chart.render_to_file("svg/mix/" + file_name)
	else:
		print("Zła płeć")

