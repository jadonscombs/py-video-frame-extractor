import argparse
import ffmpeg
import numpy
import cv2
import os
import re
import sys
import random
import traceback


"""
[STEPS]:
    1. open a video as cv2.VideoCapture object "cap"
    2. get video duration (seconds) with:
        - fps = cap.get(cv2.CV_CAP_PROP_FPS)
        - frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    3. choose a random frame:
        - cap.set(1, random.randint(1, frame_count - 1))
    4. capture and write frame to file
        - ret, frame = cap.read()
        - cv2.imwrite("random-img.png", frame)

[RESOURCES]:
- https://github.com/kkroening/ffmpeg-python/issues/165 (reading out errors)
- https://stackoverflow.com/questions/33523751/
  getting-specific-frames-from-videocapture-opencv-in-python
- https://www.geeksforgeeks.org/
  how-to-get-properties-of-python-cv2-videocapture-object/
- https://stackoverflow.com/questions/49048111/
  how-to-get-the-duration-of-video-using-cv2
- https://docs.python.org/3/library/re.html


"""

def init_parser():
    """
    Initialize an ArgumentParser to parse user-supplied command-line args.

    Returns a fully initialized argparse.ArgumentParser object.
    """
    
    parser = argparse.ArgumentParser(
        description="Save a random frame from an input video source."
    )

    # (-n): optional arg., number of randomly sampled frames to save
    parser.add_argument('-n', type=int, default=1,
                        help="specify desired number of random frames to save")

    # TODO: (-p): optional arg., file naming pattern to follow

    # (-o): specify output path to save images
    parser.add_argument('-o', type=str, default="",
                        help="specify output path to save images")

    # (-e): specify output image type (png, jpeg, ...)
    parser.add_argument('-e', type=str, default="png",
                        help="specify output image type/extension")

    # (--verbose): enable verbose output (disabled by default)
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="display detailed information during processing")

    # video_path: required arg., input video file path
    parser.add_argument('video_source', type=str,
                        help="specify source video filepath")

    return parser


def capture_frames_driver(parser_args):
    """
    Primary driver function to save image files.
    """

    cap = cv2.VideoCapture(args.video_source)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    regex_filename_pattern = re.compile(r"img-extract-(\d+)\." + args.e)
    new_filename_pattern = ("img-extract-{}." + args.e)
    new_filename = new_filename_pattern.format(0)

    # argparsing (-n): check that <n> is within allowed bounds
    if args.n < 1 or args.n > 100:
        print("Error: argument 'n' must be between 1 and 100 (inclusive)")
        exit(1)

    # informational output
    if args.verbose:
        print(
            "\n"
            f"Source: {args.video_source}\n"
            f"Total frames: {total_frames}\n"
            f"Frames to sample: {args.n}"
        )
        if args.o:
            print(f"Target directory: {args.o}\n")

        print("Now capturing random frames...")
    

    # argparsing (-n): capture <n> randomly sampled frames
    last_match = -1
    n_writes = 0
    for frame_i in range(args.n):
        
        cap.set(1, random.randint(1, total_frames - 1))
        ret, frame = cap.read()

        # set target directory for 'os.listdir()' to search
        target_directory = args.o if bool(args.o) else None
        
        for f in os.listdir(target_directory):
            match = regex_filename_pattern.match(f)
            if match:
                if int(match.group(1)) <= last_match:
                    continue
                last_match = int(match.group(1))

        if args.verbose:
            print(f"updated 'last_match' to {last_match}")    
        new_suffix = int(last_match) + 1
        new_filename = new_filename_pattern.format(new_suffix)
        new_filename = os.path.join(args.o, new_filename)

        # save frame as png to file
        cv2.imwrite(new_filename, frame)
        n_writes += 1

    # informational output
    if args.verbose:
        print(f"Operation complete: finished saving {n_writes} frames.")


if __name__ == '__main__':
    arg_parser = init_parser()
    args = arg_parser.parse_args()
    capture_frames_driver(args)

    
    
