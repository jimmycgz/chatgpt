# ChatGPT DEMOs

## DEMO #1: AIGC CICD Pipeline

### Feature List
 
This is a GitHub Action workflow that test AIGC, the pipeline has tested below steps:
* Call OpenAI API to generate a speaking script per a prompt request from json input
* Configure Workload Identity Federation to let Github Actions access GCP via OAUTH temporary token
* Generate speaking audio via Google text-to-speech API
* Call Studio.d-id API to generate a talk (mp3) speaking the above script
* Get the url of the saved mp3 file
* Call Video AI API to let the above person speak out the above script

### How to Use
Refer the details at [README.md](aigc-pipelie/README.md)