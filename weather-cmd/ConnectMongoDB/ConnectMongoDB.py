from model.weatherModel import Weather, HoraData
from mongoengine import connect
import os
from dotenv import load_dotenv

class ConnectMongoDB:
    def __init__(self):
        
        connect(os.getenv('MONGODB_DATABASE'),alias='core', host=os.getenv('MONGODB_SERVER'))
        
        

    def insert_data(self, data):
        weather = Weather(
            fecha=data['fecha'],
            estacion=data['estacion'],
            datos_hora=[
                HoraData(
                    hora=data['hora'],
                    temperatura=data['temperatura'],
                    estado_nuboso=data['estado_nuboso'],
                    visibilidad=data['visibilidad'],
                    sensacion_termica=data['sensacion_termica'],
                    humedad_relativa=data['humedad_relativa'],
                    viento_intensidad=data['viento_intensidad'],
                    viento_direccion=data['viento_direccion'],
                    presion_superfice=data['presion_superfice']
                ) 
            ]
        )
        weather.save()

    def get_data(self, fecha, estacion):
        return Weather.objects(fecha=fecha, estacion=estacion).to_json()
    
    
if __name__ == '__main__':
    
    connect = ConnectMongoDB()
    
    connect.insert_data({
        'fecha': '2024-05-27',
        'estacion': 'Estacion Central',
        'hora': '18:00',
        'temperatura': 25.5,
        'estado_nuboso': 'Parcialmente nublado',
        'visibilidad': 10.0,
        'sensacion_termica': 26.0,
        'humedad_relativa': 60.0,
        'viento_intensidad': 15.0,
        'viento_direccion': 'Noreste',
        'presion_superfice': 1012.0
    })
    connect.insert_data({
        'fecha': '2024-05-27',
        'estacion': 'Estacion Central',
        'hora': '19:00',
        'temperatura': 26.5,
        'estado_nuboso': '',
        'visibilidad': 10.0,
        'sensacion_termica': 26.0,
        'humedad_relativa': 60.0,
        'viento_intensidad': 15.0,
        'viento_direccion': 'Noreste',
        'presion_superfice': 1012.0
    })
    print(connect.get_data('2024-05-19','Estacion Central'))