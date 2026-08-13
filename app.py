# 스트림릿으로 HTML 홈페이지를 띄우는 최소 코드
# (스트림릿은 파이썬 프로그램이라, HTML 파일만으로는 실행되지 않습니다)

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="포토스팟", layout="wide")

# 왼쪽 사이드바에서 페이지 선택
pages = {
    "홈": "index.html",
    "스팟 소개": "spots.html",
    "추천 · 방명록": "guestbook.html",
}

choice = st.sidebar.radio("페이지 선택", list(pages.keys()))

html = Path(pages[choice]).read_text(encoding="utf-8")
components.html(html, height=3000, scrolling=True)
