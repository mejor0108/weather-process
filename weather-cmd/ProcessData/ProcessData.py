
from ConnectSMN.ConnectSMN import ConnectSMN 
from  ZipToData.ZipToData import ZipToData
import io
import json

class ProcessData():
    def __init__(self):
        pass
    
    def process_data(self, url: str) -> str:
        """
        Downloads a zip file from the given URL, extracts the contents of the first text file found in the zip file and returns it.

        Args:
            url (str): The URL from which the zip file is to be downloaded.

        Returns:
            str: The contents of the first text file found in the zip file.
        """
        # Download the zip file
        zip_stream = self.__get_file_SMN(url)
        # Extract the contents of the first text file found in the zip file
        text = self.__get_text_file(zip_stream)        
        
        resultado = self.__convert_txt_json(text)
        return resultado
    
    def __get_file_SMN(self, url: str) -> io.BytesIO:
            """
            Downloads a zip file from the specified URL and returns it as a BytesIO object.

            Args:
                url (str): The URL of the zip file to download.

            Returns:
                io.BytesIO: The downloaded zip file as a BytesIO object.
            """
            
            # Download the zip file
            smn = ConnectSMN(url)
            zip_stream = smn.download_file()
            return zip_stream
        
    def __get_text_file(self, zip_stream: io.BytesIO) -> str:
        """
        Extracts the contents of the first text file found in the zip file.

        Args:
            zip_stream (io.BytesIO): The zip file stream.

        Returns:
            str: The contents of the first text file found in the zip file.
        """
        # Extract the contents of the first text file found in the zip file
        zip_to_data = ZipToData()
        text = zip_to_data.unzip_to_text(zip_stream)
        print(type(text))
        
        return text
    
    def __convert_txt_json(self, texto: str) -> str:
        """
        Converts the given text to a JSON object.

        Args:
            text (str): The text to convert.

        Returns:
            dict: The JSON object.
        """
        # Convert the text to a JSON object
        #texto = eval( '"' + texto + '"' )
        texto = texto.replace('/', '')
        
        filas = texto.split('\r\n')
        
        resultado  = [fila.split(';') for fila in filas ]
        
        print (resultado)
        return texto
        
        
if __name__ == "__main__":
    
    url = "https://ssl.smn.gob.ar/dpd/zipopendata.php?dato=tiepre"
    
    process_data = ProcessData()
    process_data.process_data(url)
    