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