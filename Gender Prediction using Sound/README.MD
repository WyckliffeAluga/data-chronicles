
Overview 

Analyze the gender distribution of children's book writers and use sound to match names to gender.

Description 

The same name can be spelled out in a many ways
(for example, Marc and Mark, or Elizabeth and Elisabeth). 
Sound can, therefore, be a better way to match names than spelling. 
In this project, I will use the Python package Fuzzy to find out the genders of authors that have
appeared in the New York Times Best Seller list for Children's Picture books.

First, using fuzzy (sound) name matching, 
I will search for author names in a dataset provided by the US Social Security Administration that 
contains names and genders of all individuals who have applied for Social Security Cards. 
Next, I'll aggregate the author dataset by including gender. 
Finally, I will use the new dataset to plot the gender distribution of children's picture books authors over time.

Sound it out!

Grey and Gray. Colour and Color.
Words like these have been the cause of many heated arguments between Brits and Americans. 
Accents (and jokes) aside, there are many words that are pronounced the same way but have different spellings.
While it is easy for us to realize their equivalence, basic programming commands will fail to equate such two strings.

More extreme than word spellings are names because people have more flexibility in choosing to spell a name in a certain way. 
To some extent, tradition sometimes governs the way a name is spelled, 
which limits the number of variations of any given English name. B
ut if we consider global names and their associated English spellings, you can only imagine how many ways they can be spelled out.

One way to tackle this challenge is to write a program that checks if two strings sound the same,
instead of checking for equivalence in spellings. I'll do that here using fuzzy name matching.


Authoring the authors

The New York Times puts out a weekly list of best-selling books from different genres, 
and which has been published since the 1930’s.
I’ll focus on Children’s Picture Books, and analyze the gender distribution of authors to see if there have been changes over time. 
I'll using data on the best selling authors from 2008 to 2017.
