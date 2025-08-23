# YouTube to MP3 ダウンローダー

YouTubeからyt-dlpを使ってMP3形式でダウンロードできるPythonプログラムです。

## 機能

- YouTube動画をMP3形式でダウンロード
- 音質選択（64, 128, 192, 256, 320 kbps）
- プレイリスト対応
- サムネイル埋め込み
- メタデータ追加
- ダウンロード済みファイル一覧表示

## インストール

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

または、yt-dlpを直接インストール：

```bash
pip install yt-dlp
```

### 2. FFmpegのインストール（音声変換に必要）

#### macOS
```bash
brew install ffmpeg
```

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg
```

#### Windows
[FFmpeg公式サイト](https://ffmpeg.org/download.html)からダウンロードしてインストール

## 使用方法

### 基本的な使い方

```bash
# 単一動画をダウンロード
python youtube_to_mp3.py "https://www.youtube.com/watch?v=VIDEO_ID"

# 高音質（320kbps）でダウンロード
python youtube_to_mp3.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality 320

# プレイリストをダウンロード
python youtube_to_mp3.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist

# プレイリストから最初の5個の動画のみダウンロード
python youtube_to_mp3.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist --limit 5

# ダウンロード済みファイル一覧を表示
python youtube_to_mp3.py --list
```

### コマンドラインオプション

- `url`: YouTube動画またはプレイリストのURL
- `-o, --output`: 出力ディレクトリ（デフォルト: downloads）
- `-q, --quality`: MP3音質（64, 128, 192, 256, 320 kbps、デフォルト: 192）
- `-p, --playlist`: プレイリストとしてダウンロード
- `-l, --limit`: プレイリストからダウンロードする動画数の制限
- `--list`: ダウンロード済みファイル一覧を表示

## 使用例

### 1. 音楽動画をダウンロード
```bash
python youtube_to_mp3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### 2. プレイリスト全体をダウンロード
```bash
python youtube_to_mp3.py "https://www.youtube.com/playlist?list=PLxxxxxxxx" --playlist
```

### 3. 高音質でダウンロード
```bash
python youtube_to_mp3.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality 320
```

### 4. カスタム出力ディレクトリ
```bash
python youtube_to_mp3.py "https://www.youtube.com/watch?v=VIDEO_ID" --output "my_music"
```

## 出力

- MP3ファイルは指定したディレクトリ（デフォルト: `downloads`）に保存されます
- ファイル名は動画のタイトルが使用されます
- プレイリストの場合は、プレイリスト名のサブディレクトリが作成されます
- サムネイル画像と説明文も同時にダウンロードされます

## 注意事項

- YouTubeの利用規約を遵守してください
- 著作権で保護されたコンテンツのダウンロードは法律に違反する可能性があります
- 個人使用目的でのみ使用してください
- 大量のダウンロードは避けてください

## トラブルシューティング

### yt-dlpがインストールされていない場合
```bash
pip install yt-dlp
```

### FFmpegがインストールされていない場合
音声変換にFFmpegが必要です。上記のインストール手順を参照してください。

### ダウンロードが失敗する場合
- インターネット接続を確認
- YouTubeのURLが正しいか確認
- 動画が公開されているか確認
- 地域制限がないか確認

## ライセンス

このプログラムはMITライセンスの下で公開されています。

## 貢献

バグ報告や機能要望は、GitHubのIssuesでお知らせください。
