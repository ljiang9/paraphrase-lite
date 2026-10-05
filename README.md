# paraphrase-lite

基于内置中英同义词词典的改写小工具。把句中的词/短语替换为同义词，得到保持语义的改写句。零第三方依赖。

## 功能

- 内置中英同义词词典（高兴↔开心、happy↔glad 等）；
- 中文子串替换、英文按词边界替换（不误伤 `bigger`）；
- 英文保留原大小写；
- 最长词优先匹配；
- 一次生成多个不同改写版本。

## 快速开始

```bash
python3 cli.py "我很高兴来到这美丽的地方"
# 1. 我很开心来到这漂亮的地方
# 2. 我很快乐来到这好看的地方
```

## 使用示例

```bash
# 英文
python3 cli.py "I am happy and the big dog runs fast"

# JSON 输出
python3 cli.py "好天气" --json
```

## 无 API Key 如何运行

本工具**完全不需要 API Key**，改写为本地词典替换。

## 目录结构

```
paraphrase-lite/
├── paraphrase.py  # 同义词词典、替换、多版本生成
├── cli.py         # 命令行入口
├── tests/
│   └── test_paraphrase.py
├── README.md
├── LICENSE
└── .gitignore
```

## 测试

```bash
python3 -m unittest discover -s tests
```

## 许可证

[MIT](./LICENSE)
