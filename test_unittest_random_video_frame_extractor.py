"""
This file contains unit tests to run on the video frame extractor application.

STANDALONE: This unit testing file can be run as a standalone script, which
imports the 'random_video_frame_extractor.py' driver script.

This file is also a basis for experimenting with the built-in <unittest>
Python module.


TESTS TO RUN (PER FUNCTION):
[init_parser]
    - test successful initialization (returned obj is not None)

[capture_frames_driver]
    - valid/invalid cases for "-n" arg (number of sampled frames to save):
        - N out of range of [MIN_SAMPLES_PER_RUN, MAX_SAMPLES_PER_RUN]
        - user passes string as N
        
    - valid/invalid cases for "-o" arg (output destination path):
        - nonexistent filepath
        - a direct file is specified, but not a directory
        
    - valid/invalid cases for "-e" arg (image extension):
        - string of digits specified
        - only non-alphanumeric symbols specified, e.g.: [. % / \ # @ ]
        
    - valid/invalid cases for "-v"/"--verbose" arg:
        - arg supplied when "-v" does not accept args
        
    - valid/invalid cases for "video_source" arg:
        - non-video file supplied
        - test with .MKV files
        - test with .MP4 files
        - test with .MOV files
"""


import unittest
import random_video_frame_extractor as extractor


class TestInitParser(unittest.TestCase):
    pass
    
    
class TestCaptureFramesArgParser(unittest.TestCase):
    pass

    # testing "-n" arg handling
    def test_n_samples_arg(self):
        """
        Testing argument handling for "-n" option
        """
        pass
    
    # testing "-o" arg handling
    def test_output_destination_arg(self):
        """
        Testing argument handling for "-o" option
        """
        pass
        
    # testing "-e" arg handling
    def test_output_file_ext_arg(self):
        """
        Testing argument handling for "-e" option
        """
        pass
    
    # testing "-v" arg handling
    def test_verbose_arg(self):
        """
        Testing argument handling for "-v" option
        """
        pass
    
    # testing "video_source" arg handling
    def test_input_video_source_arg(self):
        """
        Testing argument handling for "video_source" option
        """
        pass
    
