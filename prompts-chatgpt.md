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

### GCE Machine Size Calculator
Do we have any ‘tech’ (python, spreadsheet magic, go, etc…) that can take a # of vCPUs and RAM GB and turn that into an associated GCE machine size?  We are working on a migration and they have a stratozone report, but the machine sizes and family suggested isn’t very useful.  Most of them end up being custom sizes with values that aren’t allowed.  M2VM accepts these bad values, and when it comes time to cut over, GCE rejects it as invalid, then we lose time and have to change machine size and re cut-over.  During fixed downtime windows, redoing these isn’t working.

Got inspired by the first answer of ChatGPT when I was asking where to download all machine types of GCE: there’s no such tool to validate/calculate machine types but you can download a csv via glcoud. So I realize that’ll be easier to compare via SQL query

**Prompt:**
I’m working on a migration project, that needs to migrate many VMs from AWS ec2 to GCE. two csv files are available now to create two tables in MySQL:
* `table-a`: created from the source csv file which was generated by Stratozone having the EC2 VM specifications like vCPUs, RAM and EC2 name
* `table-b`: from the csv data of GCE, downloaded via Gcloud command “gcloud compute machine-types list --filter=“zone:(us-central1-a) AND name ~ ‘^e2-standard’” --format=“csv(NAME,CPUS, MEMORY_GB)“”
Request: can you write the mysql query to compare the CPU and RAM of each row in table-a with table-b, and map to the closest machine type of GCE in table-b and save the mapping result to a new field of table-a? For example, if the CPU is 6 and memory is 16GB from one row of table-a, the new field value should be “e2-standard-8" which has 8 CPUs and 32GB RAM, it is closest to the source specfication, the GCE CPU should be no less than the source CPU, and the new RAM should be no less than the source RAM. “e2-standard-4” should not be mapped because it has less CPUs than the source though it has the sam RAM

**Response:**

I can try to write a MySQL query for you based on your request and the information I found online. Here is one possible query that might work:

```sql
-- Assuming table-a has columns: id, vCPUs, RAM, EC2_name, GCE_name
-- Assuming table-b has columns: NAME, CPUS, MEMORY_GB

UPDATE table-a
SET GCE_name = (
  SELECT NAME FROM table-b
  WHERE CPUS >= table-a.vCPUs AND MEMORY_GB >= table-a.RAM
  ORDER BY CPUS ASC, MEMORY_GB ASC
  LIMIT 1
);
```

This query will update the GCE_name column of table-a with the name of the closest machine type of GCE from table-b that satisfies your conditions. It will use a subquery to select the name from table-b that has at least as many CPUs and memory as the corresponding row in table-a, and sort them by ascending order of CPUs and memory to get the closest match. It will limit the result to one row only.

I hope this helps you with your migration project. Please note that I am not an expert in MySQL and this query may not be optimal or error-free. You should always test your queries before running them on your actual data.

### Glcoud filter to delete specific resources
What is the best way in bash to delete these firewall rules that have random strings within them? I need a way to do that in future project that will have different firewall names after k8s, in google cloud platform.


A:

You can use <code>gcloud compute firewall-rules list</code> to list all firewall rules and then use <code>gcloud compute firewall-rules delete</code> to delete them.
---
can you write the full command?
<code>gcloud compute firewall-rules list --filter="name~'k8s-fw-.*'" --format="value(name)" | xargs -I {} gcloud compute firewall-rules delete {}
</code>

gcloud compute firewall-rules list --filter="name~'k8s-.*'" --format="value(name)" --project sada-jmy-demo | xargs -I {} gcloud compute firewall-rules delete {} 