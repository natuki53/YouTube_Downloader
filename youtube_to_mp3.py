#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTubeからMP3形式でダウンロードするプログラム
yt-dlpを使用してYouTube動画をMP3形式に変換してダウンロードします
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
import re

class YouTubeToMP3:
    def __init__(self, output_dir="downloads"):
        """
        YouTubeToMP3クラスの初期化
        
        Args:
            output_dir (str): ダウンロード先ディレクトリ
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.yt_dlp_path = None
        
    def check_yt_dlp(self):
        """
        yt-dlpがインストールされているかチェック
        
        Returns:
            bool: yt-dlpが利用可能な場合True
        """
        # yt-dlpのパスを探す
        yt_dlp_paths = [
            'yt-dlp',  # PATHにある場合
            '/Users/natuki/Library/Python/3.9/bin/yt-dlp',  # macOSの一般的なパス
            '/usr/local/bin/yt-dlp',  # Homebrewのパス
            '/opt/homebrew/bin/yt-dlp'  # Apple Silicon MacのHomebrewパス
        ]
        
        for path in yt_dlp_paths:
            try:
                result = subprocess.run([path, '--version'], 
                                      capture_output=True, text=True, check=True)
                print(f"yt-dlp バージョン: {result.stdout.strip()}")
                self.yt_dlp_path = path
                return True
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
        
        print("エラー: yt-dlpがインストールされていません")
        print("インストール方法: pip install yt-dlp")
        return False
    
    def download_mp3(self, url, quality="320"):
        """
        YouTube動画をMP3形式でダウンロード
        
        Args:
            url (str): YouTube動画のURL
            quality (str): MP3の音質（kbps）
        
        Returns:
            bool: ダウンロードが成功した場合True
        """
        if not self.check_yt_dlp():
            return False
        
        # 出力ファイル名のテンプレート
        output_template = str(self.output_dir / "%(title)s.%(ext)s")
        
        # yt-dlpコマンドの構築
        cmd = [
            self.yt_dlp_path,
            '--extract-audio',           # 音声のみ抽出
            '--audio-format', 'mp3',     # MP3形式に変換
            '--audio-quality', quality,  # 音質設定
            '--embed-thumbnail',         # サムネイルを埋め込み
            '--output', output_template, # 出力先
            '--no-playlist',             # プレイリストの場合は最初の動画のみ
            url
        ]
        
        try:
            print(f"MP3ダウンロード開始: {url}")
            print(f"出力先: {self.output_dir}")
            print(f"音質: {quality}kbps")
            print("-" * 50)
            
            # yt-dlpコマンドを実行
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            
            print("MP3ダウンロード完了!")
            print(result.stdout)
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"\n❌ MP3ダウンロードエラーが発生しました")
            if e.stderr:
                error_output = e.stderr
                print(f"\nエラー詳細:\n{error_output}")
                
                # Python 3.9非推奨エラーの検出
                if "Python version 3.9 has been deprecated" in error_output or "Please update to Python 3.10" in error_output:
                    print("\n" + "="*60)
                    print("⚠️  Python 3.9が非推奨になっています")
                    print("="*60)
                    print("解決方法:")
                    print("1. Python 3.10以上をインストールしてください")
                    print("   macOS: brew install python@3.10")
                    print("   Windows: https://www.python.org/downloads/ から最新版をダウンロード")
                    print("   Ubuntu/Debian: sudo apt install python3.10")
                    print("\n2. インストール後、以下のコマンドで確認:")
                    print("   python3.10 --version")
                    print("\n3. yt-dlpを再インストール:")
                    print("   python3.10 -m pip install --upgrade yt-dlp")
                    print("="*60)
                
                # HTTP 403エラーの検出
                if "HTTP Error 403" in error_output or "403: Forbidden" in error_output:
                    print("\n" + "="*60)
                    print("⚠️  HTTP 403エラー: YouTubeがアクセスを拒否しました")
                    print("="*60)
                    print("解決方法:")
                    print("1. yt-dlpを最新版にアップデート:")
                    print("   pip install --upgrade yt-dlp")
                    print("   または")
                    print("   python3 -m pip install --upgrade yt-dlp")
                    print("\n2. しばらく時間をおいてから再試行してください")
                    print("3. 別の動画URLで試してください")
                    print("4. 動画が公開されているか、地域制限がないか確認してください")
                    print("="*60)
                
                # その他の一般的なエラー
                if "ERROR" in error_output and "403" not in error_output and "deprecated" not in error_output.lower():
                    print("\n" + "="*60)
                    print("💡 トラブルシューティング:")
                    print("="*60)
                    print("1. yt-dlpを最新版にアップデート:")
                    print("   pip install --upgrade yt-dlp")
                    print("\n2. インターネット接続を確認してください")
                    print("3. YouTubeのURLが正しいか確認してください")
                    print("4. 動画が公開されているか確認してください")
                    print("="*60)
            else:
                print(f"エラー: {e}")
            return False
        except Exception as e:
            print(f"\n❌ 予期しないエラー: {e}")
            return False
    

    
    def download_playlist(self, playlist_url, quality="320", limit=None):
        """
        プレイリストからMP3をダウンロード
        
        Args:
            playlist_url (str): YouTubeプレイリストのURL
            quality (str): MP3の音質（kbps）
            limit (int): ダウンロードする動画数の制限
        
        Returns:
            bool: ダウンロードが成功した場合True
        """
        if not self.check_yt_dlp():
            return False
        
        output_template = str(self.output_dir / "%(playlist_title)s/%(title)s.%(ext)s")
        
        cmd = [
            self.yt_dlp_path,
            '--extract-audio',
            '--audio-format', 'mp3',
            '--audio-quality', quality,
            '--embed-thumbnail',         # サムネイルを埋め込み
            '--output', output_template,
            playlist_url
        ]
        
        if limit:
            cmd.extend(['--playlist-items', f'1-{limit}'])
        
        try:
            print(f"プレイリストダウンロード開始: {playlist_url}")
            print(f"出力先: {self.output_dir}")
            print(f"音質: {quality}kbps")
            if limit:
                print(f"制限: {limit}個の動画")
            print("-" * 50)
            
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            
            print("プレイリストダウンロード完了!")
            print(result.stdout)
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"\n❌ プレイリストダウンロードエラーが発生しました")
            if e.stderr:
                error_output = e.stderr
                print(f"\nエラー詳細:\n{error_output}")
                
                # Python 3.9非推奨エラーの検出
                if "Python version 3.9 has been deprecated" in error_output or "Please update to Python 3.10" in error_output:
                    print("\n" + "="*60)
                    print("⚠️  Python 3.9が非推奨になっています")
                    print("="*60)
                    print("解決方法:")
                    print("1. Python 3.10以上をインストールしてください")
                    print("   macOS: brew install python@3.10")
                    print("   Windows: https://www.python.org/downloads/ から最新版をダウンロード")
                    print("   Ubuntu/Debian: sudo apt install python3.10")
                    print("\n2. インストール後、以下のコマンドで確認:")
                    print("   python3.10 --version")
                    print("\n3. yt-dlpを再インストール:")
                    print("   python3.10 -m pip install --upgrade yt-dlp")
                    print("="*60)
                
                # HTTP 403エラーの検出
                if "HTTP Error 403" in error_output or "403: Forbidden" in error_output:
                    print("\n" + "="*60)
                    print("⚠️  HTTP 403エラー: YouTubeがアクセスを拒否しました")
                    print("="*60)
                    print("解決方法:")
                    print("1. yt-dlpを最新版にアップデート:")
                    print("   pip install --upgrade yt-dlp")
                    print("   または")
                    print("   python3 -m pip install --upgrade yt-dlp")
                    print("\n2. しばらく時間をおいてから再試行してください")
                    print("3. 別の動画URLで試してください")
                    print("4. 動画が公開されているか、地域制限がないか確認してください")
                    print("="*60)
                
                # その他の一般的なエラー
                if "ERROR" in error_output and "403" not in error_output and "deprecated" not in error_output.lower():
                    print("\n" + "="*60)
                    print("💡 トラブルシューティング:")
                    print("="*60)
                    print("1. yt-dlpを最新版にアップデート:")
                    print("   pip install --upgrade yt-dlp")
                    print("\n2. インターネット接続を確認してください")
                    print("3. YouTubeのURLが正しいか確認してください")
                    print("4. 動画が公開されているか確認してください")
                    print("="*60)
            else:
                print(f"エラー: {e}")
            return False
    
    def list_downloads(self):
        """
        ダウンロード済みのMP3ファイル一覧を表示
        """
        mp3_files = list(self.output_dir.glob("**/*.mp3"))
        
        if not mp3_files:
            print("ダウンロード済みのMP3ファイルが見つかりません")
            return
        
        print(f"ダウンロード済みMP3ファイル ({len(mp3_files)}個):")
        print("-" * 50)
        
        for i, mp3_file in enumerate(mp3_files, 1):
            file_size = mp3_file.stat().st_size / (1024 * 1024)  # MB
            print(f"{i:2d}. {mp3_file.name}")
            print(f"    サイズ: {file_size:.1f} MB")
            print(f"    パス: {mp3_file}")
            print()

def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description="YouTubeからMP3形式でダウンロードするプログラム",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # 単一動画をダウンロード
  python youtube_to_mp3.py "https://www.youtube.com/watch?v=VIDEO_ID"
  python youtube_to_mp3.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality 320
  
  # プレイリストをダウンロード
  python youtube_to_mp3.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist
  python youtube_to_mp3.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist --quality 320 --limit 5
  
  # ダウンロード済みファイル一覧を表示
  python youtube_to_mp3.py --list
        """
    )
    
    parser.add_argument('url', nargs='?', help='YouTube動画またはプレイリストのURL')
    parser.add_argument('-o', '--output', default='downloads', 
                       help='出力ディレクトリ (デフォルト: downloads)')
    parser.add_argument('-q', '--quality', default='320', 
                       choices=['64', '128', '192', '256', '320'],
                       help='MP3音質 (デフォルト: 320)')
    parser.add_argument('-p', '--playlist', action='store_true',
                       help='プレイリストとしてダウンロード')
    parser.add_argument('-l', '--limit', type=int,
                       help='プレイリストからダウンロードする動画数の制限')
    parser.add_argument('--list', action='store_true',
                       help='ダウンロード済みMP3ファイル一覧を表示')
    
    args = parser.parse_args()
    
    # インスタンス作成
    downloader = YouTubeToMP3(args.output)
    
    if args.list:
        # ダウンロード済みファイル一覧表示
        downloader.list_downloads()
        return
    
    if not args.url:
        parser.print_help()
        return
    
    # URLがYouTubeのものかチェック
    if not re.search(r'(youtube\.com|youtu\.be)', args.url):
        print("エラー: 有効なYouTube URLを入力してください")
        return
    
    try:
        if args.playlist:
            # プレイリストダウンロード
            success = downloader.download_playlist(args.url, args.quality, args.limit)
        else:
            # 単一動画ダウンロード
            success = downloader.download_mp3(args.url, args.quality)
        
        if success:
            print("\n✅ MP3ダウンロードが正常に完了しました!")
            print(f"ファイルは {args.output} ディレクトリに保存されています")
        else:
            print("\n❌ MP3ダウンロードに失敗しました")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\nダウンロードが中断されました")
        sys.exit(1)
    except Exception as e:
        print(f"\n予期しないエラーが発生しました: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
