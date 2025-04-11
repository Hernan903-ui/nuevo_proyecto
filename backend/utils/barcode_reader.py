import cv2
from pyzbar.pyzbar import decode

def read_barcode():
    """
    Lee códigos de barras utilizando la cámara.
    """
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        for barcode in decode(frame):
            barcode_data = barcode.data.decode('utf-8')
            print(f"Código de barras detectado: {barcode_data}")
            cap.release()
            cv2.destroyAllWindows()
            return barcode_data
        cv2.imshow('Barcode Reader', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()