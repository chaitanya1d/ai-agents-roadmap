STPS.md — AI Agents Roadmap Setup Steps

Step 1: Clone the Repository

Make sure Git is installed on your system.

Clone your GitHub repo:



bash

Copy

Edit

git clone https://github.com/chaitanya1d/ai-agents-roadmap.git

cd ai-agents-roadmap

Step 2: Install Prerequisites

You need the following installed before proceeding:



Python (3.10+ recommended)



Docker Desktop (running)



Ollama (for local model inference)



Check if they’re installed:



bash

Copy

Edit

python --version

docker --version

ollama --version

Step 3: (Optional) Create a Python Virtual Environment

If you want to run the app without Docker first or for local development:



bash

Copy

Edit

python -m venv venv

source venv/bin/activate     # Mac/Linux

venv\\Scripts\\activate        # Windows

pip install -r requirements.txt

Step 4: Build the Docker Image

From the root directory of the project (where Dockerfile exists):



bash

Copy

Edit

docker build -t ai-agents-roadmap-rag-app .

-t ai-agents-roadmap-rag-app → Tags the image with this name.



. → The current directory is the build context.



Step 5: Run the Docker Container

bash

Copy

Edit

docker run --rm -p 8000:8000 ai-agents-roadmap-rag-app

--rm → Automatically removes container when stopped.



-p 8000:8000 → Maps container’s port to local machine’s port.



ai-agents-roadmap-rag-app → Image name from Step 4.



Step 6: Verify Application

Open a browser and visit:



arduino

Copy

Edit

http://localhost:8000

You should see either:



A UI (if app has a frontend), or



A JSON/API response in your browser.



Step 7: Stop the Container

If running in foreground, press:



objectivec

Copy

Edit

CTRL + C

If running in background (detached mode), list containers:



bash

Copy

Edit

docker ps

Then stop it:



bash

Copy

Edit

docker stop <container\_id>



