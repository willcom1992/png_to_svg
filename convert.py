"""
PNG→SVG 一括変換プログラム

使用方法:
1. pip install vtracer
2. input/ フォルダにPNGファイルを配置
3. python convert.py を実行
4. output/ フォルダにSVGが生成される
"""

from pathlib import Path
import vtracer


def convert_png_to_svg(input_dir: str = "input", output_dir: str = "output") -> None:
    """input_dir内の全PNGファイルをSVGに変換してoutput_dirに保存する"""
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    # 出力フォルダがなければ作成
    output_path.mkdir(exist_ok=True)

    # PNGファイルを検索
    png_files = list(input_path.glob("*.png"))

    if not png_files:
        print(f"変換対象のPNGファイルが見つかりません: {input_path}")
        return

    print(f"{len(png_files)} 個のPNGファイルを検出しました")
    print("-" * 40)

    # 各PNGファイルを変換
    for png_file in png_files:
        svg_file = output_path / f"{png_file.stem}.svg"

        try:
            vtracer.convert_image_to_svg_py(
                str(png_file),
                str(svg_file)
            )
            print(f"✓ {png_file.name} → {svg_file.name}")
        except Exception as e:
            print(f"✗ {png_file.name}: エラー - {e}")

    print("-" * 40)
    print("変換完了")


if __name__ == "__main__":
    convert_png_to_svg()
