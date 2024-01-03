# About
This is a Dungeons and Dragons character builder program for 5th edition D&D.  
It lets you choose your name, class, race, background and select feats.  
You can also roll for ability scores and hitpoints.  

For class, race, background and feats data, all of them are taken from the  
freely available ruleset up on Wizards of the Coast's site, however  
this program does support homebrew.  

Currently you can only select Elf, Barbarian, the Acolyte background and the Grappler feat.
These are included in the repo under Data/.

There is an empty character file under My Characters/, delete it if you wish.

# How to use
All data is read from text files under the Data/ folder contained in this repo.  
**Make sure to download it, otherwise the program has no data to read.**

To make a custom class, race, background or feat, simply  
follow the same syntax as in the existing .txt files.  
For example, for the Barbarian equipment is marked with the   
[Equipment start] and [Equipment end] indicators.  
Equipment information is then written in between those two lines.  

Needs an empty line between the indicators and actual content.  

For hit dice, make sure it's formatted in the following way:  

>[Hit Dice]
>Hit dice: 1d12

As for level up information, make sure proficiency bonus is formatted the following way:

>Level 3:
>Proficiency bonus: +2

I.e. level first, then a newline and the proficiency bonus written verbatim.

And of course, make sure your custom files are in the correct folder.

After asking for some user input, the program should automatically find all
relevant information from the existing text files.


# Starting the program
Starting the program should be simple.
If you don't already have Python 3.12.1 installed, go download it [here](https://www.python.org/downloads/?ref=blog.segmind.com).  
**No additional python modules are needed.**  
Once you have Python installed, simply double click the .py file to run the program.  
Again, make sure all files from this repo are in the same folder.  
