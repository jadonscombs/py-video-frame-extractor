"""
Driver script for the random video frame extractor.

This program allows extraction of random frames from an input video source,
and saves the frames in a designated destination in your image format of
choice (e.g. "png", "jpeg", etc.)

Please see <frame_capture_components.py> for more details.
"""

from sys import stderr
try:
    import frame_capture_components
    
except:
    print(
        "[random video frame extractor] error: "
        "core file 'frame_capture_components.py' could not be loaded.",
        file=stderr
    )
    raise SystemExit


# program entry point
if __name__ == '__main__':
    arg_parser = frame_capture_components.init_parser()
    args = arg_parser.parse_args()
    frame_capture_components.capture_frames_driver(args)