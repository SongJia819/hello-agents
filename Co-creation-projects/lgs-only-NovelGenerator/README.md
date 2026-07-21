# NovelGenerator - 智能小说创作助手

> 一个基于 HelloAgents 框架的智能小说辅助创作系统，助力创作者从灵感到完稿的全过程。

## 📝 项目简介

**NovelGenerator** 旨在利用大语言模型（LLM）的强大能力，为小说创作者提供智能化的辅助工具。它不仅仅是一个简单的文本生成器，而是一个能够理解故事结构、保持剧情连贯、并具备上下文记忆能力的创作伙伴。

该项目解决了长篇小说创作中的核心痛点：
- **大纲构建困难**：从模糊的灵感到结构化的大纲，AI 帮你梳理逻辑。
- **剧情连贯性**：在生成后续章节时，自动回顾前文情节和摘要，确保人物行为和剧情发展的合理性。
- **创作效率低**：支持批量生成章节，快速推进故事进度。

## ✨ 核心功能

- [x] **智能大纲生成**：根据用户输入的一句话创意、标题及标签，自动生成包含世界观、人物设定、分卷规划的详细大纲。
- [x] **上下文感知章节生成**：基于大纲和前序章节内容，生成连贯的新章节。支持自动回顾前几章摘要和上一章正文。
- [x] **多章连续创作**：支持一次性生成多个章节，AI 会自动维护剧情发展的连续性。
- [x] **内容管理系统**：
    - 自动保存生成的大纲和章节到本地文件（Markdown格式）。
    - 提供web界面通过 API 接口对内容进行读取、更新和删除。
- [x] **创作记忆机制**：自动提取并维护章节摘要和预测信息，作为后续创作的长期记忆。

## 🛠️ 技术栈

- **核心框架**: HelloAgents框架 - 提供 Agent 编排与工具调用能力，使用SimpleAgent。
- **Web 框架**: FastAPI -以此构建高性能的 RESTful API 服务。
- **数据模型**: Pydantic - 用于数据验证和结构定义。
- **文件存储**: 本地文件系统 (Markdown + JSON) - 方便用户直接查看和编辑生成的内容。
- **大语言模型**: 支持兼容 OpenAI 接口的模型（如 DeepSeek, Qwen 等，通过 .env 配置变量）。

## 🚀 快速开始

### 环境要求

- Python 3.10+

### 安装依赖

pip install -r requirements.txt

### 配置环境

1. 在项目根目录创建 `.env` 文件。
2. 配置你的 LLM 模型信息（参考 HelloAgents 文档或根据实际使用的模型填写）：

```
# .env 示例
LLM_PROVIDER=ollama # 或 openai, qwen 等
LLM_MODEL_ID=qwen2.5-72b-instruct
API_KEY=your_api_key
BASE_URL=http://localhost:11434/v1 # 如果使用本地 Ollama
LLM_TIMEOUT=60
HOST=127.0.0.1
PORT=8000
```

### 运行项目

#### 方式一：启动 API 服务（推荐）

启动后端服务，配合前端界面使用。

```bash
python src/server_app.py
# 或者
uvicorn src.app:app --reload
```

服务启动后，API 文档可访问：`http://127.0.0.1:8000/docs`


#### 方式二：运行测试脚本

如果你想直接在命令行测试生成效果，可以运行 `main.py`：

```bash
python main.py
```

## 📖 使用指南

1. **启动服务**：按照上述步骤启动 FastAPI 服务。
2. **前端交互**：打开 `frontend/index.html`（可以直接在浏览器打开，或通过简单的 HTTP 服务器托管）。
3. **创作流程**：
    - **创建项目**：输入小说标题和 ID。
    - **生成大纲**：输入你的核心创意（如“一个关于AI程序员穿越到代码世界的故事”），点击生成大纲。
    - **生成章节**：大纲生成确认无误后，进入章节生成页面，输入第一章的简要构思（可选），点击生成。
    - **查看与修改**：生成的章节会显示在列表中，你可以点击阅读，并进行手动修改保存。
![NovelGenerator Demo](data/image.png)
 
## 🎯 项目亮点

- **长文本一致性**：通过智能上下文管理和记忆机制，解决长篇生成中的逻辑崩坏问题。
- **结构化工作流**：还原作家真实创作路径（创意 -> 大纲 -> 章节），而非盲目生成。
- **数据完全掌控**：所有创作内容以 Markdown 本地存储，安全可控，方便二次编辑。
- **所见即所得**：提供直观的 Web 界面，实时预览生成效果，支持手动干预与调整。

## 📂 目录结构

```
NovelGenerator/
├── agents/                 # Agent 核心逻辑
│   ├── outline_agent.py    # 大纲生成 Agent
│   ├── chapter_generate_agent.py # 章节生成 Agent
│   └── prompt.py           # Prompt 模板
├── src/                    # API 服务代码
│   └── app.py              # FastAPI 应用入口
├── data/                   # 前端图片
│   └── image.png
├── frontend/               # 前端界面
│   └── index.html
├── outputs/                # 生成结果存储目录
├── main.py                 # 命令行测试脚本
└── README.md               # 项目文档
└── requirements.txt        # 项目依赖
```

## 🔮 未来计划（待定）

- [ ] 增加回退功能。
- [ ] 增加人物与事件、技能等知识图谱功能。
- [ ] 短篇小说生成功能。
- [ ] 引入更多样的小说风格。
- [ ] 优化前端界面体验。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 👤 作者

- GitHub: [@lgs-only](https://github.com/lgs-only)
- Email: liangguangshi123@outlook.com

## 🙏 致谢

感谢Datawhale社区和Hello-Agents项目！
