"""Helpers for the Easter 2018 event on ClickCritters.

ClickCritters [clickcritters.com] is an adoptable site where you can collect
adoptables, play games, interact with other users, and more. From March 24
to April 15, 2018, they are hosting an Easter event.

In this event, users have to reassemble eggs using the egg fragments that are
collected from around the site. Each egg takes nine pieces to assemble --
numbered 1 through 9 -- and each fragment comes in 5 types, A through E. There
are therefore 45 types of egg fragments (1a, 2a, ..., 9a, 1b, ..., 9b, ... 9e).

The main challenge associated with the event is assembling 150 different kinds
of eggs, given on a preset list of combinations. A combination is a string of
9 letters, e.g., daddecbca. This combination means we need egg fragments 1d,
2a, 3d, 4d, ..., 9a to create this particular egg.

Upon playing the event, I made several observations:
 - knowing which combinations you can make, given your inventory, is difficult
 - knowing if you have the right fragments to make a particular combination is
   difficult
 - navigating from the combination (daddecbca) to the inventory pages for each
   fragment is difficult

This module solves the first two problems. Given a list of combinations that
the user needs, and a copy of their inventory that contains egg fragments, we
generate a list of the combinations that they are able to make.

Terminology: 
 - egg fragment = shell fragment = shell = fragment: one item (e.g., 4c)
 - combination = set of 9 fragments (e.g., daddecbca)
"""

import itertools

from collections import Counter
from typing import Counter, Dict, List


class Reader:
    """Class to read shell fragments information from files.

    Attributes
    ----------
    shells : Counter
        Counter that keeps track of how many egg fragments are associated
        with this file.

    Methods
    -------
    from_file : str -> Counter
        Abstract method, even though these don't really exist in Python.
        Read from a file and update self.shells with that information.
    """

    def __init__(self, f: str):
        self.shells = self.from_file(f)


class CombinationsReader(Reader):
    """Class to read from a list of combinations. 

    A combination is a string, e.g., daddecbca (must be lowercase). The list
    of combinations is of the form:
        aaaaaaaaa
        bbbbbbbbb
        ccccccccc
        ddddddddd
        eeeeeeeee
        daddecbca
        dbdcbbdec
        [ ... ]

    Attributes
    ----------
    shells : Counter
        Keep track of how many egg shells are needed to make all combinations.

    combinations : List[str]
        List of combination strings that are read from a file.

    Methods
    -------
    from_file : str -> Counter
        See Reader.from_file.

    parse_combination : str -> List[str]
        Read a single combination and convert it to a list of fragments.

    to_links : str -> str
        Convert a combination to HTML links to the needed inventory pages.
    """

    def __init__(self, f: str):
        Reader.__init__(self, f)

        print(f"Finished reading combinations from file.")
        print(f"You need these fragments: {self.shells}\n")

    def from_file(self, f: str) -> Counter:
        """Read list of combinations from a file.

        Effect: update self.combinations with list of combinations.
        """

        shells: List[str] = [ ]
        combination_list: List[str] = [ ]
        with open(f, "r") as combs:
            for line in combs:
                # Some lines are empty
                if not line.strip():
                    continue

                fragments: List[str] = self.parse_combination(line.strip())
                shells.extend(fragments)
                combination_list.append(line.strip())

        self.combinations = combination_list
        return Counter(shells)

    def parse_combination(self, s: str) -> List[str]:
        """Read a combination and convert it to a list of fragments needed.

        Char X at position i means the shell piece required is iX.
        e.g., "ab" is [1a, 2b] and "dc" is [1d, 2c].
        """

        chars: List[str] = [ ]
        for i, c in enumerate(s):
            x: str = str(i + 1) + c
            chars.append(x)

        return chars

    def to_links(self, s: str) -> str:
        """Convert a combination to a list of links.

         e.g., 1a is http://www.clickcritters.com/iteminfo.php?itemid=437
              2a is http://www.clickcritters.com/iteminfo.php?itemid=438
              ...

        If you map the letters a = 0, b = 1, ... , e = 5, and you have
        the numbers 1 through 9, then the item ID is given by
        436 + 9*letter + number.
        """

        letters: Dict[str, int] = {
            "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e": 4
        }

        url_base: str = "http://www.clickcritters.com/iteminfo.php?itemid="
        links: str = f""
        for i, c in enumerate(s):
            letter: str = letters[c]
            number: int = i + 1
            item_id: int = 436 + 9 * letter + number
            item_name: str = str(i + 1) + c

            links += f'<a href="{url_base}{item_id}">{item_name}</a>'

        return links


