(define (problem grid)
	(:domain World)
	(:objects
	; all grid positions are coordinates
		grid_1_1 grid_1_2 grid_1_3 grid_1_4 grid_1_5 grid_1_6 grid_1_7 grid_1_8 - coordinate
		grid_2_1 grid_2_2 grid_2_3 grid_2_4 grid_2_5 grid_2_6 grid_2_7 grid_2_8 - coordinate
		grid_3_1 grid_3_2 grid_3_3 grid_3_4 grid_3_5 grid_3_6 grid_3_7 grid_3_8 - coordinate
		grid_4_1 grid_4_2 grid_4_3 grid_4_4 grid_4_5 grid_4_6 grid_4_7 grid_4_8 - coordinate
		grid_5_1 grid_5_2 grid_5_3 grid_5_4 grid_5_5 grid_5_6 grid_5_7 grid_5_8 - coordinate
		grid_6_1 grid_6_2 grid_6_3 grid_6_4 grid_6_5 grid_6_6 grid_6_7 grid_6_8 - coordinate
		grid_7_1 grid_7_2 grid_7_3 grid_7_4 grid_7_5 grid_7_6 grid_7_7 grid_7_8 - coordinate
		grid_8_1 grid_8_2 grid_8_3 grid_8_4 grid_8_5 grid_8_6 grid_8_7 grid_8_8 - coordinate
		out - coordinate

		S - bot
		A0 - arrow
		A1 - arrow
		A2 - arrow
		A3 - arrow
		A4 - arrow
		A5 - arrow
)

	(:init
		; start position for player
		(at S grid_6_7)
		(m1 S)
		(at A0 grid_3_4)
		(at A1 grid_4_3)
		(at A2 grid_4_5)
		(at A3 grid_6_2)
		(at A4 grid_8_1)
		(at A5 grid_8_6)
		; init grid connections
		(conn grid_1_1 grid_2_1)
		(push_conn grid_1_1 grid_1_3)
		(conn grid_1_3 grid_1_4)
		(conn grid_1_3 grid_2_3)
		(push_conn grid_1_3 grid_1_5)
		(push_conn grid_1_3 grid_1_1)
		(conn grid_1_4 grid_1_5)
		(conn grid_1_4 grid_2_4)
		(conn grid_1_4 grid_1_3)
		(push_conn grid_1_4 grid_1_6)
		(push_conn grid_1_4 grid_3_4)
		(conn grid_1_5 grid_1_6)
		(conn grid_1_5 grid_1_4)
		(push_conn grid_1_5 grid_3_5)
		(push_conn grid_1_5 grid_1_3)
		(conn grid_1_6 grid_2_6)
		(conn grid_1_6 grid_1_5)
		(push_conn grid_1_6 grid_3_6)
		(push_conn grid_1_6 grid_1_4)
		(conn grid_2_1 grid_1_1)
		(conn grid_2_1 grid_2_2)
		(push_conn grid_2_1 grid_2_3)
		(push_conn grid_2_1 grid_4_1)
		(conn grid_2_2 grid_2_3)
		(conn grid_2_2 grid_3_2)
		(conn grid_2_2 grid_2_1)
		(push_conn grid_2_2 grid_2_4)
		(push_conn grid_2_2 grid_4_2)
		(conn grid_2_3 grid_1_3)
		(conn grid_2_3 grid_2_4)
		(conn grid_2_3 grid_2_2)
		(push_conn grid_2_3 grid_4_3)
		(push_conn grid_2_3 grid_2_1)
		(conn grid_2_4 grid_1_4)
		(conn grid_2_4 grid_3_4)
		(conn grid_2_4 grid_2_3)
		(push_conn grid_2_4 grid_2_6)
		(push_conn grid_2_4 grid_4_4)
		(push_conn grid_2_4 grid_2_2)
		(conn grid_2_6 grid_1_6)
		(conn grid_2_6 grid_2_7)
		(conn grid_2_6 grid_3_6)
		(push_conn grid_2_6 grid_2_8)
		(push_conn grid_2_6 grid_4_6)
		(push_conn grid_2_6 grid_2_4)
		(conn grid_2_7 grid_2_8)
		(conn grid_2_7 grid_3_7)
		(conn grid_2_7 grid_2_6)
		(conn grid_2_8 grid_2_7)
		(push_conn grid_2_8 grid_2_6)
		(conn grid_3_2 grid_2_2)
		(conn grid_3_2 grid_4_2)
		(push_conn grid_3_2 grid_3_4)
		(push_conn grid_3_2 grid_5_2)
		(conn grid_3_4 grid_2_4)
		(conn grid_3_4 grid_3_5)
		(conn grid_3_4 grid_4_4)
		(push_conn grid_3_4 grid_1_4)
		(push_conn grid_3_4 grid_3_6)
		(push_conn grid_3_4 grid_5_4)
		(push_conn grid_3_4 grid_3_2)
		(conn grid_3_5 grid_3_6)
		(conn grid_3_5 grid_4_5)
		(conn grid_3_5 grid_3_4)
		(push_conn grid_3_5 grid_1_5)
		(push_conn grid_3_5 grid_3_7)
		(push_conn grid_3_5 grid_5_5)
		(conn grid_3_6 grid_2_6)
		(conn grid_3_6 grid_3_7)
		(conn grid_3_6 grid_4_6)
		(conn grid_3_6 grid_3_5)
		(push_conn grid_3_6 grid_1_6)
		(push_conn grid_3_6 grid_5_6)
		(push_conn grid_3_6 grid_3_4)
		(conn grid_3_7 grid_2_7)
		(conn grid_3_7 grid_3_6)
		(push_conn grid_3_7 grid_5_7)
		(push_conn grid_3_7 grid_3_5)
		(conn grid_4_1 grid_4_2)
		(conn grid_4_1 grid_5_1)
		(push_conn grid_4_1 grid_2_1)
		(push_conn grid_4_1 grid_4_3)
		(push_conn grid_4_1 grid_6_1)
		(conn grid_4_2 grid_3_2)
		(conn grid_4_2 grid_4_3)
		(conn grid_4_2 grid_5_2)
		(conn grid_4_2 grid_4_1)
		(push_conn grid_4_2 grid_2_2)
		(push_conn grid_4_2 grid_4_4)
		(push_conn grid_4_2 grid_6_2)
		(conn grid_4_3 grid_4_4)
		(conn grid_4_3 grid_5_3)
		(conn grid_4_3 grid_4_2)
		(push_conn grid_4_3 grid_2_3)
		(push_conn grid_4_3 grid_4_5)
		(push_conn grid_4_3 grid_6_3)
		(push_conn grid_4_3 grid_4_1)
		(conn grid_4_4 grid_3_4)
		(conn grid_4_4 grid_4_5)
		(conn grid_4_4 grid_5_4)
		(conn grid_4_4 grid_4_3)
		(push_conn grid_4_4 grid_2_4)
		(push_conn grid_4_4 grid_4_6)
		(push_conn grid_4_4 grid_4_2)
		(conn grid_4_5 grid_3_5)
		(conn grid_4_5 grid_4_6)
		(conn grid_4_5 grid_5_5)
		(conn grid_4_5 grid_4_4)
		(push_conn grid_4_5 grid_4_3)
		(conn grid_4_6 grid_3_6)
		(conn grid_4_6 grid_5_6)
		(conn grid_4_6 grid_4_5)
		(push_conn grid_4_6 grid_2_6)
		(push_conn grid_4_6 grid_6_6)
		(push_conn grid_4_6 grid_4_4)
		(conn grid_5_1 grid_4_1)
		(conn grid_5_1 grid_5_2)
		(conn grid_5_1 grid_6_1)
		(push_conn grid_5_1 grid_5_3)
		(push_conn grid_5_1 grid_7_1)
		(conn grid_5_2 grid_4_2)
		(conn grid_5_2 grid_5_3)
		(conn grid_5_2 grid_6_2)
		(conn grid_5_2 grid_5_1)
		(push_conn grid_5_2 grid_3_2)
		(push_conn grid_5_2 grid_5_4)
		(conn grid_5_3 grid_4_3)
		(conn grid_5_3 grid_5_4)
		(conn grid_5_3 grid_6_3)
		(conn grid_5_3 grid_5_2)
		(push_conn grid_5_3 grid_5_5)
		(push_conn grid_5_3 grid_5_1)
		(conn grid_5_4 grid_4_4)
		(conn grid_5_4 grid_5_5)
		(conn grid_5_4 grid_5_3)
		(push_conn grid_5_4 grid_3_4)
		(push_conn grid_5_4 grid_5_6)
		(push_conn grid_5_4 grid_5_2)
		(conn grid_5_5 grid_4_5)
		(conn grid_5_5 grid_5_6)
		(conn grid_5_5 grid_5_4)
		(push_conn grid_5_5 grid_3_5)
		(push_conn grid_5_5 grid_5_7)
		(push_conn grid_5_5 grid_7_5)
		(push_conn grid_5_5 grid_5_3)
		(conn grid_5_6 grid_4_6)
		(conn grid_5_6 grid_5_7)
		(conn grid_5_6 grid_6_6)
		(conn grid_5_6 grid_5_5)
		(push_conn grid_5_6 grid_3_6)
		(push_conn grid_5_6 grid_5_8)
		(push_conn grid_5_6 grid_7_6)
		(push_conn grid_5_6 grid_5_4)
		(conn grid_5_7 grid_5_8)
		(conn grid_5_7 grid_6_7)
		(conn grid_5_7 grid_5_6)
		(push_conn grid_5_7 grid_3_7)
		(push_conn grid_5_7 grid_7_7)
		(push_conn grid_5_7 grid_5_5)
		(conn grid_5_8 grid_5_7)
		(push_conn grid_5_8 grid_7_8)
		(push_conn grid_5_8 grid_5_6)
		(conn grid_6_1 grid_5_1)
		(conn grid_6_1 grid_6_2)
		(conn grid_6_1 grid_7_1)
		(push_conn grid_6_1 grid_4_1)
		(push_conn grid_6_1 grid_6_3)
		(push_conn grid_6_1 grid_8_1)
		(conn grid_6_2 grid_5_2)
		(conn grid_6_2 grid_6_3)
		(conn grid_6_2 grid_6_1)
		(push_conn grid_6_2 grid_4_2)
		(push_conn grid_6_2 grid_8_2)
		(conn grid_6_3 grid_5_3)
		(conn grid_6_3 grid_6_2)
		(push_conn grid_6_3 grid_4_3)
		(push_conn grid_6_3 grid_6_1)
		(conn grid_6_6 grid_5_6)
		(conn grid_6_6 grid_6_7)
		(conn grid_6_6 grid_7_6)
		(push_conn grid_6_6 grid_4_6)
		(push_conn grid_6_6 grid_8_6)
		(conn grid_6_7 grid_5_7)
		(conn grid_6_7 grid_7_7)
		(conn grid_6_7 grid_6_6)
		(conn grid_7_1 grid_6_1)
		(conn grid_7_1 grid_8_1)
		(push_conn grid_7_1 grid_5_1)
		(conn grid_7_5 grid_7_6)
		(push_conn grid_7_5 grid_5_5)
		(push_conn grid_7_5 grid_7_7)
		(conn grid_7_6 grid_6_6)
		(conn grid_7_6 grid_7_7)
		(conn grid_7_6 grid_8_6)
		(conn grid_7_6 grid_7_5)
		(push_conn grid_7_6 grid_5_6)
		(push_conn grid_7_6 grid_7_8)
		(conn grid_7_7 grid_6_7)
		(conn grid_7_7 grid_7_8)
		(conn grid_7_7 grid_7_6)
		(push_conn grid_7_7 grid_5_7)
		(push_conn grid_7_7 grid_7_5)
		(conn grid_7_8 grid_8_8)
		(conn grid_7_8 grid_7_7)
		(push_conn grid_7_8 grid_5_8)
		(push_conn grid_7_8 grid_7_6)
		(conn grid_8_1 grid_7_1)
		(conn grid_8_1 grid_8_2)
		(push_conn grid_8_1 grid_6_1)
		(conn grid_8_2 grid_8_1)
		(push_conn grid_8_2 grid_6_2)
		(push_conn grid_8_2 grid_8_4)
		(push_conn grid_8_4 grid_8_6)
		(push_conn grid_8_4 grid_8_2)
		(conn grid_8_6 grid_7_6)
		(push_conn grid_8_6 grid_6_6)
		(push_conn grid_8_6 grid_8_8)
		(push_conn grid_8_6 grid_8_4)
		(conn grid_8_8 grid_7_8)
		(push_conn grid_8_8 grid_8_6)
		; add wumpus onto map
		(wumpus grid_1_3)
		(wumpus grid_1_4)
		(wumpus grid_2_3)
		(wumpus grid_2_6)
		(wumpus grid_5_3)
		(wumpus grid_7_1)
		(wumpus grid_7_5)
		; add walls onto map
		; add pits onto map
		; add crates onto map
		(crate grid_2_4)
		(crate grid_4_1)
		(crate grid_6_6)
		; add unblocked spaces onto map
		(nblocked grid_2_2)
		(nblocked grid_2_7)
		(nblocked grid_2_8)
		(nblocked grid_3_5)
		(nblocked grid_4_6)
		(nblocked grid_5_1)
		(nblocked grid_5_2)
		(nblocked grid_5_5)
		(nblocked grid_5_6)
		(nblocked grid_6_1)
		(nblocked grid_6_3)
		(nblocked grid_6_7)
		(nblocked grid_7_6)
		(nblocked grid_8_2)
		(nblocked grid_8_4)
		(nblocked grid_8_8)
		(nblocked grid_3_4)
		(nblocked grid_4_3)
		(nblocked grid_4_5)
		(nblocked grid_6_2)
		(nblocked grid_8_1)
		(nblocked grid_8_6)
		(nblocked out)
		; add doors
		(d1 grid_1_5)
		(d1 grid_2_1)
		(d1 grid_3_2)
		(d1 grid_3_6)
		(d1 grid_5_4)
		(d1 grid_5_7)
		(d1 grid_7_8)
		(d2 grid_1_1)
		(d2 grid_1_6)
		(d2 grid_3_7)
		(d2 grid_4_2)
		(d2 grid_4_4)
		(d2 grid_5_8)
		(d2 grid_7_7)
		; add connections to goal state
		(conn grid_1_1 out)
		(conn out grid_1_1)
		(conn grid_1_3 out)
		(conn out grid_1_3)
		(conn grid_1_4 out)
		(conn out grid_1_4)
		(conn grid_1_5 out)
		(conn out grid_1_5)
		(conn grid_1_6 out)
		(conn out grid_1_6)
		(conn grid_2_1 out)
		(conn out grid_2_1)
		(conn grid_2_8 out)
		(conn out grid_2_8)
		(conn grid_4_1 out)
		(conn out grid_4_1)
		(conn grid_5_1 out)
		(conn out grid_5_1)
		(conn grid_5_8 out)
		(conn out grid_5_8)
		(conn grid_6_1 out)
		(conn out grid_6_1)
		(conn grid_7_1 out)
		(conn out grid_7_1)
		(conn grid_7_8 out)
		(conn out grid_7_8)
		(conn grid_8_1 out)
		(conn out grid_8_1)
		(conn grid_8_2 out)
		(conn out grid_8_2)
		(conn grid_8_4 out)
		(conn out grid_8_4)
		(conn grid_8_6 out)
		(conn out grid_8_6)
		(conn grid_8_8 out)
		(conn out grid_8_8)
	)
	(:goal
	(at S out)
	))