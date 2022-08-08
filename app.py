import pandas as pd


# fix data so all artists on a song are in that row rather than the main one

"""
1. all songs are relatively popular, but say yes if you want the algorithm to prioritize popularity, no otherwise


Yes to prioritize popularity:
Explain that everything is weighted
2. is there an artist on the following list (positive coefficients) you don't want to see any songs from? (remove)
3. is there an artist on the following list (negative coefficients) you definitely want to see songs from (reweight)?
4. show list of genres that affect popularity - explain they are weighted and select some you want removed or some to double
their importance


No to prioritize popularity
2. is there an artist you definitely don't want to see songs from? (remove)
3. artists you like and on a scale of 5 to 10 (5 being that you listen from time to time and 10 is one of your favorites)


4. search a keyword for a genre you like - returns list
5. type remove followed by a comma separated list of genres if you want to remove some,
    or same with keep if you just want to keep a few
6
"""
