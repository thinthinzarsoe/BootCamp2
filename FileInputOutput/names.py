import csv

with open('names.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	with open('save_names.csv', 'w') as new_file:
		fieldnames = ['first_name', 'last_name']

		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

		csv_writer.writeheader()

		for line in csv_reader:
			del line['email']
			csv_writer.writerow(line)

# .DictReader
# .DictWriter
# .writeheader
# .writerow


# Create_name.csv (နဂိုပေးထားသည့်ဖိုင်နာမည်)
# save_names.csv (ထွက်လာရမည့် ဖိုင်အသစ်)
# ID ရှေ့ဆုံး ထည့်ပေး
# excel ထဲတွင် header ထည့်ပေးရန်
# separate between first name & last_name
# အသစ်ထွက်လာမည့် excel ဖိုင်ထဲတွင် ID first_name & last_name တစ်တွဲထဲ ပါဝင်ပါမည်