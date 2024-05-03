from mongoengine import Document, DateField, StringField, FloatField, DateTimeField, connect
from datetime import datetime
from dotenv import load_dotenv
import os





class Weather(Document):
    # fecha = None                       # date
    # estacion = None                    # str
    # hora = None                        # timestamp
    # temperatura = None                 # float
    # estado_nuboso = None               # str
    # visibilidad = None                 # float > 0
    # sensacion_termica = None           # float 
    # humedad_relativa = None            # float >= 0
    # viento_intensidad = None           # float >= 0
    # viento_direccion = None            # str
    # presion_superfice = None           # float > 0 
    
    _fecha_hora          = DateField(required=True)
    _estacion            = StringField(required=True)
    _temperatura         = FloatField(required=True)
    _estado_nuboso       = StringField(required=True)
    _visibilidad         = FloatField(min_value=0, required=True)
    _sensacion_termica   = FloatField(required=True)
    _humedad_relativa    = FloatField(min_value=0, required=True)
    _viento_intensidad   = FloatField(min_value=0, required=True)
    _viento_direccion    = StringField(required=True)
    _presion_superfice   = FloatField(min_value=0, required=True)
    
    def __init__(self, *args ,**kwargs):
        # insertar los parametro en su correspondiente atributo
        super(Weather, self).__init__(*args, **kwargs)
       
    @property
    def fecha(self):
        return self._fecha_hora

    @fecha.setter
    def fecha(self, value):
        self._fecha_hora = value

    @property
    def estacion(self):
        return self._estacion

    @estacion.setter
    def estacion(self, value):
        self._estacion = value

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, value):
        self._hora = value

    @property
    def temperatura(self):
        return self.temperatura

    @temperatura.setter
    def temperatura(self, value):
        self._temperatura = value

    @property
    def estado_nuboso(self):
        return self._estado_nuboso

    @estado_nuboso.setter
    def estado_nuboso(self, value):
        self._estado_nuboso = value

    @property
    def visibilidad(self):
        return self._visibilidad

    @visibilidad.setter
    def visibilidad(self, value):
        self._visibilidad = value

    @property
    def sensacion_termica(self):
        return self._sensacion_termica

    @sensacion_termica.setter
    def sensacion_termica(self, value):
        self._sensacion_termica = value

    @property
    def humedad_relativa(self):
        return self._humedad_relativa

    @humedad_relativa.setter
    def humedad_relativa(self, value):
        self._humedad_relativa = value

    @property
    def viento_intensidad(self):
        return self._viento_intensidad

    @viento_intensidad.setter
    def viento_intensidad(self, value):
        self._viento_intensidad = value

    @property
    def viento_direccion(self):
        return self._viento_direccion

    @viento_direccion.setter
    def viento_direccion(self, value):
        self._viento_direccion = value

    @property
    def presion_superfice(self):
        return self._presion_superfice

    @presion_superfice.setter
    def presion_superfice(self, value):
        self._presion_superfice = value
        
    
    
    

            
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
        'collection': 'weather'
    }
    
    
    
if __name__ == '__main__':
    load_dotenv()
    
    connect(alias='core', host=os.getenv('MONGODB'))
    
    weather = Weather( 
        fecha_hora='2021-10-01',
        estacion='Aeropuerto de Barcelona',
        temperatura=20.0,
        estado_nuboso='Despejado',
        visibilidad=10.0,
        sensacion_termica=20.0,
        humedad_relativa=50.0,
        viento_intensidad=10.0,
        viento_direccion='Norte',
        presion_superfice=1013.0
    )
    
    weather.save()
    
    print(weather)
    
    
    
    
    