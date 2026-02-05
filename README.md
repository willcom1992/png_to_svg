# PNG to SVG Converter

vtracerライブラリを使用して、PNG画像をSVG形式に一括変換するPythonユーティリティです。

## インストール

```bash
pip install vtracer
```

## 使い方

1. `input/` ディレクトリにPNGファイルを配置
2. 変換スクリプトを実行
   ```bash
   python convert.py
   ```
3. `output/` ディレクトリにSVGファイルが生成される

## ディレクトリ構成

```
png_to_svg/
├── convert.py    # 変換スクリプト
├── input/        # 入力PNGファイル
└── output/       # 出力SVGファイル
```

## ライセンス

MIT
