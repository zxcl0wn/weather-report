import pytz
import datetime as dt
# pytz.
print('Часовые пояса, поддерживаемые модулем pytz: \n', pytz.all_timezones, '\n ')
qwe = pytz.all_timezones
print(qwe)
source_date = dt.datetime.now()


currentTimeZone = pytz.timezone('MST')# print(source_date, currentTimeZone)

currentDateWithTimeZone = currentTimeZone.localize(source_date)
print(f'Дата и время этого часового пояса:'
      f'\n{currentDateWithTimeZone}')


newTimeZone = pytz.timezone('Europe/Moscow')
print('\n Часовой пояс установлен на: \n',newTimeZone)



# Прочитать и распечатать текущую дату и время нового часового пояса
newDateWithTimezone = currentDateWithTimeZone.astimezone(newTimeZone)
print('Дата и время этого часового пояса: \n', newDateWithTimezone)

# Прочитать дату и время указанного часового пояса
print('\n Datetime of UTC Time-zone:', dt.datetime.now(tz=currentTimeZone))
print('Datetime часового пояса IST:', dt.datetime.now(tz=newTimeZone))