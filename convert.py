"""
画像→SVG 一括変換プログラム

使用方法:
1. pip install vtracer
2. input/ フォルダにPNG/JPGファイルを配置
3. python convert.py を実行
4. output/ フォルダにSVGが生成される
"""

from pathlib import Path
import vtracer


def convert_images_to_svg(input_dir: str = "input", output_dir: str = "output") -> None:
    """input_dir内の全PNG/JPGファイルをSVGに変換してoutput_dirに保存する"""
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    # 出力フォルダがなければ作成
    output_path.mkdir(exist_ok=True)

    # 画像ファイルを検索（PNG, JPG, JPEG）
    image_files = sorted(
        f for ext in ("*.png", "*.jpg", "*.jpeg")
        for f in input_path.glob(ext)
    )

    if not image_files:
        print(f"変換対象の画像ファイルが見つかりません: {input_path}")
        return

    print(f"{len(image_files)} 個の画像ファイルを検出しました")
    print("-" * 40)

    # 各画像ファイルを変換
    for image_file in image_files:
        svg_file = output_path / f"{image_file.stem}.svg"

        try:
            vtracer.convert_image_to_svg_py(
                str(image_file),
                str(svg_file)
            )
            print(f"✓ {image_file.name} → {svg_file.name}")
        except Exception as e:
            print(f"✗ {image_file.name}: エラー - {e}")

    print("-" * 40)
    print("変換完了")


if __name__ == "__main__":
    convert_images_to_svg()
