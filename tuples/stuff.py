def group_details():
    group_name = input('what is the name of your group?: ')
    group_size = input('how many people are in your group?: ')
    competition_date = input('what day was your competition? -day-month-year-: ')
    venue = input('what is the venue of your competintion?: ')
    medal_type = input('what kind of medal do you have:? ')
    group = (group_name ,group_size ,competition_date ,venue, medal_type)
    print(group)

for i in range(5):
    print(f'enter detail for group {i + 1}')
    group_details()