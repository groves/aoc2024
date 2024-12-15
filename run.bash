# Get current date if no arguments are provided
current_day=$(date +%-d)
current_year=$(date +%Y)

# Parse arguments
day=${1:-$current_day}
year=${2:-$current_year}


filename="day$day.py"
if [[ -f "$filename" ]]; then
    python "$filename"
    exit $?
fi
open "https://adventofcode.com/${year}/day/${day}"

cat <<EOF > "$filename"
import inspect
import re
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=${day}, year=${year})

def d(vars):
    frame = inspect.currentframe().f_back
    print(*[f"{var}={frame.f_locals[var]}" for var in vars.split(" ")])

def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]

def part_a(input):
    result = 0
    return result


def part_b(input):
    result = 0
    return result


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}'")
        sys.exit(1)


for ex in puzzle.examples:
    print(ex.input_data)
example = puzzle.examples[0].input_data

check_example(part_a(example), None)
puzzle.answer_a = part_a(puzzle.input_data)

check_example(part_b(example), None)
puzzle.answer_b = part_b(puzzle.input_data)
EOF

python "$filename"
,edit "$filename"
