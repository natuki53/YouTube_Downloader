# YouTube ダウンローダー

YouTubeからyt-dlpを使って高品質な動画形式またはMP3形式でダウンロードできるPythonプログラムです。

## 機能

### 動画ダウンロード
- YouTube動画を高品質な動画形式でダウンロード
- 画質選択（144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p）
- 高品質音声との自動マージ
- プレイリスト対応
- 特定の形式IDでの直接指定
- 音声品質・形式のカスタマイズ
- 利用可能な形式一覧表示
- ダウンロード済みファイル一覧表示

### 音声（MP3）ダウンロード
- YouTube動画をMP3形式でダウンロード
- 音質選択（64kbps, 128kbps, 192kbps, 256kbps, 320kbps）
- サムネイル画像の自動埋め込み
- プレイリスト対応
- ダウンロード済みMP3ファイル一覧表示

## インストール

### 0. Pythonのインストール

このプログラムを使用するには、**Python 3.10以上**が必要です（yt-dlpの最新版がPython 3.9を非推奨としているため）。

Pythonがインストールされているか確認するには、ターミナル（コマンドプロンプト）で以下のコマンドを実行してください：

```bash
python --version
```

または

```bash
python3 --version
```

Pythonがインストールされていない場合、以下の手順でインストールしてください。

#### macOS

**方法1: Homebrewを使用（推奨）**
```bash
brew install python3
```

