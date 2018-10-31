from datetime import datetime
stri = str(datetime.now().strftime('%I:%M'))

system_hr = stri[0:2]
system_min = stri[3:5]

print(system_hr)
print()
print(system_min)