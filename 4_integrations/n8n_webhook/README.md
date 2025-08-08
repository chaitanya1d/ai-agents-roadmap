# n8n Webhook Integration

1. Start your local API (e.g., simple_rag/app.py)
2. In n8n, create an HTTP Request node that POSTs to http://<your_ip>:5000/ask
3. Body JSON: {"question": "..."}

If n8n runs remotely, expose your app via ngrok or deploy to Railway/VPS first.
