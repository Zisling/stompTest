import os
import time
import stomp

def connect_and_subscribe(conn,name,password):
    conn.connect(name, password, wait=True)
    conn.subscribe(destination='/queue/test', id=1)

class MyListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)
        for x in range(10):
            print(x)
            time.sleep(1)
        print('processed message')

    def on_disconnected(self):
        print('disconnected')
        connect_and_subscribe(self.conn)

conn = stomp.Connection12([('localhost', 7777)])
conn.set_listener('', MyListener(conn))
connect_and_subscribe(conn,'zisling','password')
conn.send('/queue/test','i am gery from tvria')
time.sleep(2)
conn.disconnect()