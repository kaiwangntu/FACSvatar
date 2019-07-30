# CC0
# Stef van der Struijk

import sys
import zmq
import time


def main(ip="127.0.0.1"):
    # ZMQ connection
    url = "tcp://{}:5550".format(ip)
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.bind(url)  # publisher connects to subscriber
    print("Pub connected to: {}\nSending data...".format(url))

    i = 0

    while True:
        topic = 'foo'.encode('ascii')
        user_msg = input("Please type a message to send: ")
        msg = user_msg.encode('utf-8')
        # publish data
        socket.send_multipart([topic, msg])  # 'test'.format(i)
        print("On topic {}, send data: {}".format(topic, msg))
        # time.sleep(.5)

        i += 1


if __name__ == "__main__":
    # pass ip argument
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()