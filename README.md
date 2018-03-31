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