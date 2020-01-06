import os
import time
import stomp

def connect_and_subscribe(conn,name,password,Topic):
    global x
    x = 1
    conn.connect(name, password, wait=False)
    conn.subscribe(destination=Topic, id=x)
    x += 1


class MyListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_error(self, headers, message):
        print('received an error "%s"' % headers)
        print('body: "%s"' % message)


    def on_message(self, headers, message):
        print('received a message "%s"' % message)
        for y in range(1):
            # print(y)
            time.sleep(1)
        print('processed message')

    def on_disconnected(self):
        print('disconnected')

conn1 = stomp.Connection12([('localhost', 7777)])
conn2 = stomp.Connection12([('localhost', 7777)])
conn3 = stomp.Connection12([('localhost', 7777)])
conn4 = stomp.Connection12([('localhost', 7777)])
conn1.set_listener('', MyListener(conn1))
conn2.set_listener('', MyListener(conn2))
time.sleep(2)
# conn3.set_listener('', MyListener(conn3))
# conn4.set_listener('', MyListener(conn4))
connect_and_subscribe(conn1,'zisling','password','/wicther')
time.sleep(0.1)
connect_and_subscribe(conn2,'zisling','password','/wicther')
connect_and_subscribe(conn3,'hedi','password','/wicther')
connect_and_subscribe(conn4,'Geralt','password','/wicther')
conn1.send('/wicther',"When a humble bard Graced a ride along With Geralt of Rivia Along came this song")
time.sleep(0.5)
if conn2.is_connected():
    conn2.send('/wicther',"From when the White Wolf fought A silver-tongued devil His army of elves At his hooves did they revel")
time.sleep(0.5)
conn3.send('/wicther',"They came after me With masterful deceit Broke down my lute And they kicked in my teeth")
time.sleep(0.5)
conn4.send('/wicther','While the devil’s horns Minced our tender meat And so cried the Witcher He can’t be bleat')
time.sleep(0.5)
conn1.send('/wicther','Toss a coin to your Witcher O Valley of Plenty O Valley of Plenty, ohToss a coin to Your Witcher O Valley of Plenty')
time.sleep(0.5)
if conn2.is_connected():
    conn2.send('/wicther','At the edge of the world Fight the mighty horde That bashes and breaks you And brings you to mourn')
time.sleep(0.5)
conn3.send('/wicther','He thrust every elf Far back on the shelf High up on the mountain From whence it came')
time.sleep(0.5)
conn4.send('/wicther','He wiped out your pest Got kicked in his chest He’s a friend of humanity So give him the rest')
time.sleep(0.5)
conn1.send('/wicther','That’s my epic tale: A champion prevailed Defeated the villain Now pour him some ale')
time.sleep(0.5)
if conn2.is_connected():
    conn2.send('/wicther',"Toss a coin to your Witcher O' Valley of Plenty O' Valley of Plenty, oh Toss a coin to your Witcher A friend of humanity")
time.sleep(0.5)
conn3.send('/wicther',"Toss a coin to your Witcher O' Valley of Plenty O' Valley of Plenty, oh Toss a coin to your Witcher A friend of humanity")
time.sleep(0.5)
conn4.send('/wicther',"Toss a coin to your Witcher O' Valley of Plenty O' Valley of Plenty, oh Toss a coin to your Witcher A friend of humanity")
time.sleep(10)
conn1.disconnect()
if conn2.is_connected():
    conn2.disconnect()
conn3.disconnect()
conn4.disconnect()
