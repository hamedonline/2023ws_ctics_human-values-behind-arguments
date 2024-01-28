## TODO
- handle labels made up by GPT that are not present in the actual labels (only a very small amount. So far I ignore them and only map the ones that are obviously the same as values given for prediction)
- find a good visualization. multi label confusion matrix for the amount of classes we have is not usefull...

## src
contains all scripts.

- get_gpt_values.ipynb generates the answers for a given prompt
- prepare_gpt_results.ipynb processes the .txt files (here some manual work that cannot really be automated is required)
- analyze_results.ipynb takes a look at the answers from chat gpt
- pipeline: Work in progress. Goal: provide methods that generate and process answers and store them in the correct directories etc.

## data
- ordered answers from gpt-3.5 for different prompts for each test question from the data set.

## prompts
our prompt looks like this:

Imagine you are a scientist. It is your job to analyze the human values behind a list of arguments provided to you.

An argument is given as a triple: (<premise>, <stance>, <justification>). The premise is the statement given to the person. The stance describes what the person thinks of the premise (either pro or contra). In the justification, the person explains the reasoning behind their stance.

For each argument, we want a list of human values that best explains the person's reasoning. Specifically, we use the values proposed by Kiesel et al. in their paper "Identifying the Human Values behind Arguments" from 2022. If you did not come across this paper, here are the values and a short definition:

- thought: it is good to have own ideas and interests
- action: it is good to determine one's own actions
- stimulation: it is good to experience excitement, novelty, and change
- hedonism: it is good to experience pleasure and sensual gratification
- achievement: it is good to be successful in accordance with social norms
- dominance: it is good to be in positions of control over others
- resources: it is good to have material possessions and social resources
- face: it is good to maintain one's public image
- personal: it is good to have a secure immediate environment
- society: it is good to have a secure and stable wider society
- tradition: it is good to maintain cultural, family, or religious traditions
- rules: it is good to comply with rules, laws, and formal obligations
- interpersonal: it is good to avoid upsetting or harming others
- humility: it is good to recognize one's own insignificance in the larger scheme of things
- caring: it is good to work for the welfare of one's group's members
- dependability: it is good to be a reliable and trustworthy member of one's group
- concern: it is good to strive for equality, justice, and protection for all people
- nature: it is good to preserve the natural environment
- tolerance: it is good to accept and try to understand those who are different from oneself
- objectivity: it is good to search for the truth and think in a rational and unbiased way

Here are a few examples:

**EXAMPLES**

Only return the labels, no explanation is required. Also dont write the triplet in front of the labels.
When receiving several triplets in this form:

(x1,y1,z1)

(x2,y2,z2)

(x3,y3,z3)

answer in this format:

(label_1.1, label_1.2)

(label_2.1, label_2.2)

(label_3.1, label_3.2)

DO NOT ADD ANYTHING ELSE TO YOUR ANSWER!

Here are the triplets:

\<triplet1\>

\<triplet2\>

...

\<triplet10\>

**Prompt 1** contains three examples:

- Input: ("We should end the use of economic sanctions", contra, "Economic sanctions provide security and ensure that citizens are treated fairly")
- Your response: (societal, concern)

- Input: ("We need a better migration policy", pro, "Discussing what happened in the past between Africa and Europe is useless. All slaves and their owners died a long time ago. You cannot blame the grandchildren")
- Your response: (concern)

- Input: ("Rapists should be tortured", contra, "Throughout India, many false rape cases are being registered these days. Torturing all of the accused persons causes torture to innocent persons too.")
- Your response: (societal, concern)

**Prompt 2** contains one example for each class:
- Input: ("We should cancel pride parades","in favor of","pride parades create a huge disturbance"),
- Your response: (rules, interpersonal)

- Input: ("We should ban the use of child actors","in favor of","child actors lose the sense of a proper childhood."),
- Your response: (Stimulation,Hedonism,personal)

- Input: ("We should adopt a multi-party system","against","multi-party systems slow down what gets done because we have too many different sides trying to come to an agreement"),
- Your response: (action,Achievement,dominance,objectivity)

- Input: ("We should ban missionary work","in favor of","if we ban missionary work, then a lot less people would be seeing propaganda."),
- Your response: (thought,caring,tolerance,objectivity)

- Input: ("We should subsidize student loans","against","it isn't the obligation of any tax payer to give money to help someone else get an education. that is a personal choice, and if they want to go to college they need to pay for it on their own."),
- Your response: (Achievement,resources,personal,dependability)

- Input: ("We should end mandatory retirement","in favor of","mandatory retirement is purely age discrimination"),
- Your response: (action,concern)

- Input: ("We should adopt atheism","against","Atheism is godless and fundamentally lacking in a coherent moral compass, therefore it should not be adopted."),
- Your response: (Face,societal,Tradition,dependability)

- Input: ("We should ban cosmetic surgery","in favor of","cosmetic surgery should be banned. god made you a certain way and these procedures are going against that. besides, it could be dangerous as joan rivers died from complications during surgery."),
- Your response: (personal,Tradition,Humility,nature)

**Prompt 3** doesn't contain any examples

For each prompt we tried setting **different roles** for the LLM: Psychologist and scientist.

## data / result generation
To obtain the results the following steps are performed:
- use a python package (gpt4free) to get answers for a given prompt from chatgpt
- add 10 triplets to the prompt (see above). FOr more than 10 triplets chat-gpt had problems answering the questions and gave more than $n_{triplets}$ answers and repeated the last answer many times. (We tried 100, 50 and 20 triplets in a single prompt)
- save the answer to each block of 10 questions in a txt file
- format the txt file (remove additional information, strip answer down to only the labels). For more details look into `prepare_gpt_results.ipynb`
- For some question blocks (~10%) the answer couldn't be used (sometimes chat-gpt broke, but most times it gave 9 or 11 labels instead of 10. Rerun these question blocks.
- When all question blocks are answered "correct" format them into a single file only containing the predicted labels.
