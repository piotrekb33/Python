import cv2
import cv2.data

#Jako parametr podajemy numer kamery 0-domyślna, 1-pierwsze USB itd lub scieżke do pliku video "moj.mp4", "c:\moj.avi" itp.
video = cv2.VideoCapture(0)

#sprawdzamy czy kamerka działa
if not video.isOpened():
    raise Exception("Nie można otworzyć kamerki")

print(video.isOpened())

#wczytujemy klasyfikator twarzy - Ładuje klasyfikator Haar Cascade do wykrywania twarzy. Plik XML zawiera wytrenowany model AI do wykrywania twzry
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

if face_classifier.empty():
    raise Exception("Nie można wczytac klasyfikatora twarzy")

#Ustawiamy wielkość okna wyswietlania video
#cv2.namedWindow("Kamerka", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("Kamerka", 800, 300)
wymiar_check = True

while True:

    #wczytamy dwie wartosci pierwsza success - czy połaczenie jest TRUE czy False a druga to klatka obrazu z kamery-(Tablica pixeli) jesli jest True
    success, frame = video.read()

    if not success:
        print("Nie można wczytac klatki z kamerki")
        break
    
    #Konvertujemy do skali szarosci bo szybciej w tym systemie wykrywa sie twarze
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    #Wykrywmy twarze w obrazie szarości. Zwraca listę prostokątów (x-wpołrzędna top corner, y-wpółrzędna top corner, w-szerokość, h-wysokość) dla każdej wykrytej twarzy. face[0] tu nzapisze pierwszy wykryty prostokąt twarzy. --scaleFactor → skala przeszukiwania| --minNeighbors → dokładność|--minSize → minimalny rozmiar twarzy. Np. po wykryciu twarzy w print(face) = [[157 299 112 112]]. Natomist face_classifier = < cv2.CascadeClassifier 0000028CFF6DFD70>
    face = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    print (face)
    print (face_classifier)

    #Rysujemy prostokąty wokół wykrytych twarzy
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)


    if wymiar_check:
        print(frame.shape[0]) #wysokość video
        print(frame.shape[1]) #szerokość video
        print(frame.shape[2]) #ilość kanałów koloru dla video RGB jest 3
        wymiar_check = False
    
    #tak zmieniamy rozmiar wyswietlanej klatki video ale inshaw jako drugi parametr musimy zastapic frame na frame_resized
    #frame_resized = cv2.resize(frame, (200, 200))
    cv2.imshow("Kamerka", frame)
    key = cv2.waitKey(1)

    #Przyciski ESC i "q" na klawiaturze zamykaja okno kamerki
    if key == 27 or key == ord('q'):
        break

    #if key != -1:
    #   break

#zwalniamy kamerkę i zamykamy okna
video.release()
cv2.destroyAllWindows()







print(cv2.__version__)
print(cv2.data.haarcascades)
