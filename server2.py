import socket
from _thread import *
import pickle
from game import Game

PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(ADDR)
except socket.error as e:
    str(e)

server.listen(2)
print("SERVER UP: Waiting for Connections..")

# this will carry the game instances
games = {}
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount

    # When a connection is made initially, send back player object
    # Before sending -> encode and serialize data
    # check if p is 0 or 1, odd or even. this will determine what player to send back
    # this sends back player position
    if p % 2 == 0:
        conn.send(pickle.dumps(games[gameId].player1))
    else:
        conn.send(pickle.dumps(games[gameId].player2))

    reply = ""
    while True:
        try:
            # this should be the current players position
            data = pickle.loads(conn.recv(2048))

            if not data:
                print("Disconnected, Server didnt receive data")
                break
            # put this into the games object, players position
            # check which player
            if p % 2 == 0:
                games[gameId].player1 = data
            else:
                games[gameId].player2 = data

            if p % 2 == 0:
                reply = games[gameId].player2
            else:
                reply = games[gameId].player1

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = server.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))
