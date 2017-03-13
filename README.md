Question 1:

I have provided mainFile.py as well as Question1.py to answer this question, as well as a sample file Question1Text.txt. The resulting code can read in a text file and outputs the total number of words, number of unique words, and number of sentences in the file. In addition, there is a function to print out to the console the unique words in descending order of frequency.

For this question, I learned there are already many tools available to handle word and sentence counts. In particular, how to handle punctuation is an important question I mostly overlooked. I did provide the ability to ignore punctuation in the word count functions, but it has limited sophistication by comparison to what other people have done.

If I were to do this in a work-setting, I would use the resources mentioned in this StackOverflow question: http://stackoverflow.com/questions/4576077/python-split-text-on-sentences

Question 2:

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

Question 3:

