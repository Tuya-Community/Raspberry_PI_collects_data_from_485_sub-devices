# -*- coding: utf-8 -*-
from new_relay_control import relay
from time import sleep


#温湿度获取

def temp_hum_sensor_get():
    temp_hum = relay()
    temp_hum.all_relay = 3
    temp_hum.relay_all_on_order = ['01 04 00 00 00 02 71 CB']
    return_str = temp_hum.ALL_ON()
    return return_str


#门磁开关获取

def door_sensor_get():
    door_sensor = relay()
    door_sensor.all_relay = 3
    door_sensor.relay_all_on_order = ['FE 01 00 00 00 02 A9 C4']
    return_str = door_sensor.ALL_ON()
    return return_str

id_value =2
action =1
time = 1



if id_value == 1:

    relay_open = relay()

    if action == 1:
        return_str = relay_open.ALL_ON()
    else:
        return_str = relay_open.ALL_OFF()

    relay_str = return_str[8:12]
    if relay_str == "FF00":
        relay_state = 1
    else:
        relay_state = 0

    print(relay_str)
    print(relay_state)


if id_value == 2:

    while True:

        return_str = temp_hum_sensor_get()
        print(return_str)

        get_str1 = return_str[6:10]
        get_str2 = return_str[10:14]
        try:
            temp_data = (int(get_str1, 16)) / 10
            hum_data = (int(get_str2, 16)) / 10
        except ValueError:
            pass

        final_str2 = get_str1 + ' ' + get_str2
        print(final_str2)
        print(temp_data)
        print(hum_data)
        sleep(time)


if id_value == 3:
    while True:
        return_str = door_sensor_get()
        get_str3 = return_str[6:8]
        print(get_str3)
        sleep(time)

