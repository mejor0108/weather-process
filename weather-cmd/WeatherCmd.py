from .ProcessData import ProcessData
from .ConnectMongoDB import ConnectMongoDB
from mongoengine import connect
from dotenv import load_dotenv

load_dotenv()

MONGODB = os.getenv('MONGODB')
  



connect(alias='core', host='mongodb://localhost:27017/weather')









