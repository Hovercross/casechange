from lowercase import __version__
from lowercase.lowercase import lowercase_stream

from io import StringIO

def test_version():
    assert __version__ == '0.1.0'

def test_to_lower():
    test_data = "aBcDeFGHIJKL"
    expected_data = "abcdefghijkl"

    input_stream = StringIO(test_data)
    out_stream = StringIO()

    lowercase_stream(input_stream, out_stream)
    assert out_stream.getvalue() == expected_data
