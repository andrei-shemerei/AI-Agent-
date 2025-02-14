# 🚀 AI Agent with Multi-Tool Functionality  

## 📌 Overview  
This project implements an intelligent agent capable of utilizing **three different tools** to assist users:  

1. **📊 DataFrame Querying** – Retrieve insights from structured data.  
2. **📄 PDF Document Analysis** – Extract and answer questions based on the content of PDF files.  
3. **📝 Note-Taking** – Generate and save notes with valuable information.  
4. **🤖 Local & Cloud-Based LLM Support** – Use Gemini API or a locally hosted model for AI-powered responses.  

## 🔹 Features  
✅ Query structured data from CSV files.  
✅ Extract insights from PDF documents.  
✅ Store important information as personal notes.  
✅ Justify answers using your own data sources.  
✅ Choose between **Google Gemini API** or a **locally deployed LLM**.  

## 📂 Using Your Own Data  
To ensure accurate responses based on your **own data**, make sure to **specify the correct file path** when interacting with the agent.  

## 🛠 Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repo/ai-agent.git  
   cd ai-agent  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Set up your API keys for either Gemini or a locally hosted model.  

## 🔹 Setting Up a Local LLM with vLLM  
For local inference, we recommend using **Llama 3.1 70B Instruct** via vLLM. To install and deploy:  
   ```bash  
   pip install vllm  
   vllm-launch --model meta-llama/llama-3.1-70b-instruct  
   ```  

## 🚀 Usage  
Run the agent with:  
   ```bash  
   python main.py  
   ```

## 💡 Tip: Make sure your data files (CSV/PDF) are placed in the correct directory for seamless access!  

## 📊 Local LLM Inference Performance Metrics  
### 🔥 Serving Benchmark Results  
- **Successful requests:** 100  
- **Benchmark duration (s):** 59.27  
- **Total input tokens:** 54,995  
- **Total generated tokens:** 15,000  
- **Request throughput (req/s):** 1.69  
- **Input token throughput (tok/s):** 927.79  
- **Output token throughput (tok/s):** 253.06  

### ⏳ Time to First Token (TTFT)  
- **Mean TTFT (ms):** 25,927.37  
- **Median TTFT (ms):** 18,401.39  
- **P99 TTFT (ms):** 56,539.46  

### ⏱️ Time per Output Token (excluding first token)  
- **Mean TPOT (ms):** 113.84  
- **Median TPOT (ms):** 105.77  
- **P99 TPOT (ms):** 240.31  

### 📉 Inter-Token Latency (ITL)  
- **Mean ITL (ms):** 286.20  
- **Median ITL (ms):** 52.31  
- **P99 ITL (ms):** 7,261.91  


