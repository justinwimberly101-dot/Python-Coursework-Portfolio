# Python Coursework Portfolio

A collection of Python programs written across two semesters of coursework at George Mason University during my freshman year, organized by concept rather than assignment number. This repo tracks my progression from basic syntax through functions, control flow, data structures, file I/O, and exception handling.

Why I organized it this way

Assignment numbers don't mean much to someone browsing a GitHub profile. Grouping by concept makes it easier to see skill progression and to jump straight to, say, "recursion" or "file I/O" if that's what you're evaluating.

## Structure

```
portfolio/
├── semester-1-cs108/
│   ├── 01_intro_print_statements.py
│   ├── 02_expressions_arithmetic.py
│   ├── 03_functions_intro.py
│   ├── 04_custom_functions.py
│   ├── 05_conditionals.py
│   ├── 06_while_loops.py
│   ├── 07_for_loops.py
│   ├── 08_lists.py
│   ├── 09_nested_lists.py
│   ├── 10_tuples.py
│   └── 11_strings_pattern_matching.py
└── semester-2-201/
    ├── 01_list_processing.py
    ├── 02_2d_lists_mutation.py
    ├── 03_dictionaries.py
    ├── 04_recursion_defaults.py
    ├── 05_file_io.py
    └── 06_exceptions.py
```

## Semester 1 — CS108 (Intro Programming)

| File | Concept | Key functions |
|---|---|---|
| `01_intro_print_statements.py` | Print statements, variables, arithmetic | — |
| `02_expressions_arithmetic.py` | Expressions, quadratic formula, floor div/modulo | — |
| `03_functions_intro.py` | Calling functions & parameters (provided helpers) | `largest`, `average_three`, `odd_or_even` |
| `04_custom_functions.py` | Writing original functions from a spec | `cm_to_in`, `rect_perimeter`, `speaker_price` |
| `05_conditionals.py` | If/elif/else logic | `circ_calc`, `kind_of_roots`, `stock_advice`, `level_up2` |
| `06_while_loops.py` | While loops & accumulators | `sum_up`, `power_up`, `mystery_sum`, `bigger_mystery` |
| `07_for_loops.py` | For loops & range | `count_prop_facs`, `add_elems`, `count_zeros` |
| `08_lists.py` | List indexing, mutation, filtering | `half_em`, `only_negs`, `calc_avgs`, `coin_matches` |
| `09_nested_lists.py` | 2D / nested lists | `menu`, `find_largest`, `is_square` |
| `10_tuples.py` | Tuples & immutability | `extremes`, `count_vowels`, `count_distinct_elements` |
| `11_strings_pattern_matching.py` | String manipulation, manual pattern matching | `pig_latin_sentence`, `hidden_word` (word search grid) |

## Semester 2 — CS201 (Intermediate Programming)

| File | Concept | Key functions |
|---|---|---|
| `01_list_processing.py` | Filtering & merging parallel lists | `membership_cancellation`, `report_attendance` |
| `02_2d_lists_mutation.py` | 2D lists & in-place mutation | `rank_players`, `build_team`, `find_duplicate` |
| `03_dictionaries.py` | Dictionaries, sets, nested structures | `make_group`, `merge_dicts`, `swap` |
| `04_recursion_defaults.py` | Default parameters & recursion | `calculate_bonus`, `replaceLetter`, `sum_digits` |
| `05_file_io.py` | Reading/writing CSV & TXT files | `get_info`, `find_students`, `final_grade` |
| `06_exceptions.py` | Nested try/except handling | `find_division`, `check_timestamp` |

## Highlights

A few programs worth a closer look if you're skimming:

- **`11_strings_pattern_matching.py`** — builds Pig Latin translation and a horizontal/vertical word search solver from scratch, without relying on built-in string search methods.
- **`06_exceptions.py`** — layered exception handling that validates a timestamp string (`HH:MM:SS`) against format, type, and range errors.
- **`05_file_io.py`** — reads structured CSV data, computes per-student averages, and writes letter grades back out to a new file.

## What I learned

This coursework moved from printing strings to manipulating nested data structures, handling files, and writing defensive code with exception handling. Early files are simple and procedural; later ones reflect more deliberate design — helper functions, recursion, and validation logic.

---
*Note: original assignment files included honor code statements required by the course; those have been removed here since they're not relevant outside the classroom context.*
