#!/usr/bin/env python3
"""
Bilibili Video Player - Yu Jie Daipai Edition
直接打开 B 站「大东北是我的家乡」影片

Usage:
    python search_bilibili.py
    
Feature:
    🎵 一键播放雨姐经典 BGM！
"""

import subprocess
import sys

# 🎯 「大东北是我的家乡」影片直链
VIDEO_URL = "https://www.bilibili.com/video/BV1Nb4y137E7/?share_source=copy_web&vd_source=11709c79e9637b606b7296b05a8503c6"


def play_daipai_bgm():
    """
    使用 browser-use 直接打开 B 站影片
    """
    print("🎵 播放中：大东北是我的家乡")
    print(f"🔗 影片链接: {VIDEO_URL}")
    print("=" * 50)
    
    try:
        # 使用 browser-use 打开真实浏览器
        cmd = ["browser-use", "--browser", "real", "open", VIDEO_URL]
        print(f"🚀 执行命令: {' '.join(cmd)}")
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print("✅ 浏览器已打开！")
            print("🎤 BGM 起：大东北是我的家乡...")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ 出错了：{result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏱️ 命令执行超时（这可能是正常的，浏览器可能已打开）")
    except FileNotFoundError:
        print("❌ 找不到 browser-use，尝试使用系统浏览器...")
        import webbrowser
        webbrowser.open(VIDEO_URL)
        print("✅ 已使用系统默认浏览器打开！")
        return True
    except Exception as e:
        print(f"❌ 发生错误: {str(e)}")
        return False
    
    return True


def main():
    """主函数"""
    print("=" * 50)
    print("🌪️ 雨姐带派播放器 - B 站版")
    print("=" * 50)
    
    play_daipai_bgm()


if __name__ == "__main__":
    main()
