led.enable(False)
# station chip-present flags (turn the servo only once per scan)
present1 = False
present2 = False
present3 = False
present4 = False
# one 180° turn
# stop
def turnHalf(servo: AnalogPin):
    pins.servo_write_pin(servo, 110)
    # spin
    basic.pause(90)
    # 180°
    pins.servo_write_pin(servo, 90)
# reader select pins (SDA): all high = no reader active
pins.digital_write_pin(DigitalPin.P0, 1)
pins.digital_write_pin(DigitalPin.P1, 1)
pins.digital_write_pin(DigitalPin.P2, 1)
pins.digital_write_pin(DigitalPin.P10, 1)
# servos stopped at start
pins.servo_write_pin(AnalogPin.P8, 90)
pins.servo_write_pin(AnalogPin.P9, 90)
pins.servo_write_pin(AnalogPin.P12, 90)
pins.servo_write_pin(AnalogPin.P16, 90)
MFRC522.init()
# <- your extension's init block

def on_forever():
    global present1, present2, present3, present4
    # station 1: reader P0 -> servo P8
    pins.digital_write_pin(DigitalPin.P0, 0)
    id1 = MFRC522.get_id()
    # <- your extension's read-ID block
    pins.digital_write_pin(DigitalPin.P0, 1)
    if id1 != "":
        if not present1:
            present1 = True
            turnHalf(AnalogPin.P8)
    else:
        present1 = False
    # station 2: reader P1 -> servo P9
    pins.digital_write_pin(DigitalPin.P1, 0)
    id2 = MFRC522.get_id()
    pins.digital_write_pin(DigitalPin.P1, 1)
    if id2 != "":
        if not present2:
            present2 = True
            turnHalf(AnalogPin.P9)
    else:
        present2 = False
    # station 3: reader P2 -> servo P12
    pins.digital_write_pin(DigitalPin.P2, 0)
    id3 = MFRC522.get_id()
    pins.digital_write_pin(DigitalPin.P2, 1)
    if id3 != "":
        if not present3:
            present3 = True
            turnHalf(AnalogPin.P12)
    else:
        present3 = False
    # station 4: reader P10 -> servo P16
    pins.digital_write_pin(DigitalPin.P10, 0)
    id4 = MFRC522.get_id()
    pins.digital_write_pin(DigitalPin.P10, 1)
    if id4 != "":
        if not present4:
            present4 = True
            turnHalf(AnalogPin.P16)
    else:
        present4 = False
basic.forever(on_forever)
