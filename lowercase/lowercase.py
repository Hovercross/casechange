"""Convert stream to lowercase"""

from typing import TextIO

def lowercase_stream(in_stream: TextIO, out_stream: TextIO):
    for data in in_stream:
        out_stream.write(data.lower())