**方法2: 公式インストーラーを使用**
1. [Python公式サイト](https://www.python.org/downloads/)から最新版をダウンロード
2. ダウンロードした`.pkg`ファイルを実行してインストール

#### Windows

1. [Python公式サイト](https://www.python.org/downloads/)から最新版をダウンロード
2. インストーラーを実行し、「Add Python to PATH」にチェックを入れてインストール
3. インストール後、コマンドプロンプトで確認：
```bash
python --version
```

#### Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### その他のLinuxディストリビューション

各ディストリビューションのパッケージマネージャーを使用してPython 3をインストールしてください。

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

または、`pip`コマンドが見つからない場合は：

```bash
python3 -m pip install -r requirements.txt
```

yt-dlpを直接インストールする場合：

```bash
pip install yt-dlp
```

または：

```bash
python3 -m pip install yt-dlp
```

**重要**: HTTP 403エラーが発生する場合は、yt-dlpを最新版にアップデートしてください。

```bash
pip install --upgrade yt-dlp
```

または：

```bash
python3 -m pip install --upgrade yt-dlp
```

### 2. FFmpegのインストール（動画・音声処理に必要）

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
# 単一動画をダウンロード（デフォルト: 720p）
python youtube_video_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"

# 高画質（1080p）でダウンロード
python youtube_video_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality 1080p

# プレイリストをダウンロード
python youtube_video_downloader.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist

# プレイリストから最初の5個の動画のみダウンロード
python youtube_video_downloader.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist --limit 5

# 利用可能な形式一覧を表示
python youtube_video_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --show-formats

# ダウンロード済みファイル一覧を表示
python youtube_video_downloader.py --list
```

### コマンドラインオプション

- `url`: YouTube動画またはプレイリストのURL
- `-o, --output`: 出力ディレクトリ（デフォルト: downloads）
- `-q, --quality`: 動画画質（144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p、デフォルト: 720p）
- `-f, --format-id`: 特定の形式IDを直接指定（例: "270+234"）
- `-a, --audio-quality`: 音声品質（0=最高品質, 9=最低品質、デフォルト: 0）
- `--audio-format`: 音声形式（best, aac, flac, mp3, m4a, opus, vorbis, wav、デフォルト: best）
- `-p, --playlist`: プレイリストとしてダウンロード
- `-l, --limit`: プレイリストからダウンロードする動画数の制限
- `--show-formats`: 利用可能な形式一覧を表示
- `--list`: ダウンロード済みファイル一覧を表示

## 画質と形式IDの対応

プログラムは**動的に**各動画の利用可能な形式を分析し、指定された画質に最適な形式IDを自動選択します。

利用可能な画質オプション：

- **144p**: 144p以下の最高品質動画 + 最高品質音声
- **240p**: 240p以下の最高品質動画 + 最高品質音声
- **360p**: 360p以下の最高品質動画 + 最高品質音声
- **480p**: 480p以下の最高品質動画 + 最高品質音声
- **720p**: 720p以下の最高品質動画 + 最高品質音声
- **1080p**: 1080p以下の最高品質動画 + 最高品質音声
- **1440p**: 1440p以下の最高品質動画 + 最高品質音声
- **2160p**: 2160p以下の最高品質動画 + 最高品質音声

### 動的選択の利点

- **柔軟性**: 動画ごとに最適な形式を自動選択
- **成功率向上**: 利用できない形式でのエラーを回避
- **品質最適化**: 各動画で利用可能な最高品質を自動選択
- **保守性**: 固定IDの更新が不要

## 使用例

### 1. 高画質動画をダウンロード
```bash
# 1080pでダウンロード
python youtube_video_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality 1080p

# 720pでダウンロード
python youtube_video_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality 720p
```

### 2. 特定の形式IDでダウンロード
```bash
# カスタム形式IDを指定
python youtube_video_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --format-id "270+234"
```

### 3. 高品質音声でダウンロード
```bash
# 最高音質でダウンロード
python youtube_video_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality 1080p --audio-quality 0

# FLAC形式でダウンロード
python youtube_video_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality 1080p --audio-format flac
```

### 4. プレイリスト全体をダウンロード
```bash
python youtube_video_downloader.py "https://www.youtube.com/playlist?list=PLxxxxxxxx" --playlist
```

### 5. 利用可能な形式を確認
```bash
python youtube_video_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --show-formats
```

## 音声（MP3）ダウンロード

`youtube_to_mp3.py`を使用して、YouTube動画をMP3形式でダウンロードできます。

### 基本的な使い方

```bash
# 単一動画をMP3形式でダウンロード（デフォルト: 320kbps）
python youtube_to_mp3.py "https://www.youtube.com/watch?v=VIDEO_ID"

# 指定した音質でダウンロード
python youtube_to_mp3.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality 320

# プレイリストをMP3形式でダウンロード
python youtube_to_mp3.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist

# プレイリストから最初の5個の動画のみダウンロード
python youtube_to_mp3.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist --limit 5

# ダウンロード済みMP3ファイル一覧を表示
python youtube_to_mp3.py --list
```

### コマンドラインオプション（MP3）

- `url`: YouTube動画またはプレイリストのURL
- `-o, --output`: 出力ディレクトリ（デフォルト: downloads）
- `-q, --quality`: MP3音質（64, 128, 192, 256, 320 kbps、デフォルト: 320）
- `-p, --playlist`: プレイリストとしてダウンロード
- `-l, --limit`: プレイリストからダウンロードする動画数の制限
- `--list`: ダウンロード済みMP3ファイル一覧を表示

### MP3ダウンロードの特徴

- **高音質**: デフォルトで320kbpsの最高品質MP3
- **サムネイル埋め込み**: 自動的にサムネイル画像をMP3ファイルに埋め込み
- **プレイリスト対応**: プレイリスト全体を一括ダウンロード可能
- **音質選択**: 64kbpsから320kbpsまで音質を選択可能

### MP3ダウンロードの使用例

```bash
# 最高音質（320kbps）でダウンロード
python youtube_to_mp3.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality 320

# 標準音質（192kbps）でダウンロード
python youtube_to_mp3.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality 192

# プレイリスト全体をMP3形式でダウンロード
python youtube_to_mp3.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist

# プレイリストから最初の10個の動画を320kbpsでダウンロード
python youtube_to_mp3.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist --quality 320 --limit 10
```

## 出力

### 動画ファイル

動画ファイルは以下のように保存されます：

- 指定したディレクトリ（デフォルト: `downloads`）に保存されます
- ファイル名は動画のタイトルが使用されます
- 出力形式はMP4に統一されます
- プレイリストの場合は、プレイリスト名のサブディレクトリが作成されます

### MP3ファイル

MP3ファイルは以下のように保存されます：

- 指定したディレクトリ（デフォルト: `downloads`）に保存されます
- ファイル名は動画のタイトルが使用されます
- サムネイル画像が自動的に埋め込まれます
- プレイリストの場合は、プレイリスト名のサブディレクトリが作成されます

## 注意事項

以下の点にご注意ください：

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

動画・音声処理にFFmpegが必要です。上記のインストール手順を参照してください。

### Python 3.9が非推奨というエラーが表示される場合

yt-dlpの最新版はPython 3.10以上を要求します。

以下の手順でPythonをアップグレードしてください：

**macOS:**
```bash
brew install python@3.10
# または最新版
brew install python@3.11
```

**Windows:**
[Python公式サイト](https://www.python.org/downloads/)からPython 3.10以上をダウンロードしてインストール

**Ubuntu/Debian:**
```bash
sudo apt install python3.10
```

インストール後、yt-dlpを再インストールしてください：

```bash
python3.10 -m pip install --upgrade yt-dlp
```

### HTTP 403エラー（Forbidden）が発生する場合

YouTubeがアクセスを拒否している可能性があります。

以下の対処を試してください：

1. **yt-dlpを最新版にアップデート**（最も重要）

```bash
pip install --upgrade yt-dlp
```

2. しばらく時間をおいてから再試行してください

3. 別の動画URLで試してください

4. 動画が公開されているか、地域制限がないか確認してください

### ダウンロードが失敗する場合

以下の点を確認してください：

- インターネット接続を確認
- YouTubeのURLが正しいか確認
- 動画が公開されているか確認
- 地域制限がないか確認
- `--show-formats`で利用可能な形式を確認
- yt-dlpを最新版にアップデート（上記参照）

### 画質が期待と異なる場合

以下の方法を試してください：

- `--show-formats`で利用可能な形式を確認
- `--format-id`で特定の形式IDを直接指定

## ライセンス

このプログラムはMITライセンスの下で公開されています。

## 警告

このプログラムは**学習目的**で作成されたものです。

使用にあたっては、以下の点を必ず遵守してください：

- **著作権の遵守**: 著作権で保護されたコンテンツのダウンロードは、著作権者の許可なく行うと法律に違反する可能性があります
- **YouTubeの利用規約**: YouTubeの利用規約を必ず確認し、遵守してください
- **個人使用のみ**: ダウンロードしたコンテンツは個人使用目的でのみ使用してください
- **商用利用の禁止**: ダウンロードしたコンテンツの商用利用は禁止されています
- **再配布の禁止**: ダウンロードしたコンテンツを無断で再配布することは禁止されています

このプログラムを使用することで発生したいかなる問題についても、開発者は責任を負いません。使用者自身の判断と責任において使用してください。
