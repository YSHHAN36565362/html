# 스트림릿 실행 파일
# 페이지가 index.html 하나뿐이라 선택 버튼이 없습니다.
# (버튼을 누를 때마다 화면이 하나씩 늘어나던 문제가 이걸로 없어집니다.)

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="포토스팟", layout="wide")

html = Path("index.html").read_text(encoding="utf-8")
components.html(html, height=7000, scrolling=True)
