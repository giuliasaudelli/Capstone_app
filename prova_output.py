fiscalcode="LLLMRC99D06B354L"
MIN_AGE_MRI = 6
  
year = int(fiscalcode[6:8])
year_options = [1900 + year , 2000 + year]
print(year)

age_options = [reservation_year -i for i in year_options]

if age_options[1] < MIN_AGE_MRI:
    eta = age_options[0]
    print(eta)
else:
    eta = age_options[1]
    print(eta)
