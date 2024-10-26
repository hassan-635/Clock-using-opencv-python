import cv2                          # modules used in code
import datetime
import math

# ___________________________________________________________________________________


colors = {                           # dictionary for color codes used in clock
    'blue': (255, 0, 0),
    'green': (0, 255, 0),
    'red': (0, 0, 255),
    'yellow': (0, 255, 255),
    'magenta': (255, 0, 255),
    'cyan': (255, 255, 0),
    'white': (255, 255, 255),
    'amber': (255, 191, 0),
    'gray': (125, 125, 125),
    'dark_gray': (50, 50, 50),
    'light_gray': (220, 220, 220),
    'black': (0, 0, 0)
}

# ___________________________________________________________________________________



radius = 250                      # radius of clock
center = (300, 300)               # center(x, y) of clock

# ___________________________________________________________________________________



def get_drawing():
    hours_init = []
    hours_dest = []
    for i in range (0, 360, 6):
        x_coord = int(center[0] + radius * math.cos(i * math.pi/180)) #x = r cos theta
        y_coord = int(center[1] + radius * math.sin(i * math.pi/180)) #y = r sin theta
        hours_init.append((x_coord, y_coord))

    for i in range (0, 360, 6):
        x_coord = int(center[0] + (radius - 20) * math.cos(i * math.pi/180))
        y_coord = int(center[1] + (radius - 20) * math.sin(i * math.pi/180))
        hours_dest.append((x_coord, y_coord))

    return hours_init, hours_dest


# ___________________________________________________________________________________

def get_date():
    dt = datetime.datetime.now()
    day = dt.strftime('%A')
    date = dt.strftime('%b'" "'%d'","'%Y')
    return ((day, date))

# ___________________________________________________________________________________


def draw_digital_time(image):
    tm = datetime.datetime.now().time()
    hour = str(int(math.fmod(tm.hour, 12)))
    minute = str(tm.minute)
    second = str(tm.second)
    t = tm.strftime('%p')

    cv2.putText(image, f"{hour.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}", (170, 450), cv2.FONT_HERSHEY_DUPLEX, 2, colors['black'], 1, cv2.LINE_AA)
    cv2.putText(image, f"{t.upper()}", (280, 500), cv2.FONT_HERSHEY_DUPLEX, 1.5, colors['black'], 1, cv2.LINE_AA)
    return image

# ___________________________________________________________________________________


def draw_analog_time(image):
    tm = datetime.datetime.now().time()
    hour = math.fmod(tm.hour, 12)
    minute = tm.minute
    second = tm.second

    #finding angles for hands
    second_angle = math.fmod(second * 6 + 270, 360)
    minute_angle = math.fmod(minute * 6 + 270, 360)
    hour_angle = math.fmod((hour*30)+(minute/2)+270, 360)

    #drawing hands of clock

    second_x = int(center[0] + (radius-25) * math.cos(second_angle * math.pi/180))
    second_y = int(center[1] + (radius-25) * math.sin(second_angle * math.pi/180))
    cv2.line(image, center, (second_x, second_y), colors['red'], 2, cv2.LINE_AA)

    minute_x = int(center[0] + (radius-75) * math.cos(minute_angle * math.pi/180))
    minute_y = int(center[1] + (radius-75) * math.sin(minute_angle * math.pi/180))
    cv2.line(image, center, (minute_x, minute_y), colors['green'], 3, cv2.LINE_AA)

    hour_x = int(center[0] + (radius-125) * math.cos(hour_angle * math.pi/180))
    hour_y = int(center[1] + (radius-125) * math.sin(hour_angle * math.pi/180))
    cv2.line(image, center, (hour_x, hour_y), colors['black'], 5, cv2.LINE_AA)

    return image


