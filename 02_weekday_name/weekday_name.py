def weekday_name(day_of_week):
    weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    if 1 <= day_of_week <= 7: 
        return weekdays [day_of_week - 1]
    else: 
        return "None"