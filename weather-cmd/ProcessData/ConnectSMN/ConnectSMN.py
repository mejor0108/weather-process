import requests 
import warnings
from typing import BinaryIO
from io import BytesIO

class ConnectSMN(object):
    __url = None
    def __init__(self, url):
        self.__url = url
        
    def download_file(self) -> BytesIO:
        """
        Downloads a file from a specified URL.

        Returns:
            BinaryIO: The downloaded file content as a binary stream.
        """
        # Desactivar advertencias de InsecureRequestWarning
        warnings.filterwarnings("ignore", message="Unverified HTTPS request")

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "DNT": "1",
            "Sec-GPC": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Priority": "u=1",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }

        response = requests.get(self.__url, headers=header, verify=False)
        resultado = b''
        # imprimir el estado de la respuesta
        
        resultado = response.content
        return BytesIO(resultado)
        
if __name__ == "__main__":
    
    prueba = ConnectSMN("https://ssl.smn.gob.ar/dpd/zipopendata.php?dato=tiepre")
    content = prueba.download_file()
    print(str( content)   )
    
    