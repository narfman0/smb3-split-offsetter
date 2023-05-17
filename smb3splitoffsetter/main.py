#! /usr/bin/env python3

import datetime
import re
import xml.etree.ElementTree as ET

from smb3splitoffsetter.deltas import get_deltas
from smb3splitoffsetter.models import OffsetTypes


def get_time(time_element):
    t = re.sub(r"(?<=\.\d\d\d)0000", "000", time_element.text)
    t = re.sub(r"(:\d\d)$", r"\1.000000", t)

    # strptime only supports 6 numerals after the decimal
    dot_index = t.find(".")
    if dot_index < len(t) - 7:
        t = t[0 : dot_index + 7]

    return datetime.datetime.strptime(t, "%H:%M:%S.%f")


def set_time(time_element, time):
    time_element.text = datetime.datetime.strftime(time, "%H:%M:%S.%f")


def main(infile: str, outfile: str, type: str):
    tree = ET.parse(infile)
    root = tree.getroot()
    deltas = get_deltas(OffsetTypes[type.upper()])

    for world, segment in enumerate(root.find("Segments"), start=1):
        dt_split = datetime.timedelta(seconds=deltas[world])
        dt_segment = datetime.timedelta(seconds=deltas[world] - deltas[world - 1])
        for split_time in segment.find("SplitTimes"):
            t = get_time(split_time.find("RealTime"))
            set_time(split_time.find("RealTime"), t + dt_split)
        best_segment_time = segment.find("BestSegmentTime")
        t = get_time(best_segment_time.find("RealTime"))
        set_time(best_segment_time.find("RealTime"), t + dt_segment)
        for segment_time in segment.find("SegmentHistory"):
            if segment_time.find("RealTime") != None:
                t = get_time(segment_time.find("RealTime"))
                set_time(segment_time.find("RealTime"), t + dt_segment)

    tree.write(outfile)
