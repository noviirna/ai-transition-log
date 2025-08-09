# [Google Machine Learning & AI](https://cloud.google.com/learn/training/machinelearning-ai)

## 1. [Introduction to Gen AI](https://www.cloudskillsboost.google/paths/118?utm_source=cgc&utm_medium=website&utm_campaign=evergreen)
### What is Gen AI / Generative AI?
Gen AI / Generative AI: AI tech that can produce various content. GenAI is a type of Artificial Intelligence that creates new content based on what it has learned from existing content. A generative language model takes text as input and can output more text, an image, audio, or decisions.  For example, under the output text, question and answering is generated, and under output image a video is generated. Generative language models are pattern-matching systems. They learn about patterns based on the data you provide.
AI: Theory and methods to build machine that think and act like human
ML: Subfield of AI, a system that train a model from input data. ML give computer to learn without programming

### ML learning type / methods:
1. supervised learning
- use labeled data with tag, name, type, number
- model learn from past example to predict future values
- input -> model -> output compare with prediction -> if error happens, then the model updated to be able to predict things better

2. unsupervised learning 
- use data with no tag
- all about discovery, look at the raw data and seeing if it naturally falls into group
- input -> processed by model -> generated example

3. reinforcement learning

4. deep learning
- use artificial neural network, allowing to process more complex pattern
- it is like copying how brain works with neural network
- neural network can use both labeled and unlabeled data
- it is also called semi-supervised learning, it is combining two methods
  - supervised learning with unlabeled data for learning the task
  - unsupervised learning with unlabeled data is to generate new example
- Gen AI is subset of deep learning
- LLM is also a subset of deep learning
- deep learning model consist of 2 types: generative and discriminative
  - discriminative: trained on dataset of labeled data points. it can be used to predict label for new data point (just like supervised learning). for example it is distinguishing data inputted to the model (like classifying something). how it works: input (data + label) -> predictive ml model learn data & label connection -> output -> label. typically generate number, discrete, class, probability. 
  - generative: generate new data instances based of learned probability of existing data. for example (generating new data model by learned data previously, like generating images of something). how it works input (unstructured content) -> learn pattern -> output -> new content. typically generate natural language, image, audio, etc.
  - the math model is like this y = f(x), where y is model output, f is model, x is input data. if y is a number it is discriminative AI, if it is language then it is gen AI.
  - Gen AI utilize transformers. It is like a model which has encoder (encode input & pass it to decoder) & decoder (learn how to decode for relevant tasks). Sometimes there is issue with the transformer so that the output is 'delulu' which nonsensical, or factually wrong, or gramatically wrong. it called 'hallucination'. it can happen due to: dirty data, not enough context & constraints.

### Prompt
prompt:  is a short piece of text that is given to a large language model, or LLM

prompt design: process of creating a prompt that will generate the desired output from an LLM

Model for input text by prompt:
- text to text: example translating languages
- text to image: example create image from description
- text to video: example:google veo
- text to 3d: example creating 3d model from description
- text to task: perform a defined task or action based on text input (like checking CV, finding from websites, etc)

### Foundation Model
foundation model:  large AI model pre-trained on a vast quantity of data "designed to be adapted” (or fine-tuned) to a wide range of downstream tasks, such as sentiment analysis, image captioning, and object recognition. for example: Vertex AI.
language for foundation model: chat, text, code

### Gen AI usage
- text: content, sales, support / customer service, general writing, note taking
- code: code generation, code documentation, text to sql, app builder
- image: design, generation, social, advertising
- speech: voice synthesis
- video: video editing, video generation
- 3d: create models and sceneries
- other: gaming, rpa, music, audio, biology and chemistry

### Google Cloud Product
- Vertex AI studio -> create Gen AI Model 
- Vertex AI -> create AI agent using prompt
- Gemini -> multi model AI

### Glossary
- AI: artificial intelligence
- ML: machine learning
- LLM: large language model

### Additional Resources
- /resources/G-GENAI-I-m1-l2-en-file-2.en.pdf
----

