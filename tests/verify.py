"""Run compiled homework programs; no third-party dependencies."""
from pathlib import Path
import os
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
build = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "build"
suffix = ".exe" if os.name == "nt" else ""
count = 0

def run(exercise, data="", code=0):
    global count
    result = subprocess.run([str(build / ("ex_" + exercise + suffix))],
                            input=data, text=True, capture_output=True, timeout=5)
    assert result.returncode == code, (exercise, data, result.stdout, result.stderr)
    count += 1
    return result.stdout

shape = run("2_21").splitlines()
assert len(shape) == 9
assert shape[0].split() == ["*********", "***", "*", "*"]
assert shape[-1].split() == ["*********", "***", "*", "*"]
assert all(line[:9] == "*       *" for line in shape[1:8])
assert "*****" in shape[2]

for data, lo, hi in [("1 2 3",1,3),("3 1 2",1,3),("2 3 1",1,3),
                     ("7 7 7",7,7),("-9 0 -3",-9,0),("4 4 -1",-1,4)]:
    out = run("2_23", data)
    assert f"Largest: {hi}\nSmallest: {lo}\n" in out
for value, label in [(0,"even"),(2,"even"),(7,"odd"),(-3,"odd"),(-4,"even")]:
    assert f"{value} is {label}." in run("2_24", str(value))
blocks = run("2_25").strip().split("\n\n")
assert len(blocks) == 3
for block, letter in zip(blocks, "SHT"):
    assert set(block) <= {letter, " ", "\n"} and len(block.splitlines()) == 7
for data, expected in [("12 3","12 is a multiple of 3."),
                       ("13 3","13 is not a multiple of 3."),
                       ("-12 3","-12 is a multiple of 3."),
                       ("0 3","0 is a multiple of 3."),
                       ("12 -3","12 is a multiple of -3."),
                       ("-2147483648 -1","-2147483648 is a multiple of -1.")]:
    assert expected in run("2_26", data)
run("2_26", "1 0", 1)
pyramid = "    *\n   ***\n  *****\n *******\n*********\n"
assert run("2_27") == pyramid * 2
rows = run("2_31").splitlines()
assert rows[0] == "number\tsquare\tcube"
assert len(rows) == 12
assert rows[1] == "0\t0\t0" and rows[-1] == "10\t100\t1000"
for row in rows[1:]:
    n, square, cube = map(int, row.split("\t"))
    assert square == n ** 2 and cube == n ** 3
assert "BMI: 20.76" in run("2_32", "60 1.7")
assert "BMI: 25.00" in run("2_32", "100 2")
assert "Underweight: less than 18.5" in run("2_32", "60 1.7")
run("2_32", "60 0", 1)
run("2_32", "-1 1.7", 1)
assert "Daily driving cost: 260.00" in run("2_33", "60 30 15 100 40")
assert "Daily driving cost: 0.00" in run("2_33", "0 30 15 0 0")
assert "Daily driving cost: 73.00" in run("2_33", "25 31.5 12.5 10 0")
run("2_33", "60 30 0 0 0", 1)
for ex in ("2_23","2_24","2_26","2_32","2_33"):
    run(ex, "invalid", 1)
print(f"PASS: all 9 exercises, {count} program runs")
