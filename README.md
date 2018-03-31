# cc-easter
This repository contains scripts I used to help with the 2018 Easter event on [ClickCritters](http://www.clickcritters.com). I originally made this for the purpose of helping myself with the event tasks, then wrote something else to help others, then cleaned up the code for learning's sake.

## Motivation
In this event, users have to reassemble eggs using the egg fragments that are collected from around the site. Each egg takes nine pieces to assemble -- numbered 1 through 9 -- and each fragment comes in 5 types, A through E. There are therefore 45 types of egg fragments (1a, 2a, ..., 9a, 1b, ..., 9b, ... 9e).

The main challenge associated with the event is assembling 150 different kinds of eggs, given on a preset list of combinations. A combination is a string of 9 letters, e.g., daddecbca. This combination means we need egg fragments 1d, 2a, 3d, 4d, ..., 9a to create this particular egg.

Upon playing the event, I made several observations:
 - knowing which combinations you can make, given your inventory, is difficult
 - knowing if you have the right fragments to make a particular combination is difficult
 - navigating from the combination (daddecbca) to the inventory pages for each fragment is difficult

*N.B. These difficulties were alleviated with a site update on 3/29/2018, but I wrote these and completed the event prior to that.*

## Purpose
One script, `shell_helper.py`, figures out (1) what combinations I needed and what fragments I currently had, (2) which egg fragments I still needed, and (3) what combinations I could currently make. This solved the first two problems above.

The second script, `generate_links.py`, generates a list of links that take you to the inventory pages for each egg fragment in a combination. See the list [here](http://www.clickcritters.com/forum/view_topic.php?id=66512).

## Files Included
Python scripts:
 * `shell_helper.py` -- see above
 * `generate_links.py` -- see above

Text (data) files:
 * `inventory.txt` -- copy/pasted list of egg fragments from user inventory
 * `combinations.txt` -- list of combinations you still need, from the event page
 * `all_combinations.txt` -- list of all combinations needed

## Usage
Both files require Python >= 3.6 (f-strings!).

`python shell_helper.py` (requires the existence of `inventory.txt` and `combinations.txt`)

`python generate_links.py` (requires the existence of `all_combinations.txt`)

Neither script does any error handling, because these were made for personal use only. I also don't know anything about how to properly package Python modules, so the organization could likely be better. But that's all part of learning!

## Example Usage

```
$ python shell_helper.py

Finished reading combinations from file.
You need these fragments: Counter({'3d': 6, '9b': 4, '4e': 4, '5a': 3, '6a': 3, '2c': 3, '9a': 3, '1a': 2, '7e': 2, '8d': 2, '8b': 2, '7c': 2, '1d': 2, '5e': 2, '8a': 2, '2e': 2, '6c': 2, '7b': 2, '2d': 1, '4b': 1, '1c': 1, '5b': 1, '6d': 1, '1b': 1, '2b': 1, '3e': 1, '4d': 1, '8e': 1, '6e': 1, '7a': 1, '5c': 1, '1e': 1, '4a': 1})

Finished reading inventory from file.
You have these fragments: Counter({'1b': 33, '6b': 31, '4e': 29, '3a': 27, '6c': 27, '2e': 26, '9d': 25, '6d': 23, '1d': 22, '3b': 20, '4c': 20, '2d': 20, '5e': 20, '3c': 18, '8a': 17, '8b': 17, '7e': 17, '1c': 16, '9c': 16, '3e': 16, '7a': 15, '8e': 15, '4a': 14, '6a': 13, '2b': 13, '8c': 12, '1e': 12, '6e': 11, '2a': 10, '4b': 10, '5c': 10, '9e': 10, '8d': 9, '1a': 8, '5a': 8, '5b': 8, '7d': 7, '7b': 5, '4d': 5, '9b': 4, '2c': 3, '5d': 3, '9a': 2, '7c': 2})

You can make bbedaaceb with 1b 2b 3e 4d 5a 6a 7c 8e 9b

These are the shells you still need:
3d: you need 6 more (6 total)
9a: you need 1 more (3 total)

These are the shells you have extras of:
7b: you have 3 extra (5 total)
5d: you have 3 extra (3 total)
4d: you have 4 extra (5 total)
5a: you have 5 extra (8 total)
1a: you have 6 extra (8 total)
[ ... snipped the rest of this ... ]
```