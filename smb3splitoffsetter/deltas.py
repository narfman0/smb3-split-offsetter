from smb3splitoffsetter.models import OffsetTypes


def get_deltas(original_type: OffsetTypes, target_type: OffsetTypes):
    if (
        original_type == OffsetTypes.MARIO_WAND_GRAB
        and target_type == OffsetTypes.KING_WAND_GRAB
    ):
        return get_mario_wand_grab_to_king_wand_grab_deltas()
    elif (
        original_type == OffsetTypes.MARIO_WAND_GRAB
        and target_type == OffsetTypes.LETTER
    ):
        return get_mario_wand_grab_to_peachs_letter_deltas()
    elif (
        original_type == OffsetTypes.KING_WAND_GRAB
        and target_type == OffsetTypes.LETTER
    ):
        return get_king_wand_grab_to_peachs_letter_deltas()
    elif (
        original_type == OffsetTypes.KING_WAND_GRAB
        and target_type == OffsetTypes.MARIO_WAND_GRAB
    ):
        return [i * -1 for i in get_mario_wand_grab_to_king_wand_grab_deltas()]
    elif (
        original_type == OffsetTypes.LETTER
        and target_type == OffsetTypes.KING_WAND_GRAB
    ):
        return [i * -1 for i in get_king_wand_grab_to_peachs_letter_deltas()]
    elif (
        original_type == OffsetTypes.LETTER
        and target_type == OffsetTypes.MARIO_WAND_GRAB
    ):
        return [i * -1 for i in get_mario_wand_grab_to_peachs_letter_deltas()]
    raise Exception(f"Unmatched case {original_type}->{target_type}")


def get_mario_wand_grab_to_peachs_letter_deltas():
    return list(
        map(
            lambda i, j: i + j,
            get_mario_wand_grab_to_king_wand_grab_deltas(),
            get_king_wand_grab_to_peachs_letter_deltas(),
        )
    )


def get_mario_wand_grab_to_king_wand_grab_deltas():
    # start: 0
    # world 1: 122157 - 121098 = 1059 = 17.638s
    # world 2: 146415 - 145352 = 1063 = 17.704s (+1 tile)
    # world 3: 178130 - 177075 = 1055 = 17.571s
    # world 4: 204575 - 203508 = 1067 = 17.771s (+2 tiles)
    # world 5: 239995 - 238932 = 1063 = 17.704s (+1 tile)
    # world 6: 279565 - 278513 = 1052 = 17.521s
    # world 7: 321765 - 320706 = 1059 = 17.638s (+1 tile)
    # world 8: 0
    return [0, 17.638, 17.704, 17.571, 17.771, 17.704, 17.521, 17.638, 0]


def get_king_wand_grab_to_peachs_letter_deltas():
    # frames_between_king_wand_grab_and_peachs_letter_w1 = 858
    # frames_between_king_wand_grab_and_peachs_letter_w2 = 865
    # of course they are different, lets just pick one in the middle and pretend its average
    peachs_letter_additional_s = 858 * 0.01664
    return [
        0,
        peachs_letter_additional_s,
        peachs_letter_additional_s,
        peachs_letter_additional_s,
        peachs_letter_additional_s,
        peachs_letter_additional_s,
        peachs_letter_additional_s,
        peachs_letter_additional_s,
        0,
    ]
