#!/bin/bash

# 절대경로 기반으로 이동 (사용자 이름 자동 인식)
cd "$HOME/Desktop/kape-data" || {
  echo "폴더가 존재하지 않습니다: ~/Desktop/kape-data"
  exit 1
}

# 스크래퍼 실행
python3 kape-data-scraper.py
