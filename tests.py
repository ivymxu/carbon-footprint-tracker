from fetch_data import main
from io import StringIO
import sys
import os

def run_data_collection(capsys, monkeypatch, name):
    with open(f"tests-input/test-{name}.txt", "r") as infile:
        user_input = infile.read()
    with open(f"tests-expected-output/test-{name}.out.txt", "r") as infile:
        expected_output = infile.read()
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    main()
    captured = capsys.readouterr()
    assert captured.out == expected_output