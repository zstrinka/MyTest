# Question 1:

I have provided mainFile.py as well as Question1.py to answer this question, as well as a sample file Question1Text.txt. The resulting code can read in a text file and outputs the total number of words, number of unique words, and number of sentences in the file. In addition, there is a function to print out to the console the unique words in descending order of frequency.

For this question, I learned there are already many tools available to handle word and sentence counts. In particular, how to handle punctuation is an important question I mostly overlooked. I did provide the ability to ignore punctuation in the word count functions, but it has limited sophistication by comparison to what other people have done.

If I were to do this in a work-setting, I would use the resources mentioned in this StackOverflow question: http://stackoverflow.com/questions/4576077/python-split-text-on-sentences

# Question 2:

I did some initial work to answer this question, but did not test the code, and therefore I expect there are some issues. 

My source code was inspired by the answers here: http://stackoverflow.com/questions/16707780/count-how-many-rows-have-the-same-value
and here: http://stackoverflow.com/questions/5446778/sql-select-from-one-table-matching-criteria-in-another
and here: http://stackoverflow.com/questions/1503959/how-to-count-occurrences-of-a-column-value-efficiently-in-sql

SELECT
    A.Name
FROM
    Salesperson A
where
    A.ID in (
        SELECT B.salesperson_id COUNT(B.salesperson_id) as cnt FROM Orders B WHERE cnt>1
)

# Question 3:

What questions would you ask me about my goals and methodology?
I would want to know if the providers always saw the same version of the form. I would also want to know how many providers these results represented. If the providers saw different forms each time they visited and there were a lot of repeat visitors, I would want to know what the timeseries for each providor (visit, chose to submit a quote) looks like.

What's your interpretation of these results?
Assuming there were 3000 distinct providers for the purpose of my analysis:

I would use a power analysis calculation (like the one provided here: http://clincalc.com/stats/samplesize.aspx) to compare the largest (variation 3) and smallest (variation 2) quote rates. Doing that analysis via the calculator, the required sample size for each subgroup is given as 275 participants for alpha = 5% and power = .8. With more time, I would do all the comparisons. 

What conclusions would you draw?
I would be hesitant to make any long term predictions since (by my assumption) we can assume most providers knew how to fill out the baseline form, and so I would want to test if future visits to a revised form continued to have results similar to those found in the first experiment.

If these were all completely new providers (i.e., they had never served on the website before), based on the above analysis I would at least conclude that variation 3 is better than variation 2.

Do you have any thoughts on the experimental design?
Being able to look at the timeseries data for a single provider visiting the site multiple times would hopefully provide critical information about how the users learn the different interfaces. 
