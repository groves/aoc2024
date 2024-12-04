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
    for line in input.splitlines():
        pass
    return result


def part_b(input):
    result = ""
    return result


def check_example(solver, input, expected):
    actual = solver(input)
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}' with input\n{input}")
        sys.exit(1)


example = """"""
if example == "":
    for ex in puzzle.examples:
        print(ex)
else:
    check_example(part_a, example, None)

poss_a = part_a(puzzle.input_data)
if poss_a == "":
    sys.exit(0)
puzzle.answer_a = part_a(puzzle.input_data)
if True:
    sys.exit(0)
check_example(part_b, example, None)
puzzle.answer_b = part_b(puzzle.input_data)
EOF

python "$filename"
,edit "$filename"
