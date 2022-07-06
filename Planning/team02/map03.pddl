(define (problem grid)
	(:domain World)
	(:objects
	; all grid positions are coordinates
		grid_1_1 grid_1_2 grid_1_3 grid_1_4 grid_1_5 grid_1_6 grid_1_7 - coordinate
		grid_2_1 grid_2_2 grid_2_3 grid_2_4 grid_2_5 grid_2_6 grid_2_7 - coordinate
		grid_3_1 grid_3_2 grid_3_3 grid_3_4 grid_3_5 grid_3_6 grid_3_7 - coordinate
		grid_4_1 grid_4_2 grid_4_3 grid_4_4 grid_4_5 grid_4_6 grid_4_7 - coordinate
		grid_5_1 grid_5_2 grid_5_3 grid_5_4 grid_5_5 grid_5_6 grid_5_7 - coordinate
		out - coordinate

		S - bot
		A0 - arrow
		A1 - arrow
		A2 - arrow
)

	(:init
		; start position for player
		(at S grid_3_5)
		(m1 S)
		(at A0 grid_2_2)
		(at A1 grid_2_6)
		(at A2 grid_3_4)
		; init grid connections
		(conn grid_1_1 grid_1_2)
		(conn grid_1_1 grid_2_1)
		(conn grid_1_2 grid_2_2)
		(conn grid_1_2 grid_1_1)
		(push_conn grid_1_2 grid_1_4)
		(push_conn grid_1_2 grid_3_2)
		(conn grid_1_4 grid_1_5)
		(conn grid_1_4 grid_2_4)
		(push_conn grid_1_4 grid_1_6)
		(push_conn grid_1_4 grid_3_4)
		(push_conn grid_1_4 grid_1_2)
		(conn grid_1_5 grid_1_6)
		(conn grid_1_5 grid_2_5)
		(conn grid_1_5 grid_1_4)
		(push_conn grid_1_5 grid_1_7)
		(push_conn grid_1_5 grid_3_5)
		(conn grid_1_6 grid_1_7)
		(conn grid_1_6 grid_2_6)
		(conn grid_1_6 grid_1_5)
		(push_conn grid_1_6 grid_3_6)
		(push_conn grid_1_6 grid_1_4)
		(conn grid_1_7 grid_2_7)
		(conn grid_1_7 grid_1_6)
		(push_conn grid_1_7 grid_3_7)
		(push_conn grid_1_7 grid_1_5)
		(conn grid_2_1 grid_1_1)
		(conn grid_2_1 grid_2_2)
		(push_conn grid_2_1 grid_2_3)
		(push_conn grid_2_1 grid_4_1)
		(conn grid_2_2 grid_1_2)
		(conn grid_2_2 grid_2_3)
		(conn grid_2_2 grid_3_2)
		(conn grid_2_2 grid_2_1)
		(push_conn grid_2_2 grid_2_4)
		(push_conn grid_2_2 grid_4_2)
		(conn grid_2_3 grid_2_4)
		(conn grid_2_3 grid_3_3)
		(conn grid_2_3 grid_2_2)
		(push_conn grid_2_3 grid_2_5)
		(push_conn grid_2_3 grid_4_3)
		(push_conn grid_2_3 grid_2_1)
		(conn grid_2_4 grid_1_4)
		(conn grid_2_4 grid_2_5)
		(conn grid_2_4 grid_3_4)
		(conn grid_2_4 grid_2_3)
		(push_conn grid_2_4 grid_2_6)
		(push_conn grid_2_4 grid_4_4)
		(push_conn grid_2_4 grid_2_2)
		(conn grid_2_5 grid_1_5)
		(conn grid_2_5 grid_2_6)
		(conn grid_2_5 grid_3_5)
		(conn grid_2_5 grid_2_4)
		(push_conn grid_2_5 grid_2_7)
		(push_conn grid_2_5 grid_4_5)
		(push_conn grid_2_5 grid_2_3)
		(conn grid_2_6 grid_1_6)
		(conn grid_2_6 grid_2_7)
		(conn grid_2_6 grid_3_6)
		(conn grid_2_6 grid_2_5)
		(push_conn grid_2_6 grid_4_6)
		(push_conn grid_2_6 grid_2_4)
		(conn grid_2_7 grid_1_7)
		(conn grid_2_7 grid_3_7)
		(conn grid_2_7 grid_2_6)
		(push_conn grid_2_7 grid_4_7)
		(push_conn grid_2_7 grid_2_5)
		(conn grid_3_2 grid_2_2)
		(conn grid_3_2 grid_3_3)
		(conn grid_3_2 grid_4_2)
		(push_conn grid_3_2 grid_1_2)
		(push_conn grid_3_2 grid_3_4)
		(conn grid_3_3 grid_2_3)
		(conn grid_3_3 grid_3_4)
		(conn grid_3_3 grid_4_3)
		(conn grid_3_3 grid_3_2)
		(push_conn grid_3_3 grid_3_5)
		(conn grid_3_4 grid_2_4)
		(conn grid_3_4 grid_3_5)
		(conn grid_3_4 grid_4_4)
		(conn grid_3_4 grid_3_3)
		(push_conn grid_3_4 grid_1_4)
		(push_conn grid_3_4 grid_3_6)
		(push_conn grid_3_4 grid_3_2)
		(conn grid_3_5 grid_2_5)
		(conn grid_3_5 grid_3_6)
		(conn grid_3_5 grid_4_5)
		(conn grid_3_5 grid_3_4)
		(push_conn grid_3_5 grid_1_5)
		(push_conn grid_3_5 grid_3_7)
		(push_conn grid_3_5 grid_5_5)
		(push_conn grid_3_5 grid_3_3)
		(conn grid_3_6 grid_2_6)
		(conn grid_3_6 grid_3_7)
		(conn grid_3_6 grid_4_6)
		(conn grid_3_6 grid_3_5)
		(push_conn grid_3_6 grid_1_6)
		(push_conn grid_3_6 grid_5_6)
		(push_conn grid_3_6 grid_3_4)
		(conn grid_3_7 grid_2_7)
		(conn grid_3_7 grid_4_7)
		(conn grid_3_7 grid_3_6)
		(push_conn grid_3_7 grid_1_7)
		(push_conn grid_3_7 grid_5_7)
		(push_conn grid_3_7 grid_3_5)
		(conn grid_4_1 grid_4_2)
		(conn grid_4_1 grid_5_1)
		(push_conn grid_4_1 grid_2_1)
		(push_conn grid_4_1 grid_4_3)
		(conn grid_4_2 grid_3_2)
		(conn grid_4_2 grid_4_3)
		(conn grid_4_2 grid_4_1)
		(push_conn grid_4_2 grid_2_2)
		(push_conn grid_4_2 grid_4_4)
		(conn grid_4_3 grid_3_3)
		(conn grid_4_3 grid_4_4)
		(conn grid_4_3 grid_4_2)
		(push_conn grid_4_3 grid_2_3)
		(push_conn grid_4_3 grid_4_5)
		(push_conn grid_4_3 grid_4_1)
		(conn grid_4_4 grid_3_4)
		(conn grid_4_4 grid_4_5)
		(conn grid_4_4 grid_4_3)
		(push_conn grid_4_4 grid_2_4)
		(push_conn grid_4_4 grid_4_6)
		(push_conn grid_4_4 grid_4_2)
		(conn grid_4_5 grid_3_5)
		(conn grid_4_5 grid_4_6)
		(conn grid_4_5 grid_5_5)
		(conn grid_4_5 grid_4_4)
		(push_conn grid_4_5 grid_2_5)
		(push_conn grid_4_5 grid_4_7)
		(push_conn grid_4_5 grid_4_3)
		(conn grid_4_6 grid_3_6)
		(conn grid_4_6 grid_4_7)
		(conn grid_4_6 grid_5_6)
		(conn grid_4_6 grid_4_5)
		(push_conn grid_4_6 grid_2_6)
		(push_conn grid_4_6 grid_4_4)
		(conn grid_4_7 grid_3_7)
		(conn grid_4_7 grid_5_7)
		(conn grid_4_7 grid_4_6)
		(push_conn grid_4_7 grid_2_7)
		(push_conn grid_4_7 grid_4_5)
		(conn grid_5_1 grid_4_1)
		(conn grid_5_5 grid_4_5)
		(conn grid_5_5 grid_5_6)
		(push_conn grid_5_5 grid_3_5)
		(push_conn grid_5_5 grid_5_7)
		(conn grid_5_6 grid_4_6)
		(conn grid_5_6 grid_5_7)
		(conn grid_5_6 grid_5_5)
		(push_conn grid_5_6 grid_3_6)
		(conn grid_5_7 grid_4_7)
		(conn grid_5_7 grid_5_6)
		(push_conn grid_5_7 grid_3_7)
		(push_conn grid_5_7 grid_5_5)
		; add wumpus onto map
		(wumpus grid_1_7)
		(wumpus grid_4_3)
		(wumpus grid_4_4)
		(wumpus grid_4_6)
		(wumpus grid_5_1)
		; add walls onto map
		; add pits onto map
		(pit grid_1_6)
		(pit grid_3_6)
		; add crates onto map
		(crate grid_1_1)
		(crate grid_1_4)
		(crate grid_2_1)
		(crate grid_2_4)
		(crate grid_2_5)
		(crate grid_2_7)
		(crate grid_3_2)
		(crate grid_3_3)
		(crate grid_3_7)
		(crate grid_4_1)
		(crate grid_4_5)
		(crate grid_4_7)
		(crate grid_5_5)
		(crate grid_5_6)
		(crate grid_5_7)
		; add unblocked spaces onto map
		(nblocked grid_1_2)
		(nblocked grid_1_5)
		(nblocked grid_2_3)
		(nblocked grid_3_5)
		(nblocked grid_4_2)
		(nblocked grid_2_2)
		(nblocked grid_2_6)
		(nblocked grid_3_4)
		(nblocked out)
		; add doors
		; add connections to goal state
		(conn grid_1_1 out)
		(conn out grid_1_1)
		(conn grid_1_2 out)
		(conn out grid_1_2)
		(conn grid_1_4 out)
		(conn out grid_1_4)
		(conn grid_1_5 out)
		(conn out grid_1_5)
		(conn grid_1_6 out)
		(conn out grid_1_6)
		(conn grid_1_7 out)
		(conn out grid_1_7)
		(conn grid_2_1 out)
		(conn out grid_2_1)
		(conn grid_2_7 out)
		(conn out grid_2_7)
		(conn grid_3_7 out)
		(conn out grid_3_7)
		(conn grid_4_1 out)
		(conn out grid_4_1)
		(conn grid_4_7 out)
		(conn out grid_4_7)
		(conn grid_5_1 out)
		(conn out grid_5_1)
		(conn grid_5_5 out)
		(conn out grid_5_5)
		(conn grid_5_6 out)
		(conn out grid_5_6)
		(conn grid_5_7 out)
		(conn out grid_5_7)
	)
	(:goal
	(at S out)
	))