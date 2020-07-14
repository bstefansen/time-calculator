import re

def add_time(start, duration, *day):

  # separate hours, minutes, and period
  startHours = int(re.findall('^\d+', start)[0])
  startMinutes = int(re.findall('\d+', start)[1])
  startPeriod = str(re.findall('[A-Z]+', start)[0])
  addHours = int(re.findall('^\d+', duration)[0])
  addMinutes = int(re.findall('\d+', duration)[1])

  # time variables
  newHours = startHours + addHours
  newHoursPeriod = startHours + addHours
  newMinutes = startMinutes + addMinutes
  daysPast = 0
  daysPastString = ''
  periodSwitch = 0
  newPeriod = ''
  weekDays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
  weekDay = ''

  # adjust minutes
  if newMinutes > 59:
    newHours += 1
    newHoursPeriod += 1
    newMinutes -= 60

  # adjust hours
  while newHours > 12:
    newHours -= 12

  # add periodSwitch
  while newHoursPeriod > 11:
    periodSwitch += 1
    newHoursPeriod -= 12

  # switch day period
  if periodSwitch == 0 or periodSwitch % 2 == 0:
    newPeriod += startPeriod
  else:
    newPeriod += 'PM' if startPeriod == 'AM' else 'AM'
  
  # period and day calculations
  if startPeriod == 'PM':
    while periodSwitch > 0:
      daysPast += 1
      periodSwitch -= 2
    
  if startPeriod == 'AM':
    periodSwitch -= 1
    while periodSwitch > 0:
      daysPast += 1
      periodSwitch -= 2

  if daysPast == 1:
    daysPastString += ' (next day)'

  if daysPast > 1:
    daysPastString += ' (' + str(daysPast) + ' days later)'

  # day of the week calculations
  if day:
    newDayIndex = weekDays.index(day[0].lower()) + daysPast
    if newDayIndex > 6:
      while newDayIndex > 6:
        newDayIndex -= 7
    weekDay = ', ' + weekDays[newDayIndex].capitalize()

  # return new time
  return str(newHours) + ':' + ('0' if newMinutes < 10 else '') + str(newMinutes) + ' ' + newPeriod + weekDay + daysPastString

  