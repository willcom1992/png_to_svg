# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 言語設定

- 常に日本語で会話する
- コメントも日本語で記述する
- エラーメッセージの説明も日本語で行う
- ドキュメントも日本語で生成する

## プロジェクト概要

vtracerライブラリを使用して、PNG画像をSVG形式に一括変換するPythonユーティリティ。

## コマンド

```bash
# 依存関係のインストール
pip install vtracer

# 変換の実行
python convert.py
```

## 使い方

1. `input/` ディレクトリにPNGファイルを配置
2. `python convert.py` を実行
3. `output/` ディレクトリにSVGファイルが生成される

## 構成

単一ファイル構成（`convert.py`）:
- `input/` 内のPNGファイルを検索
- vtracerを使用して各PNGをSVGに変換
- 同名（拡張子のみ変更）で `output/` に出力
