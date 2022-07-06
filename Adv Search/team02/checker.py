# Game play for chinese checker

import copy
from helper import *

CONNECTED_COORDINATES = "conn_coors"
HEURISTIC = "heuristic"
TYPE = "type"
HOLD = "hold"

peg_turn = {"A": 0, "B": 1, "C": 2}
turn_peg = {0: "A", 1: "B", 2: "C"}


class ChineseChecker:

    def __init__(self):
        # initiate board
        self.board = BoardReader.read_json_board()

    # turn = 0:my, 1:next, 2:last
    def next_position_by_simple_move(self, cord, turn):
        adj_pos = self.board[cord][CONNECTED_COORDINATES]
        best_move = None
        for pos in adj_pos:
            if self.board[pos][HOLD] == None:
                if best_move == None:
                    best_move = pos
                if self.board[best_move][HEURISTIC][turn] > self.board[pos][HEURISTIC][turn]:
                    best_move = pos

        return best_move

    def is_swappable(self, moving_to, turn):
        to_peg = self.board[moving_to]
        home_peg = f"{turn_peg[turn]}_home"

        # swap condition
        if to_peg[TYPE] == home_peg and to_peg[HOLD] != turn_peg[turn]:
            return True
        else:
            return False

    # is_any_peg is already upper part of home or not
    def peg_in_stuck(self, peg: str, turn) -> bool:
        adj_pos = self.board[peg][CONNECTED_COORDINATES]
        for next_peg in adj_pos:
            if self.board[next_peg][HOLD]:
                hop_peg = self.is_jump_possible(peg, next_peg, turn)
                if hop_peg[1] == 1 or hop_peg[1] == 0:
                    return False
                continue
            else:
                return False
        return True

    # is_in_desired_place
    def peg_in_goal(self, peg: str, turn) -> bool:
        peg_pos = self.board[peg]
        peg_home = f"{turn_peg[turn]}_home"

        if peg_pos[TYPE] != peg_home:
            return False

        adj_pos = [pos for pos in peg_pos[CONNECTED_COORDINATES] if self.board[pos][HEURISTIC][turn] < peg_pos[HEURISTIC][turn]]
        for next_peg in adj_pos:
            if self.board[next_peg][HOLD]:
                hop_peg = self.is_jump_possible(peg, next_peg, set(), turn)
                if hop_peg[1] == 1:
                    return False
                elif hop_peg[1] == 0:
                    if self.is_swappable(hop_peg[0], turn):
                        return False
            else:
                return False
        return True

    # is all peg are in home
    def is_win(self, positions, turn):
        peg_home = f"{turn_peg[turn]}_home"
        for pos in positions:
            if self.board[pos][TYPE] != peg_home:
                return False
        return True

    def static_move(self):
        # for dynamic behaviour we have to code it like S shaped
        if self.board["1,-4"][HOLD] == "A":
            return ["1,-4", "1,-3"]
        elif self.board["3,-6"][HOLD] == "A":
            return ["3,-6", "1,-4", "1,-2"]
        elif self.board["2,-5"][HOLD] == "A":
            return ["2,-5", "2,-3", "0,-1"]
        elif self.board["3,-4"][HOLD] == "A":
            return ["3,-4", "2,-3"]

    def is_initial(self, positions: [str], turn) -> bool:
        peg_name = turn_peg[turn]
        start_peg = f"{peg_name}_start"
        return \
            len([pos for pos in positions
                 if self.board[pos][HOLD] == peg_name
                 and self.board[pos][TYPE] == start_peg]) > 2

    # Initially just check if there any enemy peg surrounding here or not
    def is_eligible_for_ai_move(self, positions: [str]) -> bool:
        for pos in positions:
            adj_pos = self.board[pos][CONNECTED_COORDINATES]
            for p in adj_pos:
                peg_pos = self.board[p][HOLD]
                if peg_pos == "B" or peg_pos == "C":
                    return True
        return False

    # Is jump is possible then send it with appropriate value
    def is_jump_possible(self, jp: str, hp: str, peg_set, turn):
        jumping_peg = jp.split(",")
        jp_x = int(jumping_peg[0])
        jp_y = int(jumping_peg[1])
        helper_peg = hp.split(",")
        hp_x = int(helper_peg[0])
        hp_y = int(helper_peg[1])

        x_diff = hp_x - jp_x
        y_diff = hp_y - jp_y

        hoping_pos = f"{hp_x + x_diff},{hp_y + y_diff}"

        if hoping_pos not in peg_set:
            if hoping_pos in self.board and hoping_pos in self.board[hp][CONNECTED_COORDINATES]:
                if self.board[hoping_pos][HOLD] is None:
                    return hoping_pos, 1 # clear to jump
                else:
                    return hoping_pos, 0 # needs to swap
        return hoping_pos, -1  # invalid jump position

    # checks if this position is final pos for hop chain or not ?
    def is_stop_for_hop_chain(self, peg_set, moving_cord, pre_hp_cord, turn):
        adj_pos = self.board[moving_cord][CONNECTED_COORDINATES]
        for pos in adj_pos:
            if self.board[pos][HOLD] is not None and pos != pre_hp_cord:
                hop_pos = self.is_jump_possible(moving_cord, pos, peg_set, turn)
                if hop_pos[1] == 1 and hop_pos[0] not in peg_set:
                    return False
        return True

    def moving_by_hop_chain(self, peg_set, curr_cord, pre_hp_cord, turn):
        if self.is_stop_for_hop_chain(peg_set, curr_cord, pre_hp_cord, turn):
            return [self.board[curr_cord][HEURISTIC][turn], [curr_cord]]

        possible_moves = []
        adj_pos = copy.deepcopy(self.board[curr_cord][CONNECTED_COORDINATES])
        # adj_pos.remove(pre_hp_cord)

        for pos in adj_pos:
            if pos != pre_hp_cord:
                possible_moves.append([self.board[curr_cord][HEURISTIC][turn], [curr_cord]])
                if self.board[pos][HOLD] is not None:
                    jump_pos = self.is_jump_possible(curr_cord, pos, peg_set, turn)
                    if jump_pos[1] == 1:
                        peg_set.add(curr_cord)
                        moving_pos_for_jump = self.moving_by_hop_chain(peg_set, jump_pos[0], pos, turn)
                        moving_pos_for_jump[1] = [curr_cord] + moving_pos_for_jump[1]
                        possible_moves.append([moving_pos_for_jump[0], moving_pos_for_jump[1]])
                    elif jump_pos[1] == 0:
                        # check if swap is possible or not?
                        if self.is_swappable(jump_pos[0], turn):
                            possible_moves.append([self.board[jump_pos[0]][HEURISTIC][turn], [curr_cord, jump_pos[0]]])
        possible_moves.sort(key=lambda x: x[0])  # sort based on heuristic value
        # print(f"Returnable: {possible_moves}")
        return possible_moves[0]  # first tuple -> first value

    # just needs to return path
    def next_move_for_one_peg(self, peg_pos: str, turn, need_all_moves= False) -> ():
        adj_pos = self.board[peg_pos][CONNECTED_COORDINATES]

        possible_moves = {}
        for a_pos in adj_pos:
            # jump possible & also check for is swap rule applicable or not?
            if self.board[a_pos][HOLD] is not None:
                hop_pos = self.is_jump_possible(peg_pos, a_pos, set(), turn)
                if hop_pos[1] == 1:
                    peg_set = set()
                    peg_set.add(peg_pos)
                    hop_chain_pos = self.moving_by_hop_chain(peg_set, hop_pos[0], a_pos, turn)
                    possible_moves[hop_chain_pos[1][-1]] = (hop_chain_pos[0], ([peg_pos] + hop_chain_pos[1]), 'H')
                elif hop_pos[1] == 0:
                    if self.is_swappable(hop_pos[0], turn):
                        possible_moves[hop_pos[0]] = (self.board[hop_pos[0]][HEURISTIC][turn], [peg_pos, hop_pos[0]], 'H')
                # check single move and if swap possible or not?
                elif self.is_swappable(a_pos, turn):
                    possible_moves[a_pos] = (self.board[a_pos][HEURISTIC][turn], [peg_pos, a_pos], 'S')

            # jump not possible, check for single move
            else:
                possible_moves[a_pos] = (self.board[a_pos][HEURISTIC][turn], [peg_pos, a_pos], 'S')

        if need_all_moves:
            return [move[1] for move in list(possible_moves.values())]

        sorted_move = list(possible_moves.values())
        sorted_move.sort(key=lambda x: x[0])

        if len(sorted_move) > 0:
            opt_move = sorted_move[0]  # minimum heuristics
        else:
            return []

        return opt_move[1][-1], opt_move

    def cal_game_adv_score(self, pegs: [str], turn) -> float:
        return sum([self.board[peg][HEURISTIC][turn] for peg in pegs if peg])

    def get_next_move(self, peg_curr_pos, turn):

        # curr_game_score = self.cal_game_adv_score(peg_curr_pos, turn)

        peg_score = {}
        for peg in peg_curr_pos:
            next_move = self.next_move_for_one_peg(peg, turn)
            if len(next_move) == 0:
                continue
            game_adv = self.board[peg][HEURISTIC][turn] - self.board[next_move[0]][HEURISTIC][turn]
            peg_score[peg] = (peg, next_move[1][1], game_adv)

        sorted_score = list(peg_score.values())
        sorted_score.sort(key=lambda x: x[2], reverse=True)

        return sorted_score[0] if len(sorted_score) > 0 else []

    def swap_positions(self, move_form, move_to):
        peg1 = self.board[move_form]
        peg2 = self.board[move_to]
        # just swap in place, nothing to return
        peg1[HOLD], peg2[HOLD] = peg2[HOLD], peg1[HOLD]

    def working_pegs(self, positions):
        new_positions = {}
        for key, value in positions.items():
            for pos in value:
                if not self.peg_in_goal(pos, peg_turn[key]):
                    if key in new_positions:
                        new_positions[key].append(pos)
                    else:
                        new_positions[key] = [pos]
        return new_positions

    def change_pos(self, moves, temp_pos):
        for key, val in moves.items():
            start, end = val[0], val[-1]
            index = temp_pos[key].index(start)
            temp_pos[key][index] = end
        return temp_pos

    def cal_future_move(self, temp_pos: {}, upto: int = 1):
        glb_con = 0
        total_score = []
        for itr in range(upto):
            wrk_pos = self.working_pegs(temp_pos)
            move_score = []
            for peg in wrk_pos['A']:
                loc_con = 0
                self.board = BoardHelper.reset_update(self.board, temp_pos)

                three_moves = {}

                next_A = self.cal_move_for_one_A(peg)  # (move, cont)
                if next_A is None:
                    continue
                loc_con = next_A[1]
                three_moves['A'] = next_A[0]

                if 'B' in wrk_pos:
                    next_B = self.cal_move_for_other_peg(wrk_pos['B'], 1)
                    if next_B is not None:
                        # loc_con += (1/next_B[1]) if next_B[1] else 1
                        loc_con -= .5 * next_B[1]
                        three_moves['B'] = next_B[0]

                if 'C' in wrk_pos:
                    next_C = self.cal_move_for_other_peg(wrk_pos['C'], 2)
                    if next_C is not None:
                        # loc_con += (1/next_C[1]) if next_C[1] else 1
                        loc_con -= .5 * next_C[1]
                        three_moves['C'] = next_C[0]

                move_score.append((three_moves, loc_con))

            move_score.sort(key=lambda x: x[1], reverse=True)
            self.board = BoardHelper.reset_update(self.board, temp_pos)

            # replace pos
            temp_pos = self.change_pos(move_score[0][0], temp_pos)

            total_score.append(move_score[0])
        return total_score


    def cal_move_for_one_A(self, pos):
        next_ = self.next_move_for_one_peg(pos, 0)  # turn:: 0 = my
        if next_ is None or len(next_) == 0:
            return None
        start, end = next_[1][1][0], next_[1][1][-1]
        self.swap_positions(start, end)
        game_adv_A = self.board[start][HEURISTIC][0] - self.board[end][HEURISTIC][0]
        return (next_[1][1], game_adv_A)

    def cal_move_for_other_peg(self, pos: [], turn):
        next_ = self.get_next_move(pos, turn)  # turn:: 1 = B
        if len(next_) > 0 and len(next_[1]) > 0:
            start, end = next_[1][0], next_[1][-1]
            self.swap_positions(start, end)
            game_adv = self.board[start][HEURISTIC][turn] - self.board[end][HEURISTIC][turn]
            return (next_[1], game_adv)
        return None

    def get_next_move_of_mine(self, pos_dict):

        working_positions = self.working_pegs(pos_dict)
        my_curr_pegs = working_positions["A"]

        # print(f"curr moves: {my_curr_pegs}")

        move_score = []
        for i in range(len(my_curr_pegs)):  # len(my_curr_pegs)
            self.board = BoardHelper.reset_update(self.board, pos_dict)
            peg = my_curr_pegs[i]

            three_moves = {}

            next_move_for_my_peg = self.next_move_for_one_peg(peg, 0, True)  # turn:: 0 = my

            if next_move_for_my_peg is None or len(next_move_for_my_peg) == 0:
                continue

            # print(f"next moves: {next_move_for_my_peg}")

            opt_moves = [move for move in next_move_for_my_peg if
                         self.board[move[-1]][HEURISTIC][0] <= self.board[peg][HEURISTIC][0]]

            # print(f"opt moves: {opt_moves}")

            # print(f"print all: {next_move_for_my_peg}, opt move: {opt_moves}")

            for move in opt_moves:
                start, end = move[0], move[-1]
                self.swap_positions(start, end)
                # temp_positions["A"][i] = next_move_for_my_peg[0]
                score_after_move = self.board[start][HEURISTIC][0] - self.board[end][HEURISTIC][0]
                game_adv_A = self.board[start][HEURISTIC][0] - self.board[end][HEURISTIC][0]
                three_moves['A'] = [start, end]

                game_adv_for_B = 0
                if 'B' in working_positions:
                    next_B = self.get_next_move(working_positions["B"], 1)  # turn:: 1 = B
                    if len(next_B) > 0 and len(next_B[1]) > 0:
                        start, end = next_B[1][0], next_B[1][-1]
                        self.swap_positions(start, end)
                        # peg_index = temp_positions["B"].index(next_B[0])
                        # temp_positions["B"][peg_index] = next_B[1][-1]
                        score_after_move = self.board[start][HEURISTIC][1] - self.board[end][HEURISTIC][1]
                        game_adv_for_B = self.board[start][HEURISTIC][1] - self.board[end][HEURISTIC][1]
                        three_moves['B'] = [start, end]

                # score calculate for peg :: C
                game_adv_for_C = 0
                if 'C' in working_positions:
                    next_C = self.get_next_move(working_positions["C"], 2)  # turn:: 1 = C
                    if len(next_C) > 0 and len(next_C[1]) > 0:
                        start, end = next_C[1][0], next_C[1][-1]
                        self.swap_positions(start, end)
                        # peg_index = temp_positions["C"].index(next_C[0])
                        # temp_positions["C"][peg_index] = next_C[1][-1]
                        score_after_move = self.board[start][HEURISTIC][2] - self.board[end][HEURISTIC][2]
                        game_adv_for_C = self.board[start][HEURISTIC][2] - self.board[end][HEURISTIC][2]
                        three_moves['C'] = [start, end]
                        # game_adv_for_C = score_before_move_C - score_after_move

                contribution = game_adv_A
                # print(f"move for {move}")
                # print(f"first contr: {contribution}")
                # contribution += 10 * (1 / game_adv_for_B) if game_adv_for_B else 1
                contribution -= (.5 * game_adv_for_B)
                # print(f"second contr: {contribution}")
                contribution -= (.5 * game_adv_for_C)
                # contribution += 10 * (1 / game_adv_for_C) if game_adv_for_C else 1
                # print(f"3rd contr: {contribution}")

                # now add contribution for future moves also
                temp_positions = copy.deepcopy(pos_dict)
                temp_positions = self.change_pos(three_moves, temp_positions)
                # if we not won yet
                if not self.is_win(temp_positions['A'], 0):
                    contribution_furthers = self.cal_future_move(temp_positions)
                    contribution += .5 * contribution_furthers[0][1]

                    # print(f"move: {move}, cotr: {contribution_furthers}")

                else:
                    contribution += 100

                '''Isolation check'''
                contribution -= self.isolation_check(move, temp_positions)

                contribution = float("{:.2f}".format(contribution))

                # print(f"move: {move}, contr: {contribution}, future: {contribution_furthers}")

                move_score.append((move, contribution))

                self.board = BoardHelper.reset_update(self.board, pos_dict)

            self.board = BoardHelper.reset_update(self.board, pos_dict)
        self.board = BoardHelper.reset_update(self.board, pos_dict)

        move_score.sort(key=lambda x: x[1], reverse=True)

        # print(move_score)

        return move_score[0][0]


    def isolation_check(self, move, temp):
        positions = temp['A']

        start, end = move[0], move[-1]

        isolation = 0

        coords1 = []
        coords2 = []

        for x in self.board[start][CONNECTED_COORDINATES]:
            coords1.append(x)

        for x in coords1:
            for y in self.board[x][CONNECTED_COORDINATES]:
                if y not in coords1 or y != start:
                    coords2.append(y)

        effpegs = []

        for x in coords1:
            if x in positions:
                effpegs.append(x)

        for x in coords2:
            if x in positions:
                effpegs.append(x)

        for peg in effpegs:
            pegolation = 4

            onevince = self.board[peg][CONNECTED_COORDINATES]
            twovince = []
            for x in onevince:
                for y in self.board[x][CONNECTED_COORDINATES]:
                    if y not in coords1 or y != peg:
                        twovince.append(y)

            for x in twovince:
                if self.board[x][HOLD] is 'A' or x == end:
                    pegolation = 2
            for x in onevince:
                if self.board[x][HOLD] is 'A' or x == end:
                    pegolation = 0

            if pegolation > isolation:
                isolation = pegolation

        return isolation


