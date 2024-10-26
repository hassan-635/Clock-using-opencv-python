import cv2
import numpy as np
from analog_values import colors, get_drawing, center, radius, get_date, draw_digital_time, draw_analog_time

# ___________________________________________________________________________________

canvas = np.ones((600, 600, 3))
hours_init, hours_dest = get_drawing()
date = get_date()

# ___________________________________________________________________________________


for i in range (len(hours_init)):
    if i % 5 == 0:
        cv2.line(canvas, hours_init[i], hours_dest[i], colors['magenta'], 5, cv2.LINE_AA)
    else:
        cv2.circle(canvas, hours_init[i], 5, colors['red'], -1)

# ___________________________________________________________________________________

cv2.circle(canvas, center, radius + 10 , colors['black'], 3, cv2.LINE_AA)
cv2.putText(canvas, "HASNI", (160, 220), cv2.FONT_HERSHEY_TRIPLEX, 3, colors['black'], 1, cv2.LINE_AA)
cv2.putText(canvas, date[0], (120, 260), cv2.FONT_HERSHEY_DUPLEX, 1, colors['black'], 1, cv2.LINE_AA)
cv2.putText(canvas, date[1], (300, 260), cv2.FONT_HERSHEY_DUPLEX, 1, colors['black'], 1, cv2.LINE_AA)
cv2.putText(canvas, "CodeIt", (245, 130), cv2.FONT_HERSHEY_DUPLEX, 1, colors['black'], 1, cv2.LINE_AA)

# ___________________________________________________________________________________

while True:
    canvas_original = canvas.copy()
    digital_face = draw_digital_time(canvas_original)
    analog_face = draw_analog_time(canvas_original)
    cv2.circle(canvas, center, 8, colors['black'], -1, cv2.LINE_AA)
    cv2.imshow("CLOCK", canvas_original)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
