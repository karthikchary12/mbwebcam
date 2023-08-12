import requests
import cv2
import numpy as np
import imutils
import time

ip = input("Enter your IP webcam URL: ")
suf = "/shot.jpg"
url = ip + suf

cv2.namedWindow("Android_cam", cv2.WINDOW_NORMAL)  # Create a named window

try:
    while True:
        try:
            img_resp = requests.get(url, timeout=10)
            img_arr = np.frombuffer(img_resp.content, dtype=np.uint8)
            img = cv2.imdecode(img_arr, cv2.IMREAD_UNCHANGED)
            img = imutils.resize(img, width=1000, height=1800)
            cv2.imshow("Android_cam", img)

            # Press 'q' key to exit
            if cv2.waitKey(1) == ord('q'):
                break

        except requests.ConnectionError as e:
            print("Connection error:", e)
            time.sleep(5)  # Wait for a moment before trying again

except KeyboardInterrupt:
    pass  # Allow clean exit on Ctrl+C

cv2.destroyAllWindows()
