"""命令行：python3 cli.py "句子" """
import argparse
import json
import sys

from paraphrase import paraphrase, paraphrase_variants


def main(argv=None):
    p = argparse.ArgumentParser(description="paraphrase-lite 同义词改写")
    p.add_argument("text", nargs="?", help="待改写句子")
    p.add_argument("-n", type=int, default=3, help="生成几个版本")
    p.add_argument("--json", action="store_true")
    args = p.parse_args(argv)

    text = args.text or sys.stdin.read()
    if not text.strip():
        print("错误：未提供句子", file=sys.stderr)
        return 2

    variants = paraphrase_variants(text, n=args.n)
    if args.json:
        print(json.dumps(variants, ensure_ascii=False, indent=2))
    else:
        for i, v in enumerate(variants, 1):
            print(f"{i}. {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
