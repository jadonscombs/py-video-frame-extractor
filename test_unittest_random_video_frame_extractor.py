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
        

TODO:
- add timeit functionality (test testing performance/metrics)
- HIGH PRIORITY: auto-deletion of frames/images generated during testing
- add new tests to test <frame_capture_components.py>
"""


import unittest
import frame_capture_components as extractor
import traceback
    
    
class TestCaptureFramesArgParser(unittest.TestCase):
    
    def get_test_video_file(self):
        return "kaleidoscope.mp4"
    
    # boolean arg validation helper
    def validate_args(self, parser, arglist) -> bool:
        """
        Catches argument errors.
        
        Return False if error, otherwise return True.
        """

        video_file = self.get_test_video_file()
        
        try:
            args = parser.parse_args(arglist + [video_file])
            return True
        except:
            return False
        

    # testing "-n" arg handling
    def test_n_samples_arg(self):
        """
        Testing argument handling for "-n" option
        """

        # initialize argument parser
        parser = extractor.init_parser()

        # (valid cases)
        self.assertTrue(self.validate_args(parser, ['-n', '1']))
        self.assertTrue(self.validate_args(parser, ['-n', '32']))
        self.assertTrue(self.validate_args(parser, ['-n', '100']))
        
        # non-numeric value given
        self.assertFalse(self.validate_args(parser, ['-n', 'XYZ']))
        self.assertFalse(self.validate_args(parser, ['-n', 'c']))
        
        # invalid number of args (0 or 2+)
        self.assertFalse(self.validate_args(parser, ['-n', 'arg1', 'arg2']))
        self.assertFalse(self.validate_args(parser, ['-n']))
        
        # test behavior with capture_frames_driver() method;
        # TODO: add "assertXXX" statements later
        capture_frames_driver_testargs_list = [
            ('-n', '1'),
            ('-n', '15'),
            
            ('-n', '-1'),
            ('-n', '101'),
            ('-n', '285000'),
            ('-n', 'XYZ'),
            ('-n', 'c'),
            ('-n', 'arg1', 'arg2'),
            ('-n',)
        ]

        for arglist in capture_frames_driver_testargs_list:
            args = arglist + (self.get_test_video_file(),)

            try:
                self.assertTrue(parser.parse_args(args))
                args = parser.parse_args(args)
                self.assertTrue(extractor.capture_frames_driver(args))
            except:
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
        
        
if __name__ == "__main__":
    unittest.main()
    
