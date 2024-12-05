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
import sys
from aocd.models import Puzzle
from rich import print

puzzle = Puzzle(day=${day}, year=${year})


def part_a(input):
    result = ""
    return result


def part_b(input):
    result = ""
    return result


def check_example(actual, expected):
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}' with input\n{example}")
        sys.exit(1)


for ex in puzzle.examples:
    print(ex.input_data)
example = puzzle.examples[0].input_data

ex_a = part_a(example)
if ex_a == "":
    sys.exit(0)
check_example(ex_a, None)
puzzle.answer_a = part_a(puzzle.input_data)

ex_b = part_b(example)
if ex_b == "":
    sys.exit(0)
check_example(part_b, None)
puzzle.answer_b = part_b(puzzle.input_data)
EOF

python "$filename"
,edit "$filename"
