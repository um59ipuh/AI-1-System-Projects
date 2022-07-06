(define (problem grid)
	(:domain World)
	(:objects
	; all grid positions are coordinates
		grid_1_1 grid_1_2 grid_1_3 grid_1_4 grid_1_5 grid_1_6 grid_1_7 grid_1_8 grid_1_9 grid_1_10 - coordinate
		grid_2_1 grid_2_2 grid_2_3 grid_2_4 grid_2_5 grid_2_6 grid_2_7 grid_2_8 grid_2_9 grid_2_10 - coordinate
		grid_3_1 grid_3_2 grid_3_3 grid_3_4 grid_3_5 grid_3_6 grid_3_7 grid_3_8 grid_3_9 grid_3_10 - coordinate
		grid_4_1 grid_4_2 grid_4_3 grid_4_4 grid_4_5 grid_4_6 grid_4_7 grid_4_8 grid_4_9 grid_4_10 - coordinate
		grid_5_1 grid_5_2 grid_5_3 grid_5_4 grid_5_5 grid_5_6 grid_5_7 grid_5_8 grid_5_9 grid_5_10 - coordinate
		grid_6_1 grid_6_2 grid_6_3 grid_6_4 grid_6_5 grid_6_6 grid_6_7 grid_6_8 grid_6_9 grid_6_10 - coordinate
		grid_7_1 grid_7_2 grid_7_3 grid_7_4 grid_7_5 grid_7_6 grid_7_7 grid_7_8 grid_7_9 grid_7_10 - coordinate
		grid_8_1 grid_8_2 grid_8_3 grid_8_4 grid_8_5 grid_8_6 grid_8_7 grid_8_8 grid_8_9 grid_8_10 - coordinate
		out - coordinate

		S - bot
)

	(:init
		; start position for player
		(at S grid_4_6)
		(m1 S)
		; init grid connections
		(conn grid_1_1 grid_1_2)
		(conn grid_1_1 grid_2_1)
		(push_conn grid_1_1 grid_1_3)
		(push_conn grid_1_1 grid_3_1)
		(conn grid_1_2 grid_1_3)
		(conn grid_1_2 grid_2_2)
		(conn grid_1_2 grid_1_1)
		(push_conn grid_1_2 grid_1_4)
		(push_conn grid_1_2 grid_3_2)
		(conn grid_1_3 grid_1_4)
		(conn grid_1_3 grid_2_3)
		(conn grid_1_3 grid_1_2)
		(push_conn grid_1_3 grid_1_5)
		(push_conn grid_1_3 grid_3_3)
		(push_conn grid_1_3 grid_1_1)
		(conn grid_1_4 grid_1_5)
		(conn grid_1_4 grid_2_4)
		(conn grid_1_4 grid_1_3)
		(push_conn grid_1_4 grid_1_6)
		(push_conn grid_1_4 grid_3_4)
		(push_conn grid_1_4 grid_1_2)
		(conn grid_1_5 grid_1_6)
		(conn grid_1_5 grid_2_5)
		(conn grid_1_5 grid_1_4)
		(push_conn grid_1_5 grid_1_7)
		(push_conn grid_1_5 grid_3_5)
		(push_conn grid_1_5 grid_1_3)
		(conn grid_1_6 grid_1_7)
		(conn grid_1_6 grid_2_6)
		(conn grid_1_6 grid_1_5)
		(push_conn grid_1_6 grid_1_8)
		(push_conn grid_1_6 grid_3_6)
		(push_conn grid_1_6 grid_1_4)
		(conn grid_1_7 grid_1_8)
		(conn grid_1_7 grid_2_7)
		(conn grid_1_7 grid_1_6)
		(push_conn grid_1_7 grid_1_9)
		(push_conn grid_1_7 grid_3_7)
		(push_conn grid_1_7 grid_1_5)
		(conn grid_1_8 grid_1_9)
		(conn grid_1_8 grid_2_8)
		(conn grid_1_8 grid_1_7)
		(push_conn grid_1_8 grid_1_10)
		(push_conn grid_1_8 grid_3_8)
		(push_conn grid_1_8 grid_1_6)
		(conn grid_1_9 grid_1_10)
		(conn grid_1_9 grid_2_9)
		(conn grid_1_9 grid_1_8)
		(push_conn grid_1_9 grid_3_9)
		(push_conn grid_1_9 grid_1_7)
		(conn grid_1_10 grid_2_10)
		(conn grid_1_10 grid_1_9)
		(push_conn grid_1_10 grid_3_10)
		(push_conn grid_1_10 grid_1_8)
		(conn grid_2_1 grid_1_1)
		(conn grid_2_1 grid_2_2)
		(conn grid_2_1 grid_3_1)
		(push_conn grid_2_1 grid_2_3)
		(push_conn grid_2_1 grid_4_1)
		(conn grid_2_2 grid_1_2)
		(conn grid_2_2 grid_2_3)
		(conn grid_2_2 grid_3_2)
		(conn grid_2_2 grid_2_1)
		(push_conn grid_2_2 grid_2_4)
		(push_conn grid_2_2 grid_4_2)
		(conn grid_2_3 grid_1_3)
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
		(push_conn grid_2_6 grid_2_8)
		(push_conn grid_2_6 grid_4_6)
		(push_conn grid_2_6 grid_2_4)
		(conn grid_2_7 grid_1_7)
		(conn grid_2_7 grid_2_8)
		(conn grid_2_7 grid_3_7)
		(conn grid_2_7 grid_2_6)
		(push_conn grid_2_7 grid_2_9)
		(push_conn grid_2_7 grid_4_7)
		(push_conn grid_2_7 grid_2_5)
		(conn grid_2_8 grid_1_8)
		(conn grid_2_8 grid_2_9)
		(conn grid_2_8 grid_3_8)
		(conn grid_2_8 grid_2_7)
		(push_conn grid_2_8 grid_2_10)
		(push_conn grid_2_8 grid_4_8)
		(push_conn grid_2_8 grid_2_6)
		(conn grid_2_9 grid_1_9)
		(conn grid_2_9 grid_2_10)
		(conn grid_2_9 grid_3_9)
		(conn grid_2_9 grid_2_8)
		(push_conn grid_2_9 grid_4_9)
		(push_conn grid_2_9 grid_2_7)
		(conn grid_2_10 grid_1_10)
		(conn grid_2_10 grid_3_10)
		(conn grid_2_10 grid_2_9)
		(push_conn grid_2_10 grid_4_10)
		(push_conn grid_2_10 grid_2_8)
		(conn grid_3_1 grid_2_1)
		(conn grid_3_1 grid_3_2)
		(conn grid_3_1 grid_4_1)
		(push_conn grid_3_1 grid_1_1)
		(push_conn grid_3_1 grid_3_3)
		(push_conn grid_3_1 grid_5_1)
		(conn grid_3_2 grid_2_2)
		(conn grid_3_2 grid_3_3)
		(conn grid_3_2 grid_4_2)
		(conn grid_3_2 grid_3_1)
		(push_conn grid_3_2 grid_1_2)
		(push_conn grid_3_2 grid_3_4)
		(push_conn grid_3_2 grid_5_2)
		(conn grid_3_3 grid_2_3)
		(conn grid_3_3 grid_3_4)
		(conn grid_3_3 grid_4_3)
		(conn grid_3_3 grid_3_2)
		(push_conn grid_3_3 grid_1_3)
		(push_conn grid_3_3 grid_3_5)
		(push_conn grid_3_3 grid_5_3)
		(push_conn grid_3_3 grid_3_1)
		(conn grid_3_4 grid_2_4)
		(conn grid_3_4 grid_3_5)
		(conn grid_3_4 grid_4_4)
		(conn grid_3_4 grid_3_3)
		(push_conn grid_3_4 grid_1_4)
		(push_conn grid_3_4 grid_3_6)
		(push_conn grid_3_4 grid_5_4)
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
		(push_conn grid_3_6 grid_3_8)
		(push_conn grid_3_6 grid_5_6)
		(push_conn grid_3_6 grid_3_4)
		(conn grid_3_7 grid_2_7)
		(conn grid_3_7 grid_3_8)
		(conn grid_3_7 grid_4_7)
		(conn grid_3_7 grid_3_6)
		(push_conn grid_3_7 grid_1_7)
		(push_conn grid_3_7 grid_3_9)
		(push_conn grid_3_7 grid_5_7)
		(push_conn grid_3_7 grid_3_5)
		(conn grid_3_8 grid_2_8)
		(conn grid_3_8 grid_3_9)
		(conn grid_3_8 grid_4_8)
		(conn grid_3_8 grid_3_7)
		(push_conn grid_3_8 grid_1_8)
		(push_conn grid_3_8 grid_3_10)
		(push_conn grid_3_8 grid_5_8)
		(push_conn grid_3_8 grid_3_6)
		(conn grid_3_9 grid_2_9)
		(conn grid_3_9 grid_3_10)
		(conn grid_3_9 grid_4_9)
		(conn grid_3_9 grid_3_8)
		(push_conn grid_3_9 grid_1_9)
		(push_conn grid_3_9 grid_5_9)
		(push_conn grid_3_9 grid_3_7)
		(conn grid_3_10 grid_2_10)
		(conn grid_3_10 grid_4_10)
		(conn grid_3_10 grid_3_9)
		(push_conn grid_3_10 grid_1_10)
		(push_conn grid_3_10 grid_5_10)
		(push_conn grid_3_10 grid_3_8)
		(conn grid_4_1 grid_3_1)
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
		(conn grid_4_3 grid_3_3)
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
		(push_conn grid_4_4 grid_6_4)
		(push_conn grid_4_4 grid_4_2)
		(conn grid_4_5 grid_3_5)
		(conn grid_4_5 grid_4_6)
		(conn grid_4_5 grid_5_5)
		(conn grid_4_5 grid_4_4)
		(push_conn grid_4_5 grid_2_5)
		(push_conn grid_4_5 grid_4_7)
		(push_conn grid_4_5 grid_6_5)
		(push_conn grid_4_5 grid_4_3)
		(conn grid_4_6 grid_3_6)
		(conn grid_4_6 grid_4_7)
		(conn grid_4_6 grid_5_6)
		(conn grid_4_6 grid_4_5)
		(push_conn grid_4_6 grid_2_6)
		(push_conn grid_4_6 grid_4_8)
		(push_conn grid_4_6 grid_6_6)
		(push_conn grid_4_6 grid_4_4)
		(conn grid_4_7 grid_3_7)
		(conn grid_4_7 grid_4_8)
		(conn grid_4_7 grid_5_7)
		(conn grid_4_7 grid_4_6)
		(push_conn grid_4_7 grid_2_7)
		(push_conn grid_4_7 grid_4_9)
		(push_conn grid_4_7 grid_6_7)
		(push_conn grid_4_7 grid_4_5)
		(conn grid_4_8 grid_3_8)
		(conn grid_4_8 grid_4_9)
		(conn grid_4_8 grid_5_8)
		(conn grid_4_8 grid_4_7)
		(push_conn grid_4_8 grid_2_8)
		(push_conn grid_4_8 grid_4_10)
		(push_conn grid_4_8 grid_6_8)
		(push_conn grid_4_8 grid_4_6)
		(conn grid_4_9 grid_3_9)
		(conn grid_4_9 grid_4_10)
		(conn grid_4_9 grid_5_9)
		(conn grid_4_9 grid_4_8)
		(push_conn grid_4_9 grid_2_9)
		(push_conn grid_4_9 grid_6_9)
		(push_conn grid_4_9 grid_4_7)
		(conn grid_4_10 grid_3_10)
		(conn grid_4_10 grid_5_10)
		(conn grid_4_10 grid_4_9)
		(push_conn grid_4_10 grid_2_10)
		(push_conn grid_4_10 grid_6_10)
		(push_conn grid_4_10 grid_4_8)
		(conn grid_5_1 grid_4_1)
		(conn grid_5_1 grid_5_2)
		(conn grid_5_1 grid_6_1)
		(push_conn grid_5_1 grid_3_1)
		(push_conn grid_5_1 grid_5_3)
		(push_conn grid_5_1 grid_7_1)
		(conn grid_5_2 grid_4_2)
		(conn grid_5_2 grid_5_3)
		(conn grid_5_2 grid_6_2)
		(conn grid_5_2 grid_5_1)
		(push_conn grid_5_2 grid_3_2)
		(push_conn grid_5_2 grid_5_4)
		(push_conn grid_5_2 grid_7_2)
		(conn grid_5_3 grid_4_3)
		(conn grid_5_3 grid_5_4)
		(conn grid_5_3 grid_6_3)
		(conn grid_5_3 grid_5_2)
		(push_conn grid_5_3 grid_3_3)
		(push_conn grid_5_3 grid_5_5)
		(push_conn grid_5_3 grid_7_3)
		(push_conn grid_5_3 grid_5_1)
		(conn grid_5_4 grid_4_4)
		(conn grid_5_4 grid_5_5)
		(conn grid_5_4 grid_6_4)
		(conn grid_5_4 grid_5_3)
		(push_conn grid_5_4 grid_3_4)
		(push_conn grid_5_4 grid_5_6)
		(push_conn grid_5_4 grid_7_4)
		(push_conn grid_5_4 grid_5_2)
		(conn grid_5_5 grid_4_5)
		(conn grid_5_5 grid_5_6)
		(conn grid_5_5 grid_6_5)
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
		(conn grid_5_7 grid_4_7)
		(conn grid_5_7 grid_5_8)
		(conn grid_5_7 grid_6_7)
		(conn grid_5_7 grid_5_6)
		(push_conn grid_5_7 grid_3_7)
		(push_conn grid_5_7 grid_5_9)
		(push_conn grid_5_7 grid_7_7)
		(push_conn grid_5_7 grid_5_5)
		(conn grid_5_8 grid_4_8)
		(conn grid_5_8 grid_5_9)
		(conn grid_5_8 grid_6_8)
		(conn grid_5_8 grid_5_7)
		(push_conn grid_5_8 grid_3_8)
		(push_conn grid_5_8 grid_5_10)
		(push_conn grid_5_8 grid_7_8)
		(push_conn grid_5_8 grid_5_6)
		(conn grid_5_9 grid_4_9)
		(conn grid_5_9 grid_5_10)
		(conn grid_5_9 grid_6_9)
		(conn grid_5_9 grid_5_8)
		(push_conn grid_5_9 grid_3_9)
		(push_conn grid_5_9 grid_7_9)
		(push_conn grid_5_9 grid_5_7)
		(conn grid_5_10 grid_4_10)
		(conn grid_5_10 grid_6_10)
		(conn grid_5_10 grid_5_9)
		(push_conn grid_5_10 grid_3_10)
		(push_conn grid_5_10 grid_7_10)
		(push_conn grid_5_10 grid_5_8)
		(conn grid_6_1 grid_5_1)
		(conn grid_6_1 grid_6_2)
		(conn grid_6_1 grid_7_1)
		(push_conn grid_6_1 grid_4_1)
		(push_conn grid_6_1 grid_6_3)
		(push_conn grid_6_1 grid_8_1)
		(conn grid_6_2 grid_5_2)
		(conn grid_6_2 grid_6_3)
		(conn grid_6_2 grid_7_2)
		(conn grid_6_2 grid_6_1)
		(push_conn grid_6_2 grid_4_2)
		(push_conn grid_6_2 grid_6_4)
		(push_conn grid_6_2 grid_8_2)
		(conn grid_6_3 grid_5_3)
		(conn grid_6_3 grid_6_4)
		(conn grid_6_3 grid_7_3)
		(conn grid_6_3 grid_6_2)
		(push_conn grid_6_3 grid_4_3)
		(push_conn grid_6_3 grid_6_5)
		(push_conn grid_6_3 grid_8_3)
		(push_conn grid_6_3 grid_6_1)
		(conn grid_6_4 grid_5_4)
		(conn grid_6_4 grid_6_5)
		(conn grid_6_4 grid_7_4)
		(conn grid_6_4 grid_6_3)
		(push_conn grid_6_4 grid_4_4)
		(push_conn grid_6_4 grid_6_6)
		(push_conn grid_6_4 grid_8_4)
		(push_conn grid_6_4 grid_6_2)
		(conn grid_6_5 grid_5_5)
		(conn grid_6_5 grid_6_6)
		(conn grid_6_5 grid_7_5)
		(conn grid_6_5 grid_6_4)
		(push_conn grid_6_5 grid_4_5)
		(push_conn grid_6_5 grid_6_7)
		(push_conn grid_6_5 grid_8_5)
		(push_conn grid_6_5 grid_6_3)
		(conn grid_6_6 grid_5_6)
		(conn grid_6_6 grid_6_7)
		(conn grid_6_6 grid_7_6)
		(conn grid_6_6 grid_6_5)
		(push_conn grid_6_6 grid_4_6)
		(push_conn grid_6_6 grid_6_8)
		(push_conn grid_6_6 grid_8_6)
		(push_conn grid_6_6 grid_6_4)
		(conn grid_6_7 grid_5_7)
		(conn grid_6_7 grid_6_8)
		(conn grid_6_7 grid_7_7)
		(conn grid_6_7 grid_6_6)
		(push_conn grid_6_7 grid_4_7)
		(push_conn grid_6_7 grid_6_9)
		(push_conn grid_6_7 grid_8_7)
		(push_conn grid_6_7 grid_6_5)
		(conn grid_6_8 grid_5_8)
		(conn grid_6_8 grid_6_9)
		(conn grid_6_8 grid_7_8)
		(conn grid_6_8 grid_6_7)
		(push_conn grid_6_8 grid_4_8)
		(push_conn grid_6_8 grid_6_10)
		(push_conn grid_6_8 grid_8_8)
		(push_conn grid_6_8 grid_6_6)
		(conn grid_6_9 grid_5_9)
		(conn grid_6_9 grid_6_10)
		(conn grid_6_9 grid_7_9)
		(conn grid_6_9 grid_6_8)
		(push_conn grid_6_9 grid_4_9)
		(push_conn grid_6_9 grid_8_9)
		(push_conn grid_6_9 grid_6_7)
		(conn grid_6_10 grid_5_10)
		(conn grid_6_10 grid_7_10)
		(conn grid_6_10 grid_6_9)
		(push_conn grid_6_10 grid_4_10)
		(push_conn grid_6_10 grid_8_10)
		(push_conn grid_6_10 grid_6_8)
		(conn grid_7_1 grid_6_1)
		(conn grid_7_1 grid_7_2)
		(conn grid_7_1 grid_8_1)
		(push_conn grid_7_1 grid_5_1)
		(push_conn grid_7_1 grid_7_3)
		(conn grid_7_2 grid_6_2)
		(conn grid_7_2 grid_7_3)
		(conn grid_7_2 grid_8_2)
		(conn grid_7_2 grid_7_1)
		(push_conn grid_7_2 grid_5_2)
		(push_conn grid_7_2 grid_7_4)
		(conn grid_7_3 grid_6_3)
		(conn grid_7_3 grid_7_4)
		(conn grid_7_3 grid_8_3)
		(conn grid_7_3 grid_7_2)
		(push_conn grid_7_3 grid_5_3)
		(push_conn grid_7_3 grid_7_5)
		(push_conn grid_7_3 grid_7_1)
		(conn grid_7_4 grid_6_4)
		(conn grid_7_4 grid_7_5)
		(conn grid_7_4 grid_8_4)
		(conn grid_7_4 grid_7_3)
		(push_conn grid_7_4 grid_5_4)
		(push_conn grid_7_4 grid_7_6)
		(push_conn grid_7_4 grid_7_2)
		(conn grid_7_5 grid_6_5)
		(conn grid_7_5 grid_7_6)
		(conn grid_7_5 grid_8_5)
		(conn grid_7_5 grid_7_4)
		(push_conn grid_7_5 grid_5_5)
		(push_conn grid_7_5 grid_7_7)
		(push_conn grid_7_5 grid_7_3)
		(conn grid_7_6 grid_6_6)
		(conn grid_7_6 grid_7_7)
		(conn grid_7_6 grid_8_6)
		(conn grid_7_6 grid_7_5)
		(push_conn grid_7_6 grid_5_6)
		(push_conn grid_7_6 grid_7_8)
		(push_conn grid_7_6 grid_7_4)
		(conn grid_7_7 grid_6_7)
		(conn grid_7_7 grid_7_8)
		(conn grid_7_7 grid_8_7)
		(conn grid_7_7 grid_7_6)
		(push_conn grid_7_7 grid_5_7)
		(push_conn grid_7_7 grid_7_9)
		(push_conn grid_7_7 grid_7_5)
		(conn grid_7_8 grid_6_8)
		(conn grid_7_8 grid_7_9)
		(conn grid_7_8 grid_8_8)
		(conn grid_7_8 grid_7_7)
		(push_conn grid_7_8 grid_5_8)
		(push_conn grid_7_8 grid_7_10)
		(push_conn grid_7_8 grid_7_6)
		(conn grid_7_9 grid_6_9)
		(conn grid_7_9 grid_7_10)
		(conn grid_7_9 grid_8_9)
		(conn grid_7_9 grid_7_8)
		(push_conn grid_7_9 grid_5_9)
		(push_conn grid_7_9 grid_7_7)
		(conn grid_7_10 grid_6_10)
		(conn grid_7_10 grid_8_10)
		(conn grid_7_10 grid_7_9)
		(push_conn grid_7_10 grid_5_10)
		(push_conn grid_7_10 grid_7_8)
		(conn grid_8_1 grid_7_1)
		(conn grid_8_1 grid_8_2)
		(push_conn grid_8_1 grid_6_1)
		(push_conn grid_8_1 grid_8_3)
		(conn grid_8_2 grid_7_2)
		(conn grid_8_2 grid_8_3)
		(conn grid_8_2 grid_8_1)
		(push_conn grid_8_2 grid_6_2)
		(push_conn grid_8_2 grid_8_4)
		(conn grid_8_3 grid_7_3)
		(conn grid_8_3 grid_8_4)
		(conn grid_8_3 grid_8_2)
		(push_conn grid_8_3 grid_6_3)
		(push_conn grid_8_3 grid_8_5)
		(push_conn grid_8_3 grid_8_1)
		(conn grid_8_4 grid_7_4)
		(conn grid_8_4 grid_8_5)
		(conn grid_8_4 grid_8_3)
		(push_conn grid_8_4 grid_6_4)
		(push_conn grid_8_4 grid_8_6)
		(push_conn grid_8_4 grid_8_2)
		(conn grid_8_5 grid_7_5)
		(conn grid_8_5 grid_8_6)
		(conn grid_8_5 grid_8_4)
		(push_conn grid_8_5 grid_6_5)
		(push_conn grid_8_5 grid_8_7)
		(push_conn grid_8_5 grid_8_3)
		(conn grid_8_6 grid_7_6)
		(conn grid_8_6 grid_8_7)
		(conn grid_8_6 grid_8_5)
		(push_conn grid_8_6 grid_6_6)
		(push_conn grid_8_6 grid_8_8)
		(push_conn grid_8_6 grid_8_4)
		(conn grid_8_7 grid_7_7)
		(conn grid_8_7 grid_8_8)
		(conn grid_8_7 grid_8_6)
		(push_conn grid_8_7 grid_6_7)
		(push_conn grid_8_7 grid_8_9)
		(push_conn grid_8_7 grid_8_5)
		(conn grid_8_8 grid_7_8)
		(conn grid_8_8 grid_8_9)
		(conn grid_8_8 grid_8_7)
		(push_conn grid_8_8 grid_6_8)
		(push_conn grid_8_8 grid_8_10)
		(push_conn grid_8_8 grid_8_6)
		(conn grid_8_9 grid_7_9)
		(conn grid_8_9 grid_8_10)
		(conn grid_8_9 grid_8_8)
		(push_conn grid_8_9 grid_6_9)
		(push_conn grid_8_9 grid_8_7)
		(conn grid_8_10 grid_7_10)
		(conn grid_8_10 grid_8_9)
		(push_conn grid_8_10 grid_6_10)
		(push_conn grid_8_10 grid_8_8)
		; add wumpus onto map
		; add walls onto map
		; add pits onto map
		; add crates onto map
		(crate grid_1_1)
		(crate grid_1_2)
		(crate grid_1_3)
		(crate grid_1_4)
		(crate grid_1_5)
		(crate grid_1_7)
		(crate grid_1_9)
		(crate grid_1_10)
		(crate grid_2_3)
		(crate grid_2_5)
		(crate grid_2_6)
		(crate grid_2_7)
		(crate grid_2_8)
		(crate grid_2_9)
		(crate grid_3_1)
		(crate grid_3_3)
		(crate grid_3_5)
		(crate grid_3_7)
		(crate grid_3_10)
		(crate grid_4_1)
		(crate grid_4_3)
		(crate grid_4_4)
		(crate grid_4_7)
		(crate grid_4_9)
		(crate grid_5_1)
		(crate grid_5_2)
		(crate grid_5_3)
		(crate grid_5_7)
		(crate grid_5_10)
		(crate grid_6_1)
		(crate grid_6_2)
		(crate grid_6_4)
		(crate grid_6_6)
		(crate grid_6_7)
		(crate grid_6_9)
		(crate grid_7_2)
		(crate grid_7_3)
		(crate grid_7_4)
		(crate grid_7_5)
		(crate grid_7_6)
		(crate grid_7_8)
		(crate grid_7_9)
		(crate grid_7_10)
		(crate grid_8_4)
		(crate grid_8_5)
		(crate grid_8_6)
		(crate grid_8_7)
		(crate grid_8_8)
		(crate grid_8_9)
		(crate grid_8_10)
		; add unblocked spaces onto map
		(nblocked grid_1_6)
		(nblocked grid_1_8)
		(nblocked grid_2_1)
		(nblocked grid_2_2)
		(nblocked grid_2_4)
		(nblocked grid_2_10)
		(nblocked grid_3_2)
		(nblocked grid_3_4)
		(nblocked grid_3_6)
		(nblocked grid_3_8)
		(nblocked grid_3_9)
		(nblocked grid_4_2)
		(nblocked grid_4_5)
		(nblocked grid_4_6)
		(nblocked grid_4_8)
		(nblocked grid_4_10)
		(nblocked grid_5_4)
		(nblocked grid_5_5)
		(nblocked grid_5_6)
		(nblocked grid_5_8)
		(nblocked grid_5_9)
		(nblocked grid_6_3)
		(nblocked grid_6_5)
		(nblocked grid_6_8)
		(nblocked grid_6_10)
		(nblocked grid_7_1)
		(nblocked grid_7_7)
		(nblocked grid_8_1)
		(nblocked grid_8_2)
		(nblocked grid_8_3)
		(nblocked out)
		; add doors
		; add connections to goal state
		(conn grid_1_1 out)
		(conn out grid_1_1)
		(conn grid_1_2 out)
		(conn out grid_1_2)
		(conn grid_1_3 out)
		(conn out grid_1_3)
		(conn grid_1_4 out)
		(conn out grid_1_4)
		(conn grid_1_5 out)
		(conn out grid_1_5)
		(conn grid_1_6 out)
		(conn out grid_1_6)
		(conn grid_1_7 out)
		(conn out grid_1_7)
		(conn grid_1_8 out)
		(conn out grid_1_8)
		(conn grid_1_9 out)
		(conn out grid_1_9)
		(conn grid_1_10 out)
		(conn out grid_1_10)
		(conn grid_2_1 out)
		(conn out grid_2_1)
		(conn grid_2_10 out)
		(conn out grid_2_10)
		(conn grid_3_1 out)
		(conn out grid_3_1)
		(conn grid_3_10 out)
		(conn out grid_3_10)
		(conn grid_4_1 out)
		(conn out grid_4_1)
		(conn grid_4_10 out)
		(conn out grid_4_10)
		(conn grid_5_1 out)
		(conn out grid_5_1)
		(conn grid_5_10 out)
		(conn out grid_5_10)
		(conn grid_6_1 out)
		(conn out grid_6_1)
		(conn grid_6_10 out)
		(conn out grid_6_10)
		(conn grid_7_1 out)
		(conn out grid_7_1)
		(conn grid_7_10 out)
		(conn out grid_7_10)
		(conn grid_8_1 out)
		(conn out grid_8_1)
		(conn grid_8_2 out)
		(conn out grid_8_2)
		(conn grid_8_3 out)
		(conn out grid_8_3)
		(conn grid_8_4 out)
		(conn out grid_8_4)
		(conn grid_8_5 out)
		(conn out grid_8_5)
		(conn grid_8_6 out)
		(conn out grid_8_6)
		(conn grid_8_7 out)
		(conn out grid_8_7)
		(conn grid_8_8 out)
		(conn out grid_8_8)
		(conn grid_8_9 out)
		(conn out grid_8_9)
		(conn grid_8_10 out)
		(conn out grid_8_10)
	)
	(:goal
	(at S out)
	))