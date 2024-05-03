import cv2

# Az OpenCV inicializálása és a webkamera megnyitása
cap = cv2.VideoCapture(0)

# A zárósapka sablonjának betöltése
template = cv2.imread('template_cap.png', 0)  # Előzetesen készített sablonkép betöltése

# A sablon méretének meghatározása
w, h = template.shape[::-1]

while True:
    # A következő képkocka beolvasása
    ret, frame = cap.read()

    # Ha nem sikerült beolvasni a képkockát, kilépés a ciklusból
    if not ret:
        break

    # A képkocka szürkeárnyalatosra konvertálása
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # A sablon felismerése a képkockán
    res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Küszöbérték beállítása a találatokhoz
    loc = cv2.findNonZero((res >= threshold).astype(int))

    # Ha található zárósapka a képen
    if loc is not None:
        # Zárósapka helyzetének meghatározása és körülkeretezése
        for pt in loc:
            cv2.rectangle(frame, (pt[0][0], pt[0][1]), (pt[0][0] + w, pt[0][1] + h), (0, 255, 255), 2)

        # Eredmény megjelenítése
        cv2.imshow('Result', frame)
    else:
        cv2.imshow('Result', gray_frame)

    # Kilépés a ciklusból, ha a felhasználó megnyomta a 'q' billentyűt
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bezárása és ablakok bezárása
cap.release()
cv2.destroyAllWindows()
