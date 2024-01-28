## TODO

## src
contains generic script to run any LLM model on HuggingFace service.

- get_LLaMa_2_values.ipynb generates the answers for a given prompt

## data
- ordered answers from LLaMa-2 for different prompts for each test question from the data set.

## prompts
our prompt looks like this:

[INST] <<SYS>>
{{ Imagine you are a psychologist. It is your job to analyze the human values behind a list of arguments provided to you.

An argument is given as a triple: ( , , ). The premise is the statement given to the person. The stance describes what the person thinks of the premise (either pro or contra). In the justification, the person explains the reasoning behind their stance.

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

- Input: ("We should end the use of economic sanctions", contra, "Economic sanctions provide security and ensure that citizens are treated fairly")
- Your response: (societal, concern)

- Input: ("We need a better migration policy", pro, "Discussing what happened in the past between Africa and Europe is useless. All slaves and their owners died a long time ago. You cannot blame the grandchildren")
- Your response: (concern)

- Input: ("Rapists should be tortured", contra, "Throughout India, many false rape cases are being registered these days. Torturing all of the accused persons causes torture to innocent persons too.")
- Your response: (societal, concern)

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

Here are the triplets:}}
<</SYS>>

{{user_prompt}} [/INST]

## login huggingface:
User Access Tokens = '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'
