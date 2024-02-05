# KnifeHub 

KnifeHub 中的 Knife 取自“瑞士军刀”（Swiss Army Knife）的意思，KnifeHub 允许你收纳你的小工具，可以自由集成可用的 Python 代码的工具库。

这样就能够将自己所需的 Python 代码片段整合到一个地方，并允许通过 API 请求调用。

## 创建一个 KnifeHub 的小工具

以下是创建一个 KnifeHub 的小工具的步骤：

1. **创建脚本目录**：在 `./data` 目录下创建一个新的目录，目录的名称将作为你的脚本的名称。例如，你可以创建一个名为 `pangu_spacing` 的目录。

2. **编写脚本**：在你的脚本目录中创建一个名为 `script.py` 的 Python 脚本。你的脚本应该从命令行参数中接收输入，并通过 `print` 函数输出结果。例如，你可以创建一个使用 `pangu.spacing_text` 函数来添加空格的脚本。

    ```python
    import sys
    import pangu

    def main(input_text):
        spaced_text = pangu.spacing_text(input_text)
        print(spaced_text)

    if __name__ == "__main__":
        input_text = sys.argv[1]
        main(input_text)
    ```

3. **列出依赖**：在你的脚本目录中创建一个名为 `requirements.txt` 的文件，列出你的脚本的依赖。例如，如果你的脚本使用了 `pangu` 模块，那么你的 `requirements.txt` 文件应该包含一行 `pangu`。

## 运行 KnifeHub

你可以通过以下命令在开发环境中运行 KnifeHub：

```
uvicorn main:app --host 0.0.0.0 --port 9080 --reload
```

你也可以通过 Docker 在生产环境中运行 KnifeHub：

```
docker build -t knifehub .
docker run -p 9080:9080 knifehub
```

## 使用 KnifeHub

你可以通过 API 请求来列出所有可用的脚本：

```
GET /scripts
```

你也可以通过 API 请求来运行一个脚本：

```
POST /run/{script_name}
Content-Type: application/json

{
  "script_input": "你的输入文本"
}
```

请注意，`{script_name}` 应该替换为你的脚本的名称，请求体应该包含一个 `script_input` 属性，它的值是你想要传递给你的脚本的输入。
