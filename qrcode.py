# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
  
def genqr(string):
    # String which represents the QR code
    s = string
    
    # Generate QR code
    url = pyqrcode.create(s)
    
    # Create and save the png file naming "myqr.png"
    url.png('myqr.png', scale = 10)