import cv2 as cv
def qrdet():
    im = cv.imread('myqr.png')
    det = cv.QRCodeDetector()
    retval, points, straight_qrcode = det.detectAndDecode(im)
    print(retval)
    return retval