"""
    To use this implementation, you simply have to implement `get_move` such that it returns a legal move.
    You can then let your agent compete on the server by calling
        python3 client_simple.py path/to/your/config.json
"""

import json
import requests
import time
import sys
from helper import *
from checker import *


def position_split(position):
    'splits the position data into a list of lists of coordinates'
    #format: [[(x,y),(x,y)],[(x,y),(x,y)],[(x,y),(x,y)]]
    players = position.split(":")
    coords = []
    for x in players:
        coords.append(x.split(";"))
    return coords


def get_move(position):
    # increase limit
    sys.setrecursionlimit(2000)

    positions = BoardHelper.extract_formatted_positions(position)

    cc = ChineseChecker()
    cc.board = BoardHelper.reset_update(cc.board, positions)

    move = []
    if cc.is_initial(positions["A"], 0):
        move = cc.static_move()
    else:
        move = cc.get_next_move_of_mine(positions)

    move_str = ";".join(move)

    return move_str
    # raise NotImplementedError()


def run(config_file):
    # load configuration
    with open(config_file, 'r') as fp:
        config = json.load(fp)

    moves = []
    while True:
        # send request
        print('Sending moves', moves)
        response = requests.put(f'{config["url"]}/play/{config["tournament"]}', json={
            'name': config['name'],
            'pwd': config['pwd'],
            'moves': moves,
        })
        print('Response status:', response.status_code)
        print('Response text:', response.text)
        if response.status_code == 200:
            positions = response.json()['positions']
            if not positions:  # if the server has no positions:
                time.sleep(1)  # wait a moment to avoid overloading the server and then try again
            # get moves for next request
            moves = []
            for position in positions:
                moves.append({'id': position['id'], 'move': get_move(position['position'])})
        elif response.status_code == 503:
            time.sleep(3)  # server is busy - wait a moment and then try again
        else:
            print('Stopping')  # other errors (e.g. authentication problems) do not benefit from a retry
            break


if __name__ == '__main__':
    import sys
    run(sys.argv[1])

