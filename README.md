# Profinaty
Many tweets contain certain profane words which are committed to age restrictions. These tweets might violate policies of social media. So to avoid this .there is a need to replace these profane words with censored letters i.e., 'x' or '*'. Also certain algorithms neglect specific exceptions in those words given the data to the algortihms. Those excpetions are also taken care of. For eg: Deleting a letter or replacing it with another character to avoid AI to detect such words. 
The tweets data is taken from Kaggle which includes over 24K+ tweets which contain non-profane/offensive and profane tweets. 
The profane words are taken from various online sources and put it together in a single .json file 
An csv file is generated after running main.py which contains degree of profanity and censored tweets.
