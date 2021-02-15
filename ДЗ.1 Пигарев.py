duration = int(input())
if duration <60:
    print(duration, 'sec')
elif duration >=60 and duration <3600:
    print(duration//60, 'min', duration%60, 'sec')
elif duration >=3600 and duration<86400:
    print(duration//3600, 'hour', (duration-3600*(duration//3600))//60, 'min', (duration-3600*(duration//3600))%60,'sec')
elif duration >= 86400:
    print(duration//86400, 'days', (duration-86400*(duration//86400))//3600, 'hour',
    ((duration-86400*(duration//86400))-3600*((duration-86400*(duration//86400))//3600))//60, 'min',
    ((duration-86400*(duration//86400))-3600*((duration-86400*(duration//86400))//3600))%60, 'sec')