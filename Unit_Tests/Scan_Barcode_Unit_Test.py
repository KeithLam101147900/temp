# Importing library
import cv2
from pyzbar.pyzbar import decode
  
# Make one method to decode the barcode
def BarcodeReader(image):
     
    # read the image in numpy array using cv2
    img = cv2.imread(image)
      
    # Decode the barcode image
    detectedBarcodes = decode(img)
      
    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
       
          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes: 
             
            if barcode.data!="":
               
            # Print the barcode data
                print(barcode.data)
                print(barcode.data.decode("utf-8"))
                print(barcode.type)
                 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
# Main
if __name__ == '__main__':
    # Read image
    img = "barcode0.jpg"
 
    print("Decode")
    decodedObjects = BarcodeReader(img)
