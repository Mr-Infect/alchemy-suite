# ⚡ ALCHEMY AGENT
### Autonomous AI-Powered Security Research Engine

> Not a scanner. Not a script.  
> This is an **agentic offensive system** designed to think, adapt, and validate vulnerabilities like a human researcher.

---

## 🧠 Overview

**Alchemy Agent** is an AI-driven security crawler that combines:

- Browser automation (Playwright)
- Multi-user session simulation
- LLM-based reasoning (Ollama / Gemma)
- Adaptive attack execution
- Multi-step attack chaining
- Intelligent vulnerability scoring

👉 Built to move beyond traditional scanners and towards **autonomous vulnerability discovery**

---

## 🔥 Core Capabilities

### 🕷️ Intelligent Crawling
- SPA-aware crawling (Playwright)
- Runtime API interception
- Endpoint graph discovery

### 🔐 Session-Aware Attacks
- Multi-user simulation (Admin vs User)
- Cookie/session reuse
- Auth vs unauth comparisons

### 🧠 LLM Attack Brain
- Endpoint classification
- Attack strategy generation
- Payload suggestion
- Context-aware reasoning

### ⚔️ Adaptive Attack Engine
- Dynamic method selection (GET/POST/etc.)
- Payload mutation
- Vulnerability-type targeting

### 🔗 Attack Chaining
- Multi-step exploitation logic
- Follow-up actions based on response
- Validation-driven workflow

### 📊 Smart Scoring Engine
- Signal-based prioritization
- Noise filtering
- High-confidence vulnerability detection

---

## 🏗️ Architecture

```

alchemy_agent/
│
├── core/
│   ├── crawler/
│   ├── session_manager/
│   ├── request_engine/
│
├── brain/
│   ├── llm_router.py
│   ├── prompt_engine.py
│   ├── chain_engine.py
│
├── modules/
│   ├── idor/
│
├── recon/
├── reporting/
├── utils/
├── config/
│
├── main.py
├── runner.py

````

---

## ⚙️ System Requirements

### 💻 Minimum
- RAM: 16GB
- CPU: 4+ cores
- Storage: 20GB free

### ⚡ Recommended
- RAM: 32GB+
- CPU: 8 cores+
- GPU (optional): NVIDIA (for faster inference)

### 🐧 OS
- Kali Linux / Ubuntu 22.04+ (recommended)
- WSL2 (supported)

---

## 🧰 Dependencies

### Core Stack
- Python 3.10+
- Docker
- Playwright
- Ollama (local LLM runtime)

---

## 🚀 Installation

### 1. Clone Repo

```bash
git clone https://github.com/YOUR_USERNAME/alchemy-agent.git
cd alchemy-agent
````

---

### 2. Setup Virtual Environment

```bash
python3 -m venv alchemy_env
source alchemy_env/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install playwright requests httpx beautifulsoup4 lxml rich tqdm networkx pydantic fastapi uvicorn
```

---

### 4. Install Playwright Browsers

```bash
playwright install
```

---

### 5. Install Ollama (LLM Runtime)

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Start server:

```bash
ollama serve
```

---

### 6. Download Models

```bash
ollama pull gemma:7b
ollama pull codellama:7b
ollama pull phi
```

---

### 7. Run Test Target (Juice Shop)

```bash
docker run -d -p 3000:3000 bkimminich/juice-shop
```

---

## ▶️ Running the Agent

```bash
python main.py
```

---

## 🧪 Expected Workflow

```
[+] Creating multiple sessions
[+] Crawling target
[+] Discovering API endpoints
[+] Running Adaptive Attack Engine
[+] LLM-driven analysis
[!!!] VALIDATED ISSUE → endpoint
```

---

## 🎯 Example Output

```
[!!!] Sensitive Data Exposure (Score: 70)
Target URL: /rest/admin/application-configuration

[!!!] IDOR / Access Control (Score: 65)
Target URL: /rest/user/whoami?fields=id,email
```

---

## 🧠 How It Works (Simplified)

1. Crawl application (Playwright)
2. Capture runtime API traffic
3. Generate sessions (multi-user)
4. LLM analyzes endpoints
5. Attack engine executes strategy
6. Compare responses (admin vs user)
7. Score + validate findings
8. Attempt attack chaining
9. Generate report

---

## ⚠️ Ethical Use

This tool is intended for:

* Bug bounty research
* Security auditing
* Controlled lab environments

❌ Do NOT use against unauthorized targets

---

## 🔥 Roadmap

* [ ] Autonomous loop engine (self-improving agent)
* [ ] Graph-based attack prioritization
* [ ] Advanced payload generation
* [ ] Cloud scanning integration
* [ ] Distributed scanning nodes
* [ ] CVE discovery automation

---

## 🧠 Philosophy

Most tools:

> scan endpoints

Alchemy Agent:

> **understands, decides, attacks, validates**

---

## 👨‍💻 Author

Built by a security engineer pushing toward:

> Autonomous Offensive AI Systems

---

## ⭐ Contribute / Support

If you find this useful:

* Star ⭐ the repo
* Fork 🍴 and improve
* Share with researchers

---

## ⚡ Final Note

This is not the final form.

This is the **foundation of an autonomous security researcher**.

```
