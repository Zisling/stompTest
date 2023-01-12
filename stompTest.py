import time
import stomp
import argparse


def connect_and_subscribe(conn, name, password, topic):
    conn.connect(name, password, wait=True)
    conn.subscribe(destination=topic, id=1)


class MyListener(stomp.ConnectionListener):
    def __init__(self, conn, id_num):
        self.conn = conn
        self.id = id_num

    def on_error(self, frame):
        print('connection number %d received an error\n%s' % (self.id, frame))

    def on_message(self, frame):
        if self.id == 1:
            print('%s' % frame.body)

    def on_disconnected(self):
        print('disconnected')


def parse_args():
    parser = argparse.ArgumentParser(description='STOMP client')
    parser.add_argument('-ip', '--ip', type=str, default='localhost', help='IP address of the server')
    parser.add_argument('-p', '--port', type=int, default=7777, help='Port of the server')
    parser.add_argument('--doubleLogin', action='store_true', help='Enable user double login check')
    return parser.parse_args()


dune_quote = '''I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past I will turn the inner eye to see its path.
Where the fear has gone there will be nothing.
Only I will remain.
--- Frank Herbert, Dune'''
con2_message = 'conn 2 should not be connected and send this message'
if __name__ == '__main__':
    args = parse_args()
    ip_port = [(args.ip, args.port)]
    conn1 = stomp.Connection12(ip_port)
    if args.doubleLogin:
        conn2 = stomp.Connection12(ip_port)
    else:
        conn2 = None
    conn3 = stomp.Connection12(ip_port)
    conn4 = stomp.Connection12(ip_port)
    active_cons = [conn1, conn3, conn4]

    conn1.set_listener('', MyListener(conn1, 1))
    if conn2 is not None:
        conn2.set_listener('', MyListener(conn2, 2))
    conn3.set_listener('', MyListener(conn3, 3))
    conn4.set_listener('', MyListener(conn4, 4))
    time.sleep(1)
    connect_and_subscribe(conn1, 'Paul', 'Atreides', '/dune')
    if conn2 is not None:  # should result in error frame
        connect_and_subscribe(conn2, 'Paul', 'Atreides', '/dune')

    connect_and_subscribe(conn3, 'Alia', 'OfTheKnife', '/dune')
    connect_and_subscribe(conn4, 'Lady', 'Jessica', '/dune')
    time.sleep(1)
    dune_quote_split = dune_quote.split('\n')

    if conn2 is not None and conn2.is_connected():
        conn2.send(body=con2_message, destination='/dune')
        time.sleep(0.5)
    for i, line in enumerate(dune_quote_split):
        active_cons[i % 3].send(body=line, destination='/dune')
        time.sleep(0.5)

    time.sleep(1)
    for con in active_cons:
        if con.is_connected():
            con.disconnect()
    if conn2 is not None and conn2.is_connected():
        print('conn 2 should not be connected and we disconnected it')
        conn2.disconnect()
