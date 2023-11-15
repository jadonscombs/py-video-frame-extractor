# py-video-frame-extractor

## Overview

A simple program to extract and save individual video frames

## Quick Start

This program is intended to run on the command-line, and requires the `opencv-python` package to run.

## Usage

```
usage: frame_extractor_driver.py [-h] [-n N_FRAMES] [-p PATTERN] [-o OUTPUT_DIR] [-e FILETYPE] [-v] SOURCE

Save a random frame from an input video source.

positional arguments:
  SOURCE         specify source video filepath

options:
  -h, --help     show this help message and exit
  -n N_FRAMES    specify desired number of random frames to save
  -p PATTERN     specify filename prefix for newly created files
  -o OUTPUT_DIR  specify output directory to save images
  -e FILETYPE    specify output image type/extension
  -v, --verbose  display detailed information during processing
```
