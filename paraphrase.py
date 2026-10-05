"""paraphrase-lite — 同义词表改写。

内置中英同义词词典，把句中词/短语替换为同义词得到改写句，保持语义。
零第三方依赖。
"""
from __future__ import annotations

import re

# 内置同义词词典：原词 -> 候选同义词列表
SYNONYMS: dict[str, list[str]] = {
    # 中文
    "高兴": ["开心", "快乐", "愉快"],
    "美丽": ["漂亮", "好看", "靓丽"],
    "快速": ["迅速", "飞快", "火速"],
    "帮助": ["帮忙", "协助", "援助"],
    "巨大": ["庞大", "宏大", "巨型"],
    "喜欢": ["喜爱", "钟爱", "偏好"],
    "重要": ["关键", "要紧", "举足轻重"],
    "认为": ["觉得", "以为", "视作"],
    # 英文
    "happy": ["glad", "cheerful", "delighted"],
    "big": ["large", "huge", "enormous"],
    "fast": ["quick", "rapid", "swift"],
    "good": ["great", "excellent", "fine"],
    "help": ["assist", "aid", "support"],
    "small": ["tiny", "little", "compact"],
}


def paraphrase(text: str, choice: int = 0) -> str:
    """把 text 中可替换词替换为同义词。

    choice 指定每个词取第几个候选（取模），便于生成多种改写。
    中文按子串、英文按词边界匹配，最长词优先。
    """
    keys = sorted(SYNONYMS.keys(), key=len, reverse=True)
    out = text
    for key in keys:
        alts = SYNONYMS[key]
        repl = alts[choice % len(alts)]
        if key == repl:
            continue
        if re.search(r"[a-zA-Z]", key):
            pattern = re.compile(rf"\b{re.escape(key)}\b", re.IGNORECASE)
            def _sub(m, _k=key, _r=repl):
                w = m.group(0)
                if w[0].isupper():
                    return _r.capitalize()
                return _r
            out = pattern.sub(_sub, out)
        else:
            out = out.replace(key, repl)
    return out


def paraphrase_variants(text: str, n: int = 3) -> list[str]:
    """生成 n 个不同改写版本。"""
    seen = []
    for i in range(n * 3):
        p = paraphrase(text, choice=i)
        if p != text and p not in seen:
            seen.append(p)
        if len(seen) >= n:
            break
    return seen
