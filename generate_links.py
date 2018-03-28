"""Short script to generate all the links for inventory items.

This module solves the third problem listed in shell_helper.py, that is, that
there's no good way to get from a combination to the inventory items. This
takes the list of all combinations (in all_combinations.txt) and generates
a list of links to be posted on the ClickCritters forums.

See the list here: http://www.clickcritters.com/forum/view_topic.php?id=66512.
"""

from shell_helper import CombinationsReader


if __name__ == "__main__":
    cr = CombinationsReader("all_combinations.txt")

    # Get links for all combinations -- split into two for post formatting
    for comb in cr.combinations[:75]:
        links = cr.to_links(comb)

        print(f"\n\n{comb}")
        print(links)

    print("\n\n\n\n\n\n\n\n\n\n")
    print("BREAK THE POSTS HERE")
    print("\n\n\n\n\n\n\n\n\n\n")

    for comb in cr.combinations[75:]:
        links = cr.to_links(comb)

        print(f"\n{comb}")
        print(links)