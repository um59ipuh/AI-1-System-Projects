# Helper functions are written here

import json


class Utils:

    @staticmethod
    def remove_spaces(s: str) -> str:
        new_s = ""
        for c in s:
            if not c.isspace():
                new_s += c
        return new_s


class BoardReader:

    @staticmethod
    def read_json_board(path="board.json"):
        board = {}
        with open(path, 'r') as f:
            data = json.load(f)
            for pos in data:
                coordinate = list(pos.keys())[0]
                infos = pos[coordinate]
                board[coordinate] = infos
        return board


class BoardHelper:

    # TODO: Update board's peg positions based on new information coming from network call
    @staticmethod
    def reset_update(board, peg_pos):
        # reset board
        res_board = BoardHelper.reset_board(board)
        # update board
        for key, value in peg_pos.items():
            for val in value:
                res_board[val]['hold'] = key
        return res_board

    @staticmethod
    def update(board, peg_pos):
        for key, value in peg_pos.items():
            for val in value:
                board[val]['hold'] = key
        return board

    @staticmethod
    def extract_formatted_positions(positions: str) -> {str: [str]}:
        all_pegs = positions.split(":")
        a_pegs = [Utils.remove_spaces(pos) for pos in all_pegs[0].split(";")]
        next_pegs = [Utils.remove_spaces(pos) for pos in all_pegs[1].split(";")]
        last_pegs = [Utils.remove_spaces(pos) for pos in all_pegs[2].split(";")]

        return {"A": a_pegs, "B": next_pegs, "C": last_pegs}

    @staticmethod
    def reset_board(board):
        for key, value in board.items():
            value['hold'] = None
        return board