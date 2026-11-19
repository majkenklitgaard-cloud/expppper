serial.redirectToUSB()
MFRC522.Init()
basic.forever(function () {
    serial.writeLine("" + (MFRC522.getID()))
    if (MFRC522.getID() != 0) {
        for (let index = 0; index < 1; index++) {
            // full speed
            pins.servoWritePin(AnalogPin.P8, 180)
            // 180° turn, tune this
            basic.pause(500)
            // full speed
            pins.servoWritePin(AnalogPin.P8, 68)
            // 180° turn, tune this
            basic.pause(100)
        }
    }
    basic.pause(50)
})
