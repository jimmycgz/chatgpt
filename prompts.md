# Example of Prompt for ChatGPT

### Initiate the Github Action workflow yml file
Make a pipeline of Github Actions to generate a video that a fake person speaks. Show me the full content of the pipeline yaml file. 
* Call ChatGPT API to generate a speaking script from a prompt
* Call Audio AI API to generate an mp3 audio speaking out that script generated from the above prompt
* Call Video AI API to generate a mp4 clip someone speaking out that script generated from the above prompt
* Save the audio/video files to a gcs storage

### As a Tech writer, I'm working on a Technical Design Document
I'm writing a TDD for a project, could you help to write some paragraphs for a gke overview? the goal is to let a beginner knows the concept, the advantage/benefit and why gke, may hight more advanced features that gke has comparing to any other similar products in the market?

looks great to me. could you introduce the components inside a GKE cluster and their features, functions, provide some links if the reader wants to refer for more details?

well those are all common things for both gke and open source kubernetes, could you revise to add more specific items GKE has? any references to GKE architecture and configuration?

### As a Cloud Infrastructure Engineer, Terraform GCP <=> AWS
can you convert below terraform code for GCP to AWS, make sure it works and don't use the outdated module

### As a Cloud Infrastructure Engineer, Terraform <=> Ansible

1. can you convert below terraform code to ansible playbook, make sure it's useful and don't use the outdated module
2. I can't fine  the gce module, can you use the latest module?
3. Is the module community.google.cloud.gcp_compute_instance available and valid?
4. I don't think so, I can't find community.google.cloud.gcp_compute_instance

### Act as a Linux Terminal
Contributed by: [Fatih Kadir Akın](https://github.com/f) Reference: https://www.engraved.blog/building-a-virtual-machine-inside/

I want you to act as a linux terminal. I will type commands and you will reply with what the terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. When I need to tell you something in English, I will do so by putting text inside curly brackets {like this}. My first command is pwd
```
pwd

{give me an example to call chatgpt api by curl}

{assume you have the valid 'API_SECRET_KEY' already and you already have internet connection to talk to any endpoint}

curl -X POST https://api.openai.com/v1/engines/davinci-codex/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer API_SECRET_KEY" \
-d '{
  "prompt": "Hello, my name is",
  "max_tokens": 5,
  "temperature": 0.5
}'
```

