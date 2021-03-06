(defrule normal
    (number_1 5)
    (number_2 7)
    (number_3 15)
    (number_4 5)
    (number_5 8)
    (number_6 6)
    (number_7 45)
    (number_8 73)
    (number_9 12)
    (number_10 42)
    =>
    (assert (people_is normal))
    (printout t "Normal User" crlf)
)

(defrule parsial_colorBlind
    (not (number_1 5))
    (not (number_2 7))
    (not (number_3 15))
    (not (number_4 5))
    (not (number_5 8))
    (not (number_6 6))
    (not (number_7 45))
    (not (number_8 73))
    (number_9 12)
    (not (number_10 42))
    =>
    (assert(people_is partial_colorBlind))
    (printout t "Parsial color blind user" crlf)
)

(defrule total_colorBlind
    (not (number_1 5))
    (not (number_2 7))
    (not (number_3 15))
    (not (number_4 5))
    (not (number_5 8))
    (not (number_6 6))
    (not (number_7 45))
    (not (number_8 73))
    (not(number_9 12))
    (not (number_10 42))
    =>
    (assert(people_is total_colorBlind))
    (printout t "Total color blind user" crlf)
)