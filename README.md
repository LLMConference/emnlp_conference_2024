### SimulateBench: How Far Are We from Believable AI? A Benchamrk for Evaluating the Believability of Human Behavior Simulation

---



In recent years, AI has demonstrated remarkable capabilities in simulating human behaviors, particularly those implemented with large language models (LLMs). 
However, due to the lack of systematic evaluation of LLMs' simulations, the believability of LLMs among humans remains ambiguous, i.e., it is unclear which behaviors of LLMs are convincingly human-like and which need further improvements. In this work, we design SimulateBench to evaluate the believability of LLMs when simulating human behaviors. In specific, we evaluate the believability of LLMs based on two critical dimensions: 1) consistency: the extent to which LLMs can behave consistently with the given information of a human to simulate; and
2) robustness: the ability of LLMs' simulated behaviors to remain robust when faced with perturbations. SimulateBench includes 65 character profiles and a total of 8,400 questions to examine LLMs' simulated behaviors. Based on SimulateBench, we evaluate the performances of 10 widely used LLMs when simulating characters. The experimental results reveal that current LLMs struggle to align their behaviors with assigned characters and are vulnerable to perturbations in certain factors.



<img src="https://raw.githubusercontent.com/GAIR-NLP/SimulateBench/master/introduction.png" alt="test" style="zoom:50%;" />

###  Table of content

---

* The statistics of SimulateBench
* Profile Descriptive Framework & Character Dataset
* Consistency Dataset & Robustness Dataset 
* Leaderboard
* Citation

### The statistics of SimulateBench

---

| Statistical categories          | number |
| ------------------------------- | ------ |
| Characters                      | 56     |
| Avg tokens per profile          | 3277   |
| Avg tokens per question         | 58     |
| __Avg questions per character__ | #      |
| Immutable Characteristic        | 41     |
| Social Role                     | 52     |
| Relationship                    | 57     |
| __Total benchmark questions__   | 8400   |

### Profile Descriptive Framework & Character Dataset 

---

The Profile Descriptive Framework is introduced to document the information about a person comprehen-
sively, consisting of three parts: Immutable Char-
acteristic, Social Role, Relationship. 

We selected characters from TV dramas of popular genres: The Simpsons (Animated), Friends (Comedy), Breaking Bad (Crime), and The Rings of Power(Science fiction). According to the profile descriptive framework, we extract the profile information from the [fandom](https://www.fandom.com/).

The profile is recorded in the json format for easy to use. You can find the profile of a character in the folder of "/db/profile/". The Social Role, Relationship information are stored in one json file.

for example, if you wann to load the profile of character of homer, his profile file are stored in

Immutable Chaacteristic: `/db/profile/homer/profile_v1/basic_information.json`

Social Role, Relationship: `db/profile/homer/profile_v1/roles.json`

### Consistency Dataset & Robustness Dataset

---

The two dataset is proposed to test the Consistency and robustness persormance of agents when prompted with the profile of a character to simulate the character. The two dataset is composed of single-
choice questions and its gold answer. According to the profile descriptive framework, there are three kinds of questions related to Immutable Characteristics, Social Roles, and Relationships. For a character, you can find the dataset in the folder of "/db/benchmark_only_QA".

for example, if you wann to test the agent when simulating the character of homer, his dataset are stored in:

Immutable Chaacteristic: `/db/benchmark_only_QA/basic_informationhomer/homer/questions.json`

Social Role: `/db/benchmark_only_QA/role_non_relation/homer/questions.json`

Relationship: `/db/benchmark_only_QA/role_relation/homer/questions.json`

>To test the LLMs' consistency ability, we will ask the LLM to first simulate the character. Then, we will ask the LLM to finsh the corresponding multi-choice question in the Consistency Dataset. The accuracy score will be used as the measure of the consistency ability.

>The Robustness Dataset is these datasets whose names are of the format of 'homer_{varients}'. To test LLMs' robustness ability, the LLMs is tested by compare their performance on the Consistency dataset and Robustness dataset. For example, if we want to test the LLMs' robustness ability when faced with age perturbations, we will first change the field of birthday year of homer in the profile, namely from 1956 to 1985. We then ask the LLM to simulate homer(`/db/profile/homer/`) and homer_1985(`/db/profile/homer_1985/`) by prompting the two profile to the agent respectively. Then, we will ask the LLM to finish the test in the `/db/benchmark_only_QA/{question_type}/homer/questions.json` and `/db/benchmark_only_QA/{question_type}/homer_1985/questions.json` respectively. Then, we can compare the two score on the two dataset to analyse the LLMs' robustness ability.









