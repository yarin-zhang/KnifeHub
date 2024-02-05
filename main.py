import os
import json
import subprocess
from fastapi import FastAPI
from typing import Optional

app = FastAPI()


# 在 FastAPI 应用启动时，读取脚本目录并安装必要的依赖
async def startup_event():
    script_dirs = [d for d in os.listdir("./data") if os.path.isdir(os.path.join("./data", d))]

    # 为每个脚本目录安装必要的依赖
    for script_dir in script_dirs:
        subprocess.run(["pip", "install", "-r", f"./data/{script_dir}/requirements.txt"])

app.add_event_handler("startup", startup_event)

# 添加 API 端点，让用户可以通过 API 请求来列出所有脚本
@app.get("/scripts")
async def list_scripts_endpoint():
    # 读取 ./data 目录下的所有目录
    script_dirs = [d for d in os.listdir("./data") if os.path.isdir(os.path.join("./data", d))]
    return {"scripts": script_dirs}


# 添加 API 端点，让用户可以通过 API 请求来运行脚本
@app.post("/run/{script_name}")
async def run_script_endpoint(script_name: str, script_input: Optional[str] = None):
    # 运行脚本
    command = ["python", f"./data/{script_name}/script.py"]
    if script_input:
        command.append(script_input)
    result = subprocess.run(command, capture_output=True, text=True)
    
    # 返回结果
    return {"output": result.stdout}
