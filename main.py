import json
import subprocess
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# 在 FastAPI 应用启动时，读取配置文件并安装必要的依赖
async def startup_event():
    # 读取配置文件
    with open("./data/config.json") as f:
        config = json.load(f)

    # 安装必要的依赖
    for script in config["scripts"]:
        if script["install_on_startup"]:
            subprocess.run(["pip", "install", "-r", f"./data/{script['name']}/requirements.txt"])

app.add_event_handler("startup", startup_event)

# 添加 API 端点，让用户可以通过 API 请求来列出所有脚本
@app.get("/scripts")
async def list_scripts_endpoint():
    # 读取配置文件
    with open("./data/config.json") as f:
        config = json.load(f)

    # 返回脚本列表
    return {"scripts": [script["name"] for script in config["scripts"]]}

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
