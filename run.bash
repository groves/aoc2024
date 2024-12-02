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
    if isinstance(actual, int):
        actual = str(actual)
    if actual != expected:
        print(f"Expected '{expected}' but got '{actual}' with input\n{input}")
        import sys

        sys.exit(1)


for example in puzzle.examples:
    if example.answer_a is not None:
        check_example(part_a, example.input_data, example.answer_a)
    if example.answer_b is not None:
        check_example(part_b, example.input_data, example.answer_b)

poss_a = part_a(puzzle.input_data)
if poss_a != "":
    puzzle.answer_a = part_a(puzzle.input_data)
poss_b = part_b(puzzle.input_data)
if poss_b != "":
    puzzle.answer_b = part_b(puzzle.input_data)
EOF

python "$filename"
,edit "$filename"
