# Philosophy Game

## General Information

The Philosophy Game is a quantitative experiment to see how many steps any topic on Wikipedia is from the "Philosophy" page. This repository holds a simple Python script that does just that. It is a very simple script that does not deal with cases such as loops or invalid links. In practice we ran it in a bash script and a time out to rule out those corner cases.

## How To Get Going

To find out how many steps it takes to get to "Philosophy" run:

```shell
python exec.py "DESIRED TOPIC"
```

## File Information

* `exec.py` -- A command-line wrapper that takes in the topic as an argument and runs the scraper script.
* `algorithm.py` -- Contains the algorithm, which relies on the HTML parser, to "walk" the pages until "Philosophy" is reached.
* `html_parser.py` -- All HTML parsing logic, such as finding the first link on each Wikipedia page is here.
* `The Game of Philosophy.pdf` -- Presentation given to the class at the end of the semester showcasing our results of running the script on a random sample of Wikipedia pages (scraped from their archive).
