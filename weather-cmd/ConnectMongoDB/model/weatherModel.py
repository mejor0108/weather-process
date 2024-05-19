from mongoengine import Document, DateField, StringField, FloatField, DateTimeField, connect, EmbeddedDocument, fields
import datetime
from dotenv import load_dotenv
import os




class HoraData(EmbeddedDocument):
    """
    Represents weather data for a specific hour.

    Attributes:
        hora (DateTimeField): The timestamp of the weather data.
        temperatura (FloatField): The temperature in Celsius.
        estado_nuboso (StringField): The description of the cloud state.
        visibilidad (FloatField): The visibility in kilometers.
        sensacion_termica (FloatField): The perceived temperature in Celsius.
        humedad_relativa (FloatField): The relative humidity in percentage.
        viento_intensidad (FloatField): The wind intensity in kilometers per hour.
        viento_direccion (StringField): The wind direction.
        presion_superfice (FloatField): The surface pressure in hPa.
    """

    hora = fields.StringField(required=True, regex=r'^\d{2}:\d{2}(:\d{2})?$')  # Formato HH:MM o HH:MM:SS
    temperatura = fields.FloatField(required=True)
    estado_nuboso = fields.StringField(required=True)
    visibilidad = fields.FloatField(required=True, min_value=0)
    sensacion_termica = fields.FloatField(required=True)
    humedad_relativa = fields.FloatField(required=True, min_value=0)
    viento_intensidad = fields.FloatField(required=True, min_value=0)
    viento_direccion = fields.StringField(required=True)
    presion_superfice = fields.FloatField(required=True, min_value=0)

    def __init__(self, *args, **kwargs):
        super(HoraData, self).__init__(*args, **kwargs)

    def __str__(self):
        return (
            'hora :' + str(self.hora) + '\n' +
            'temperatura :' + str(self.temperatura) + '\n' +
            'estado nuboso :' + str(self.estado_nuboso) + '\n' +
            'visibilidad :' + str(self.visibilidad) + '\n' +
            'sensacion termica :' + str(self.sensacion_termica) + '\n' +
            'humedad relativa :' + str(self.humedad_relativa) + '\n' +
            'viento intensidad :' + str(self.viento_intensidad) + '\n' +
            'viento direccion :' + str(self.viento_direccion) + '\n' +
            'presion superficie :' + str(self.presion_superfice) + '\n'
        )

   

class Weather(Document):
    # fecha = None                       # date
    # estacion = None                    # str
    # List [ HoraDate ]           
    # 
    
    fecha               = DateField(required=True)
    estacion            = StringField(required=True)
    datos_hora          = fields.EmbeddedDocumentListField(HoraData) 
    
    

    
    def __init__(self, *args ,**kwargs):
        # insertar los parametro en su correspondiente atributo
        super(Weather, self).__init__(*args, **kwargs)
       
    
    

            
    def __str__(self):
        """
        Returns a string representation of the WeatherModel object.
        
        The string includes the following information:
        - estación (station)
        - fecha (date)
        - hora (time)
        - temperatura (temperature)
        - estado nuboso (cloudy state)
        - visibilidad (visibility)
        - sensación térmica (thermal sensation)
        - humedad relativa (relative humidity)
        - viento intensidad (wind intensity)
        - viento dirección (wind direction)
        - presión superficie (surface pressure)
        """
        return (
            'estación :' + self.estacion + '\n' +
            'fecha :' + str( self.fecha_hora )+ '\n' +
            'temperatura :' + str(self.temperatura) + '\n' +
            'estado nuboso :' + str(self.estado_nuboso) + '\n' +
            'visibilidad :' + str(self.visibilidad) + '\n' +
            'sensación térmica :' + str( self.sensacion_termica) + '\n' +
            'humedad relativa :' + str(self.humedad_relativa) + '\n' +
            'viento intensidad :' + str(self.viento_intensidad) + '\n' +
            'viento dirección :' + str(self.viento_direccion) + '\n' +
            'presión superficie :' + str(self.presion_superfice)  + '\n'
                )
    
    meta = {
        'db_alias': 'core',
        'collection': "documents"
    }
    
    
    
if __name__ == '__main__':
    load_dotenv()
    
    connect(os.getenv('MONGODB_DATABASE'),alias='core', host=os.getenv('MONGODB_SERVER'))
    
    
    
    
    
    
    
#     Crear una instancia del subdocumento
    hora_data_18 = HoraData(
        hora="18:00",
        temperatura=25.5,
        estado_nuboso='Parcialmente nublado',
        visibilidad=10.0,
        sensacion_termica=26.0,
        humedad_relativa=60.0,
        viento_intensidad=15.0,
        viento_direccion='Noreste',
        presion_superfice=1012.0
    )
    hora_data_19 = HoraData(
        hora="19:00",  # Año, mes, día, hora, minuto
        temperatura=26.5,
        estado_nuboso='',
        visibilidad=10.0,
        sensacion_termica=26.0,
        humedad_relativa=60.0,
        viento_intensidad=15.0,
        viento_direccion='Noreste',
        presion_superfice=1012.0
    )


    # Crear una instancia del documento principal
    estacion_data_example = Weather(
        fecha=datetime.date(2024, 5, 19),
        estacion='Estacion Central',
        datos_hora=[hora_data_18,hora_data_19]  # Puedes agregar más instancias de HoraData si lo necesitas
    )



    
    estacion_data_example.save()
    
    print(estacion_data_example)
    
    
    
    