hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_minutes = (hour * 60) + mins + dura 

end_hour = total_minutes // 60
end_mins = total_minutes % 60
print(end_hour, ":", end_mins, sep='')

