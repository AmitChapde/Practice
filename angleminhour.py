def calc_angle(h,m):
    if(h<0 or m<0 or h>12 or m>60):
        print("wrong input")

    if h==12:
        h=0
    if m==60:
        m=0
        h+=1
        if h>12:
            h=h-12

    #calculate angle moved by hour hand and minute hand
    hour_hand=(0.5*(h*60+m))
    minute_hand=6*m

    #difference between two angles
    angle=abs(hour_hand-minute_hand)
    #Return the smaller angle of two possible angles
    angle=min(360-angle,angle)
    return angle

k=calc_angle(3,30)
print(k)
        




