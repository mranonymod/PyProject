# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
import datetime
  
def genqr(string,path):
    # String which represents the QR code
    s = string
    
    # Generate QR code
    url = pyqrcode.create(s)
    current_date_and_time = datetime.datetime.now()
    current_date_and_time_string = current_date_and_time.strftime("%d/%m/%Y %H:%M:%S")
    cdt=''.join(e for e in current_date_and_time_string if e.isalnum())

    pathandfile=path+"/"+cdt+"_QR.png"
    # Create and save the png file naming "myqr.png"
    url.png(pathandfile, scale = 10)