## 2. [Introduction to LLM](https://www.cloudskillsboost.google/paths/118/course_templates/539)
### LLM
LLM: a subset of deep learning. large general purpose language models that can be pre-trained and fine-tuned for specific purposes

Chain of thought reasoning: models tend to be better at getting right answer when the first output explains the reason for the answer.

3 Major features LLM
- Large -> refer to number of: training dataset, parameters
- General Purpose -> model can solve common problems by commonality human languages and resource constraints
- Pretrained and fine-tuned -> pretrain a LLM for a general purpose with a large dataset and then fine tune it for specific purpose with smaller dataset

Use cases & predominance than other model:
- Single models can solve multiple tasks
- Require minimal training data when tailored
- Decent performance with minimal training data
- Can be used for few-shot (model trained with minimal data) or even zero-shot scenario (model that can recognize things that haven't been learned)
- performance is improved with more training data & parameter

LLM is based on transformer models.

Transformer model, has:
- encoder (encode the input so it can be processed by decoder and pass it to decoder)
- decoder (process it so the model can give output)

It allows system to perform tasks without having to code it explicitly.

Predominance LLM vs traditional ML :
- No ML expertise
- No training example
- No need to train a mode
- Only need to know about prompt design -> design a prompt that clear concise informative. important part of NLP.

3 Model Type of LLM:
- Generic: predict the next word based on language on the training data. like how to create a coherent sentences. like an autocomplete. Task specific model is more reliable than generic model.
- Instruction-tuned: trained to predict based on the instruction in the input. example prompt: summarize the documents into a presentation notes
- Dialogue: trained to have a dialogue by predicting next response. for example: chatbot that is tuned to answer FAQ. works better with natural question-like phrasings.

### NLP & Prompting
QA is a subfield of NLP that deal with task of automatically answering questions in natural language. It is trained with large amount of text and code, can answer wide range of questions. You need a domain knowledge (the dictionary) to develop QA models.

There are also generative QA, which no need domain knowledge to develop it, it only needs the context and generate the answers along the context.

Prompt Design :
- creating tailored prompt for specific task the system need to  perform
- for wide general usage

Prompt Engineering :
- creating tailored prompt to improve performance
- necessary for system that need high accuracy or performance

### Tuning
Tuning: adapting the model to new use case by training model on new data. to customize the model's response.

Type of tuning:
- Fine-tuning: re-train model and tuning every weight in the llm. require a training job and hosting your own model. it is expensive.
- PETM: turning LLM on your own custom data without duplicating the model. more efficient than fine-tuning.
- Prompt tuning: adjust the prompt, the easiest PETM.

### Google's product related:
- Vertex AI studio to create & deploy, gen AI model, with various tools.
- Vertex AI (no code AI model builder)

### Glossary
- LLM: Large Language Model
- NLP: Natural Language Processing
- QA: Question Answering
- PETM: parameter efficient tuning method

### Additional Resource
- G-LLM-I-m0-l2-en-file-2.en.pdf

## 3. [Introduction to Responsible AI](https://www.cloudskillsboost.google/paths/118/course_templates/554)
Developing responsible AI requires understanding of:
- possible issues
- limitations
- unintended conseuences

AI may replicate existing issues in society or even amplify it.

Each organization can define their own principle of responsible AI. Most of them cover these principle:
- transparency
- fairness
- accountability
- privacy

Google's values on responsible AI:
- built for everyone
- accountable and safe
- respect privacy
- driven by scientific excellence

Machine is not the decision maker in AI. People involved in AI development is. They collect data, deploy, and apply the system.

Responsible AI development & usage is important because AI can affect society, daily lives, so it is needs to have ethics / code of conduct. Without it, it can cause ethical issues or unintended outcomes. The ethics can guide AI design to be more beneficial to people's live.

3 Google principles on Responsible AI in practices
- AI that grounded in bold innovation to empower people & society
- Responsible development and deployment
- Collaborative progress

### Glossary
- 

### Additional Resource
- 

