# Script to convert the disease dataset from a CSV format to a JSON format

if __name__ == "__main__" :

	# Open the two files
	fcsv = open('diseases.csv', 'r')
	fjson = open('intents.json', 'r+')

	# Move the file pointer to the end of the JSON file
	fjson.seek(0, 2)
	pos = fjson.tell()

	# Check if the file is already ready for use
	if pos != 1230 :
		exit(0)

	# Move the file pointer back to overwrite the end of the JSON object
	fjson.seek((pos - 4), 0)
	fjson.write(",\n")

	# Read all the diseases in the CSV file, skipping the comment on the first line
	diseases = fcsv.readlines()
	diseases = diseases[1:]

	# Iterate over all the disease entries
	for disease in diseases :

		# Separate the disease entry into its components and remove all extra whitespaces
		elements = disease.split(',', 2)
		for i in range (3) :
			elements[i] = elements[i].strip()

		# Write formatted text to the JSON file
		fjson.write("\t{{\"tag\": \"{}\",\n".format(elements[1]))
		fjson.write("\t \"patterns\": [")

		# Get all the listed symptoms from the disease entry
		symptoms = elements[2][1:-1].split(',')

		# Iterate over the symptoms and write them into the JSON file
		for symptom in symptoms :
			symptom = symptom.strip()
			fjson.write("\"{}\", ".format(symptom))

		# Move the file pointer back to overwrite the extra ','
		pos = fjson.tell()
		fjson.seek((pos - 2), 0)
		fjson.write("],\n")

		# Write formatted text to the JSON file
		fjson.write("\t \"responses\": [\"I can't say for certain, but this might be a symptom of {d}\", \"I'm not sure, but it is possible that you might have {d}\", \"Based on that information, it could turn out to be a case of {d}\"],\n".format(d = elements[1]))

		fjson.write("\t \"context\": [\"\"]\n")
		fjson.write("\t},\n")

	# Move the file pointer back to overwrite the extra ',' with the end of JSON object
	pos = fjson.tell()
	fjson.seek((pos - 2), 0)
	fjson.write("\n]}")

	# Close both the files	
	fcsv.close()
	fjson.close()
