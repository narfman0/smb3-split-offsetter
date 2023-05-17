def get_deltas():
    # TODO pass this as an argument?
    split_on_peachs_letter = True
    frames_between_king_wand_grab_and_peachs_letter_w1 = 858
    frames_between_king_wand_grab_and_peachs_letter_w2 = 865  # of course they are different, lets just pick one in the middle and pretend its average
    peachs_letter_additional_s = (
        frames_between_king_wand_grab_and_peachs_letter_w2 * 0.01664
    )

    # start: 0
    # world 1: 122157 - 121098 = 1059 = 17.638s
    # world 2: 146415 - 145352 = 1063 = 17.704s (+1 tile)
    # world 3: 178130 - 177075 = 1055 = 17.571s
    # world 4: 204575 - 203508 = 1067 = 17.771s (+2 tiles)
    # world 5: 239995 - 238932 = 1063 = 17.704s (+1 tile)
    # world 6: 279565 - 278513 = 1052 = 17.521s
    # world 7: 321765 - 320706 = 1059 = 17.638s (+1 tile)
    # world 8: 0
    deltas = [0, 17.638, 17.704, 17.571, 17.771, 17.704, 17.521, 17.638, 0]

    if split_on_peachs_letter:
        deltas = [
            delta + peachs_letter_additional_s if delta else delta for delta in deltas
        ]
    return deltas
