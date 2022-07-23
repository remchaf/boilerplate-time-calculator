def add_time(startTime, endTime, starting_day=''):
    week = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saterday", "Sunday")
    [h0, m0] = startTime.split(' ')[0].split(':')
    time0 = (int(h0) % 12) * 60 + int(m0)
    if startTime.split(' ')[1] == 'PM':
        time0 += 12 * 60

    [h1, m1] = endTime.split(':')
    time1 = time0 + int(h1) * 60 + int(m1)

    # Days after
    days = time1 // (24*60)
    try:
        time1 %= (days * 24 * 60)
    except:
        pass

    # Hours and minutes after
    hours = time1 // 60
    try :
        minutes = str(time1 % (hours * 60))
    except :
        minutes = str(time1)
    
    if len(minutes) == 1 :
        minutes = '0' + minutes
    
    string = ''
    if hours > 12 :
        string += str(hours - 12) + ':' + str(minutes) + ' PM'
    elif hours == 12 :
        string += '12:' + str(minutes) + ' PM'
    elif not hours :
        string += '12:' + str(minutes) + ' AM'
    else :
        string += str(hours) + ':' + str(minutes) + ' AM'
        
    if starting_day :
        for d in range(7) :
            if week[d].lower() == starting_day.lower() :
                string += ', ' + week[(d + days) % 7]
                break
            
    if days == 1 :
        string += ' (next day)'
    elif days > 1 :
        string += ' (' + str(days) + ' days later)'
        
    print(string)


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
