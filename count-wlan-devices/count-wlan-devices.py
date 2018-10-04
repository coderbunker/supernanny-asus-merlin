import subprocess
from influxdb import InfluxDBClient

location = "coderbunker"
targets = [
    ["10.1.0.1", "22"],
    ["10.1.0.27", "22"],
    ["10.1.0.59", "47000"],
    ["10.1.0.93", "22"],
    ["10.1.0.191", "22"],
]


# device_count
def writeToInflux(json_body):
    client = InfluxDBClient('206.189.45.190', 8086, 'test')
    client.write_points(json_body)



def getMacCount(ip, port):
    # This command could have multiple commands separated by a new line \n
    command = 'ssh admin@{0} -p {1} -o StrictHostKeyChecking=no "wl assoclist"'.format(ip,port)
    print(command)

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()

    # This makes the wait possible
    p_status = p.wait()

    # Return the amount of devices connected
    return len(output.splitlines())


def main():
    myjson = {
            "measurement": "wlan-device-count",
            "tags": {
                "location": location,
                "ip": ip
            },
            "fields": {
                "macs": count
            }
        }
    json_body = []
    for t in targets:
        count = getMacCount(t[0], t[1])
        json_body.append(myjson.format(location, t[0], count))
    writeToInflux(json_body)

if __name__== "__main__":
    main()