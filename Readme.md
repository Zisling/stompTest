# STOMP TEST
This is a test for bgu spl stomp server

To run this code you need to install the following:
1. Linux or The VM or The given docker.
2. python 3.6 or above. if you don't have it install it
3. install stomp.py

## How to run
1. Run you server on port 7777
2. Then run the fallowing command in the terminal:
   
 
    python3 stompTest.py

3. You should see the following output:
   

    connection number 2 received an error
    <THE ERROR FRAME YOU SENT>
    I must not fear.
    Fear is the mind-killer.
    Fear is the little-death that brings total obliteration.
    I will face my fear.
    I will permit it to pass over me and through me.
    And when it has gone past I will turn the inner eye to see its path.
    Where the fear has gone there will be nothing.
    Only I will remain.
    --- Frank Herbert, Dune

### How To install stomp.py

    pip3 install stomp.py

make sure you have python installed


### Extra

You can change the ip and the port for the tests by running:

    python3 stompTest.py --ip <ip> --port <port>