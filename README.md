# Tweet Generator

## Summary
Building a tweet generator with the modest goal of passing the Turing test using the [following tutorial](https://www.makeschool.com/academy/track/tweet-generator--data-structures---probability-with-python).

## What's in here?
**app.py**: flask app.
**cleanup.py**: to cleanup source file
**tokenizer.py**: turn source file into a list of tokens
**word_count.py**: to get a histogram from source file
**sample.py**: to generate a random sample of __ words from a source file

## How can I try this?
- Go to https://twt-generator.herokuapp.com -- it will automatically generate a 23 word sample from Edgar Allan Poe.
- Refresh for another sample
- If you want a longer sample, you can go to https://twt-generator.herokuapp.com/200 for a 200 word sample. (Note: This app is a WIP. It currently crashes above 1,000 words.)

## Milestones
- [x] **1. Rearranging words from terminal output.** To test this, clone the repo and run `python3 rearrange.py some random words`
- [x] **2. Random Dictionary Words** `python3 dictionarywords.py 10` where 10 is # of words to grab
- [x] **3. Analyze Word Frequency in Text** `python3 frequencyanalyzer.py` uncomment code as needed
- [x] **4. Stochastic Sampling**
- [x] **5. Flask Web App**
- [WIP] **6. Application Architecture**
- [ ] **7. Generating Sentences**
- [ ] **8. Linked List**
- [ ] **9. Hash Table**
- [ ] **10. Performance Analysis**
- [ ] **11. Markov Chains Revisited**
- [ ] **12. Creating a Corpus**
- [ ] **13. Parsing Text and Clean Up**
- [ ] **14. Tokenization**
- [ ] **15. Time to Tweet**

## App Architecture reflections (related to #6 above)
What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?
Are the names of files, modules, functions, and variables appropriate and accurate? Would a new programmer be able to understand the names without too much contextual knowledge?
What are the scopes of variables and are they appropriate for their use case? If there are global variables, why are they needed?
Are the functions small and clearly specified, with as few side effects as possible?
Are there functions that could be better organized in an Object-Oriented Programming style by defining them as methods of a class?
Can files be used as both modules and as scripts?
Do modules all depend on each other or can they be used independently?
