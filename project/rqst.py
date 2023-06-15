import requests
import datetime 
from tabulate import tabulate
from math import ceil


default_date = datetime.datetime.now()
key = 'eb3a79de-1bd8-4e64-8a74-f95314d94149'
event = 'departure'
station_code = 's9602494'
transport_type = 'train'

def flight_table(event):
    station_code = 's9600366'
    schedule_api = f'https://api.rasp.yandex.net/v3.0/schedule/?apikey={key}&station={station_code}&date={str(default_date)}&event={event}'
    response = requests.get(schedule_api).json()
    number_of_flights = int(ceil(response['pagination']['total']/100))
    flights = []
    for i in range(number_of_flights):
        schedule_api = f'https://api.rasp.yandex.net/v3.0/schedule/?apikey={key}&station={station_code}&date={str(default_date)}&offset={i*100}&event={event}'
        response = requests.get(schedule_api).json()
        name = response['station']['station_type_name']+' '+response['station']['title']
        timesheet = response['schedule']
        for flight in timesheet:
            info = []
            if default_date < datetime.datetime.fromisoformat(flight['departure'][:19]):
                info.append(flight['thread']['number'])
                info.append(flight['thread']['title'])
                info.append(flight['departure'][11:16])
                flights.append(info)
    #print(f'Табло рейсов на Вылет, {name} \n')
    return ('<pre>'+tabulate(flights, headers = ["Рейс№", "Рейс", "Время вылета(!Местное время!)"], tablefmt="plain") + '</pre>')

def train_table(station_code, event):
    schedule_api = f'https://api.rasp.yandex.net/v3.0/schedule/?apikey={key}&station={station_code}&date={str(default_date)}&event={event}'
    response = requests.get(schedule_api).json()
    name = response['station']['station_type_name']+' '+response['station']['title']
    number_of_trains = int(ceil(response['pagination']['total']/100))
    trains = []
    for i in range(number_of_trains):
        schedule_api = f'https://api.rasp.yandex.net/v3.0/schedule/?apikey={key}&station={station_code}&date={str(default_date)}&offset={i*100}&event={event}&transport_types={transport_type}'
        response = requests.get(schedule_api).json()
        timesheet = response['schedule']
        for train in timesheet:
            info = []
            if default_date < datetime.datetime.fromisoformat(train['departure'][:19]):
                info.append(train['thread']['number'])
                info.append(train['thread']['title'])
                info.append(train['departure'][11:16])
                trains.append(info)
    #return (f'Расписание поездов, {name} \n') 
    return (tabulate(trains, headers = ["№ поезда", "Поезд", "Время отправления"], tablefmt="github"))
f = open('schedule.txt', 'w')
f.write(train_table(station_code ,event))

