import cv2 as cv
def qrdet(path):
    im = cv.imread(path)
    det = cv.QRCodeDetector()
    retval, points, straight_qrcode = det.detectAndDecode(im)
    print(retval)
    return retval