class Device:
    ipAddr=""
    port=""

    @staticmethod
    def findDevices():
        devices = []

        d = Device()
        d.ipAddr = "192.168.1.1"
        d.port = "2001"

        devices.append(d)


        d = Device()
        d.ipAddr = "192.168.1.50"
        d.port = "7091"

        devices.append(d)


        d = Device()
        d.ipAddr = "192.168.1.100"
        d.port = "80"

        devices.append(d)

        return devices


class deviceView:

    def showDevices(self, devices):

        for d in devices:
            print("--------------")
            print("Ip Address: " + str(d.ipAddr))
            print("Port: " + str(d.port))
            print("--------------")


class DevicesController:

    def __init__(self):
        devices = Device.findDevices()

        v = deviceView()
        v.showDevices(devices)

c = DevicesController()




