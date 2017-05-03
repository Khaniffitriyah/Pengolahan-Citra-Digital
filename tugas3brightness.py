#NAMA   : KHONIF NUR FITRIYAH
#NIM    : 5301414043
#ROMBEL : 02
#PRODI  : PENDIDIKAN TEKNIK ELEKTRO
#TUGAS  : MENGOLAH KECERAHAN CITRA PADA WEBCAM PC

import numpy as np
import cv2

cap = cv2.VideoCapture(0) 
#melakukan inisialisasi pada webcam. angka "0" menunjukkan bahwa yang digunakan adalah webcam internal pada pc.
print(cap.isOpened())
#menampilkan gambar

while(True): 
    #melakukan looping (pengulangan) imshow, sehingga camera akan menangkap objek video secara realtime.
    ret, frame = cap.read() 
    #menangkap gambar dengan format berwarna /BGR
    bright = cv2.addWeighted(frame,1.5, np.zeros(frame.shape, frame.dtype), 0, 25) 
    #meningkatkan nilai kecerahan gambar
    cv2.imshow('webcam',bright) 
    #menampilkan gambar yang telah diubah tingkat kecerahannya.
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        #perintah untuk menutup program dengan menekan tombol "q" pada keyboard
        break
        #menghentikan program

##setelah semuanya selesai, capture dilepaskan
cap.realease()
cv2.destroyAllwindows()