class InventoryReader(Reader):
    """Class to read shell fragments from a user's inventory.

    A user's inventory must be copy/pasted from clickcritters.com/items.php
    and has the following format:

        Egg Fragment (1a)
        x4
            

        Egg Fragment (2a)
        x5
            

        Egg Fragment (3a)
        x20

    Note arbitrary amounts of whitespace between lines. Each line that is not
    whitespace will be either the name of an egg fragment or the number of the
    previous egg fragment that the user has. We make use of this structure
    when reading the file.
            

    Attributes
    ----------
    shells : Counter
        Keep track of how many egg fragments this user has.

    Methods
    -------
    from_file : str -> Counter
        See Reader.from_file.

    get_combinations : CombinationsReader -> None
        Given a CombinationsReader, print out egg combinations we can make.
    """

    def __init__(self, f: str):
        Reader.__init__(self, f)

        print(f"Finished reading inventory from file.")
        print(f"You have these fragments: {self.shells}\n")

    def from_file(self, f: str) -> Counter:
        """Read a user's inventory and return the fragments they have."""

        shells: Counter = Counter()
        with open(f, "r") as items:
            current_item: str = None
            for line in items:
                # Some lines are empty
                if not line.strip():
                    continue

                # Check if it's an item name, if so then get fragment type
                elif line[:3] == "Egg":
                    current_item = line[-4:-2]

                # Otherwise, it's a number associated with previous item
                else:
                    num: int = int(line[1:])
                    shells[current_item] = num

        return shells

    def get_combinations(self, cr: CombinationsReader) -> None:
        """Given a CombinationsReader, print out combinations we can make."""

        for comb in cr.combinations:
            fragments: List[str] = cr.parse_combination(comb)
            need: Counter = Counter(fragments)

            # For each shell in the combination, check if it exists in the
            # inventory. If we have them all, then we can make that one.
            shell: str
            for shell in need:
                if shell not in self.shells:
                    break
            else:
                fragment_names: str = " ".join(need.keys())
                print(f"You can make {comb} with {fragment_names}")

    def get_differences(self, cr: CombinationsReader) -> None:
        """Get numbers of needed shells and extra shells.

        Given the combinations we need to make (cr) and the fragments
        that we have, print out which fragments we still need to gather and
        which fragments we have extras of (and how many of both).
        """

        # Build differences of how many fragments we need and have. The
        # Counter will be (#need - #have), so positive numbers represent us
        # needing some of a certain fragment, and negative numbers represent
        # us having extras.
        differences: Counter = Counter(cr.shells)
        differences.subtract(self.shells)

        print("These are the shells you still need:")
        for shell, num in differences.most_common():
            if num > 0:
                print(f"{shell}: you need {num} more ({cr.shells[shell]} total)")
            else:  # break once we're past the ones we need
                break

        print("\nThese are the shells you have extras of:")
        for shell, num in differences.most_common():
            if num < 0:
                print(f"{shell}: you have {-1 * num} extra ({self.shells[shell]} total)")

        return



if __name__ == "__main__":
    cr = CombinationsReader("combinations.txt")
    ir = InventoryReader("inventory.txt")

    ir.get_combinations(cr)
    ir.get_differences(cr)
