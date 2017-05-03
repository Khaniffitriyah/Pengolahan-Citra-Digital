#NAMA   : KHONIF NUR FITRIYAH
#NIM    : 5301414043
#ROMBEL : 02
#PRODI  : PENDIDIKAN TEKNIK ELEKTRO
#TUGAS  : MENGOLAH CITRA BERWARNA MENJADI NEGATIF PADA WEBCAM PC

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#ntuk melakukan inisialisasi pada webcam. angka "0" menunjukkan bahwa yang digunakan adalah webcam internal pada pc.
print(cap.isOpened())
#menampilkan gambar
while(True): 
    #melakukan looping (pengulangan) imshow, sehingga camera akan menangkap objek video secara realtime.
    ret, frame = cap.read() 
    #menangkap gambar dengan format berwarna /BGR
    abu=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    #mengkonversi objek video dari yang sebelumnya berwarna menjadi keabuan terlebih dahulu sebelum diubah menjadi gambar negatif.
    cv2.imshow('webcam', 255-abu) 
    #mengubah gambar dari skala keabuan menjadi gambar dengan skala negatif. 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        #perintah untuk menutup program dengan menekan tombol "q" pada keyboard
        break
        #menghentikan program

#setelah semuanya selesai, capture dilepaskan
cap.realease()
cv2.destroyAllwindows()
