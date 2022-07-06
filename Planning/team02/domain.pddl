;; Domain for the Wumpus Problem
;;

(define (domain World)
  (:requirements :strips :typing :disjunctive-preconditions)
  (:types
    player - bot
    bot - object
    arrow - object
    place - object
    coordinate - place
  )

  (:predicates
    (at ?player - bot ?coord - coordinate)
    (is-collected ?arr - arrow)
    (pit ?coord - coordinate)
    (wumpus ?coord - coordinate)
    (crate ?coord - coordinate)
    (nblocked ?coord - coordinate)
    (conn ?coord1 - coordinate ?coord2 - coordinate)
    (push_conn ?coord1 - coordinate ?coord2 - coordinate)
    (m1 ?player - bot)
    (m2 ?player - bot)
    (d1 ?coord - coordinate)
    (d2 ?coord - coordinate)
  )

  (:action move_1
    :parameters (?player - bot ?cold - coordinate ?cnew - coordinate)
    :precondition (and (at ?player ?cold) (conn ?cold ?cnew) (nblocked ?cnew) (m1 ?player))
    :effect (and (at ?player ?cnew) (not (at ?player ?cold)) (not (m1 ?player)) (m2 ?player))
  )

  (:action move_2
    :parameters (?player - bot ?cold - coordinate ?cnew - coordinate)
    :precondition (and (at ?player ?cold) (conn ?cold ?cnew) (nblocked ?cnew) (m2 ?player))
    :effect (and (at ?player ?cnew) (not (at ?player ?cold)) (not (m2 ?player)) (m1 ?player))
  )

  (:action move_door_1
    :parameters (?player - bot ?cold - coordinate ?cnew - coordinate)
    :precondition (and (at ?player ?cold) (conn ?cold ?cnew) (d1 ?cnew) (m1 ?player) (nblocked ?cold))
    :effect (and (at ?player ?cnew) (not (at ?player ?cold)) (not (m1 ?player)) (m2 ?player))
  )

  (:action move_door_2
    :parameters (?player - bot ?cold - coordinate ?cnew - coordinate)
    :precondition (and (at ?player ?cold) (conn ?cold ?cnew) (d2 ?cnew) (m2 ?player) (nblocked ?cold))
    :effect (and (at ?player ?cnew) (not (at ?player ?cold)) (not (m2 ?player)) (m1 ?player))
  )

  (:action pickup-arrow
    :parameters (?player - bot ?arr - arrow ?coord - coordinate)
    :precondition (and (at ?player ?coord) (at ?arr ?coord))
    :effect (and (not (at ?arr ?coord)) (is-collected ?arr))
  )

  (:action shoot-arrow_1
    :parameters (?player - bot ?arr - arrow ?coord1 - coordinate ?coord2 - coordinate)
    :precondition (and (at ?player ?coord1) (conn ?coord1 ?coord2) (wumpus ?coord2) (is-collected ?arr) (m1 ?player))
    :effect (and (not (wumpus ?coord2)) (nblocked ?coord2) (not (is-collected ?arr)) (not (m1 ?player)) (m2 ?player))
  )

  (:action shoot-arrow_2
    :parameters (?player - bot ?arr - arrow ?coord1 - coordinate ?coord2 - coordinate)
    :precondition (and (at ?player ?coord1) (conn ?coord1 ?coord2) (wumpus ?coord2) (is-collected ?arr) (m2 ?player))
    :effect (and (not (wumpus ?coord2)) (nblocked ?coord2) (not (is-collected ?arr)) (not (m2 ?player)) (m1 ?player))
  )

  (:action push-crate_1
    :parameters (?player - bot ?cplayer - coordinate ?ccrate - coordinate ?ctarget - coordinate)
    :precondition (and (at ?player ?cplayer) (conn ?cplayer ?ccrate) (conn ?ccrate ?ctarget) (push_conn ?cplayer ?ctarget) (crate ?ccrate) (nblocked ?ctarget) (m1 ?player))
    :effect (and (crate ?ctarget) (not (nblocked ?ctarget)) (not (crate ?ccrate)) (nblocked ?ccrate) (not (m1 ?player)) (m2 ?player) (at ?player ?ccrate) (not (at ?player ?cplayer)))
  )

  (:action push-crate_2
    :parameters (?player - bot ?cplayer - coordinate ?ccrate - coordinate ?ctarget - coordinate)
    :precondition (and (at ?player ?cplayer) (conn ?cplayer ?ccrate) (conn ?ccrate ?ctarget) (push_conn ?cplayer ?ctarget) (crate ?ccrate) (nblocked ?ctarget) (m2 ?player))
    :effect (and (crate ?ctarget) (not (nblocked ?ctarget)) (not (crate ?ccrate)) (nblocked ?ccrate) (not (m2 ?player)) (m1 ?player) (at ?player ?ccrate) (not (at ?player ?cplayer)))
  )

  (:action push-crate-in-pit_1
    :parameters (?player - bot ?cplayer - coordinate ?ccrate - coordinate ?ctarget - coordinate)
    :precondition (and (at ?player ?cplayer) (conn ?cplayer ?ccrate) (conn ?ccrate ?ctarget) (push_conn ?cplayer ?ctarget) (crate ?ccrate) (pit ?ctarget) (m1 ?player))
    :effect (and (not (pit ?ctarget)) (not (crate ?ccrate)) (nblocked ?ccrate) (nblocked ?ctarget) (not (m1 ?player)) (m2 ?player) (at ?player ?ccrate) (not (at ?player ?cplayer)))
  )

  (:action push-crate-in-pit_2
    :parameters (?player - bot ?cplayer - coordinate ?ccrate - coordinate ?ctarget - coordinate)
    :precondition (and (at ?player ?cplayer) (conn ?cplayer ?ccrate) (conn ?ccrate ?ctarget) (push_conn ?cplayer ?ctarget) (crate ?ccrate) (pit ?ctarget) (m2 ?player))
    :effect (and (not (pit ?ctarget)) (not (crate ?ccrate)) (nblocked ?ccrate) (nblocked ?ctarget) (not (m2 ?player)) (m1 ?player) (at ?player ?ccrate) (not (at ?player ?cplayer)))
  )

)