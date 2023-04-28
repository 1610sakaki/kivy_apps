#!/bin/bash
sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python \
    python3 \
    python-dev \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev

# 動画や音声の再生、変換に必要なライブラリ
sudo apt-get install -y \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good

# Kivyのインストール
# 1. 仮想環境を作成する
python3 -m venv venv

# 2. 仮想環境をアクティブにする
source venv/bin/activate

# 3. pipを最新バージョンに更新する
pip install --upgrade pip

# 4. Kivyをインストールする
pip install kivy

# 5. インストールが完了したかどうかを確認する
python -c "import kivy; kivy.require('1.11.1')"
