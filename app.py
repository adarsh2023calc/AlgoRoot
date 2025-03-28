from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from chroma_retrieval import retrieve_function
from automate_requests import FUNCTION_REGISTRY

app = FastAPI()

class ExecuteRequest(BaseModel):
    prompt: str

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>LLM + RAG Automation API</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
                h1 { color: #333; }
                p { font-size: 18px; }
                input, button { padding: 10px; margin: 10px; font-size: 16px; }
                button { background-color: #007BFF; color: white; border: none; cursor: pointer; }
                button:hover { background-color: #0056b3; }
            </style>
            <script>
                async function execute() {
                    const prompt = document.getElementById("prompt").value;
                    const response = await fetch("/execute", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ prompt: prompt })
                    });
                    const result = await response.json();
                    alert(JSON.stringify(result, null, 2));
                }
            </script>
        </head>
        <body>
            <h1>Welcome to the LLM + RAG Automation API 🚀</h1>
            <p>Use this API to dynamically retrieve and execute automation functions.</p>
            <input type="text" id="prompt" placeholder="Enter your prompt">
            <button onclick="execute()">Execute</button>
        </body>
    </html>
    """

@app.post("/execute")
def execute(request: ExecuteRequest):
    function_name = retrieve_function(request.prompt)
    
    if not function_name or function_name not in FUNCTION_REGISTRY:
        raise HTTPException(status_code=404, detail="Function not found")

    return {"result": FUNCTION_REGISTRY[function_name]()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