if __name__ == "__main__":
    import sys

    sys.setrecursionlimit(2000)

    #pos_str = "-3,5;-3,6;-2,5;-2,4;-4,2;1,-1:-2,-2;-3,-2;-3,-3;-2,-3;-1,-3;-3,-1:-6,3;0,1;5,-2;6,-3;4,-2;5,-3"
    pos_str = "2,-4;3,-5;1,-2;0,-1;2,-3;1,1:2,2;1,3;2,3;1,0;-1,1;-4,1:-4,3;-6,3;-3,1;-1,0;2,-1;3,0"

    positions = BoardHelper.extract_formatted_positions(pos_str)

    cc = ChineseChecker()
    cc.board = BoardHelper.reset_update(cc.board, positions)

    # print(f"position before: {positions}")

    '''
    rem_keys = {}
    for key, value in positions.items():
        for pos in value:
            if cc.peg_in_goal(pos, peg_turn[key]):
                if key in rem_keys:
                    rem_keys[key].append(pos)
                else:
                    rem_keys[key] = [pos]

    # remove keys
    for key, pos in rem_keys.items():
        for o in pos:
            positions[key].remove(o)
    '''

    # print(cc.board['0,2'][HOLD])
    move = cc.get_next_move_of_mine(positions)
    # move = cc.next_move_for_one_peg('1,-2', 0)
    # move = cc.get_next_move(positions['C'], 0)
    print(f"move: {move} and error: {cc.board['0,2'][HOLD]}")

    # print(f"Our move is {move}")

    '''
    flag = True
    move_counter = 0
    while flag:
        print(f"Start a new move....")
        cc = ChineseChecker()
        cc.board = BoardHelper.update_pegs_info(cc.board, positions)

        for key, value in positions.items():
            for pos in value:
                if cc.peg_in_goal(pos, peg_turn[key]):
                    print(f"removing element: {pos}")
                    positions[key].remove(pos)


        print(f"Start with positions: { positions['A'] }")

        # peg, score = cc.get_next_move_of_mine(positions)
        if cc.is_initial(positions["A"], 0):
            move = cc.static_move()
            start, goal = move[0], move[-1]
        else:
            move = cc.get_next_move_of_mine(positions)
            start, goal = move[0][1][0], move[0][1][-1]

        index = positions["A"].index(start)
        positions["A"][index] = goal
        print(f"Finish new move: {move}")
        cc.board = BoardHelper.update_pegs_info(cc.board, positions)
        move_counter += 1

        if cc.is_win(positions["A"], 0):
            flag = False

    print(f"Game win at move count : {move_counter}")

    # print(f"Select peg : {peg} for moving to : , cause score is minimum: {score}")
    '''
