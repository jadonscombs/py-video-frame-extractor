"""
Driver script for the random video frame extractor.

This program allows extraction of random frames from an input video source,
and saves the frames in a designated destination in your image format of
choice (e.g. "png", "jpeg", etc.)

Please see <frame_capture_components.py> for more details.
"""

import sys
try:
    import frame_capture_components as extractor
    
except:
    print(
        "[random video frame extractor] error: "
        "core file 'frame_capture_components.py' could not be loaded.",
        file=sys.stderr
    )


# program entry point
if __name__ == '__main__':
    arg_parser = extractor.init_parser()
    args = arg_parser.parse_args()
    extractor.capture_frames_driver(args)