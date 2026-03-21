<h1 align="center">🚀 AI-Powered Self-Healing Kubernetes System</h1>

<p align="center">
A production-style DevOps project that demonstrates automated monitoring, failure detection, and self-healing in a Kubernetes environment using Prometheus and custom controllers.
</p>

<hr/>

<h2 style="color:#4CAF50;">📌 Project Overview</h2>

<p>
This project simulates a real-world cloud-native system where microservices are deployed on Kubernetes and monitored continuously.  
The system is designed to detect failures, analyze metrics, and automatically recover services — moving towards a fully AI-driven self-healing infrastructure.
</p>

---

<h2 style="color:#4CAF50;">🏗️ Architecture</h2>

<pre>
                +----------------------+
                |    Load Generator    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |     API Service      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |        Redis         |
                +----------------------+

                           |
                           v

                +----------------------+
                |     Prometheus       |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |       Grafana        |
                +----------------------+

                           |
                           v

                +----------------------+
                | Self-Healing Controller |
                +----------------------+

                           |
                           v

                +----------------------+
                |   Kubernetes Cluster |
                +----------------------+
</pre>

---

<h2 style="color:#4CAF50;">⚙️ Tech Stack</h2>

<ul>
  <li><b>Kubernetes (Kind)</b> – Container orchestration</li>
  <li><b>Docker</b> – Containerization</li>
  <li><b>Prometheus</b> – Metrics collection</li>
  <li><b>Grafana</b> – Visualization</li>
  <li><b>Python</b> – API + Controller logic</li>
  <li><b>Flask</b> – Microservice backend</li>
</ul>

---

<h2 style="color:#4CAF50;">✅ Completed Features (Phase 1)</h2>

<ul>
  <li>✔ Kubernetes cluster setup using Kind</li>
  <li>✔ Microservices deployment (API, Redis, Load Generator)</li>
  <li>✔ Docker containerization</li>
  <li>✔ Prometheus monitoring integration</li>
  <li>✔ Grafana dashboards for real-time metrics</li>
  <li>✔ Metrics exposure via API (<code>/metrics</code>)</li>
  <li>✔ Custom controller to read cluster metrics</li>
</ul>

---

<h2 style="color:#FFC107;">🟡 In Progress (Phase 2)</h2>

<ul>
  <li>🔄 Automated failure detection logic</li>
  <li>🔄 Pod restart automation based on metrics</li>
  <li>🔄 Intelligent scaling decisions</li>
</ul>

---

<h2 style="color:#F44336;">🚀 Upcoming Features (Phase 3)</h2>

<ul>
  <li>🧠 AI-based anomaly detection</li>
  <li>📊 Predictive scaling using ML models</li>
  <li>⚙️ CI/CD pipeline (GitHub Actions)</li>
  <li>☁️ Terraform-based cloud deployment (AWS)</li>
  <li>📈 Advanced observability (alerts + dashboards)</li>
</ul>

---

<h2 style="color:#4CAF50;">📂 Project Structure</h2>

<pre>
ai-self-healing-k8s/
│
├── kubernetes/           # Deployment & service YAMLs
├── microservices/        # API, Redis, Load Generator
├── monitoring/           # Prometheus & Grafana configs
├── self-healing-controller/  # Custom controller logic
├── ai-engine/            # (Upcoming ML logic)
├── cicd/                 # (Upcoming CI/CD pipelines)
├── terraform/            # (Upcoming infra setup)
└── docs/                 # Documentation
</pre>

---

<h2 style="color:#4CAF50;">📊 How It Works</h2>

<ol>
  <li>Microservices generate traffic and data</li>
  <li>Prometheus collects real-time metrics</li>
  <li>Grafana visualizes system performance</li>
  <li>Controller continuously reads metrics</li>
  <li>Future: AI detects anomalies & triggers recovery</li>
</ol>

---

<h2 style="color:#4CAF50;">🚀 Getting Started</h2>

<h3>1️⃣ Clone the Repository</h3>

<pre>
git clone https://github.com/Darshan7887/AI-Self-Healing-K8S.git
cd AI-Self-Healing-K8S
</pre>

<h3>2️⃣ Deploy to Kubernetes</h3>

<pre>
kubectl apply -f kubernetes/ --recursive
</pre>

<h3>3️⃣ Access API</h3>

<pre>
kubectl port-forward &lt;api-pod&gt; 5000:5000
</pre>

Open: <b>http://localhost:5000</b>

---

<h2 style="color:#4CAF50;">💡 Key Learnings</h2>

<ul>
  <li>Real-world Kubernetes debugging</li>
  <li>Monitoring & observability setup</li>
  <li>Container lifecycle management</li>
  <li>Designing self-healing systems</li>
</ul>

---

<h2 style="color:#4CAF50;">🌟 Future Vision</h2>

<p>
This project aims to evolve into a fully autonomous cloud system where infrastructure can:
</p>

<ul>
  <li>Detect failures automatically</li>
  <li>Predict issues before they occur</li>
  <li>Self-heal without human intervention</li>
</ul>

---

<h2 style="color:#4CAF50;">🤝 Contributing</h2>

<p>Contributions are welcome! Feel free to fork and improve the project.</p>

---

<h2 align="center">🔥 Built for DevOps | SRE | Cloud Engineering 🚀</h2>
