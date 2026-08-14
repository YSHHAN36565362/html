# 포토스팟 (PHOTOSPOT)

강남대학교 K-MOVE 스쿨 HTML 실습 · 미니 홈페이지 과제

사진 찍기 좋은 장소 여섯 곳을 구글 플러스 코드와 내 지도(My Maps)로 소개하는 페이지입니다.

## 파일 구성

| 파일 | 설명 |
|---|---|
| `index.html` | 홈페이지 본문 (한 장짜리 페이지) |
| `images/` | 장소 사진 폴더 |
| `app.py` | 스트림릿 실행 파일 |
| `requirements.txt` | 스트림릿에 필요한 패키지 목록 |

## 사진 파일

| 파일 이름 | 장소 |
|---|---|
| `images/gyeongbokgung.jpg` | 경복궁 |
| `images/olympic-park.jpg` | 올림픽공원 |
| `images/hwaseong-haenggung.jpg` | 화성행궁 |
| `images/minsokchon.jpg` | 한국민속촌 |
| `images/everland.jpg` | 에버랜드 |
| `images/kangnam-univ.jpg` | 강남대학교 |

사진을 바꾸려면 같은 이름으로 덮어쓰면 됩니다. HTML은 고치지 않아도 됩니다.

## 소개한 장소

| 장소 | 플러스 코드 |
|---|---|
| 경복궁 | HXHG+RR 서울특별시 |
| 올림픽공원 | G4CC+7H 서울특별시 |
| 화성행궁 | 72J7+QF 수원시 경기도 |
| 한국민속촌 | 7459+H6 용인시 경기도 |
| 에버랜드 | 76V3+H2 용인시 경기도 |
| 강남대학교 | 74GJ+7X 용인시 경기도 |

## 사용한 기술

HTML만 사용했습니다. (CSS 파일과 자바스크립트 없음)

- 제목, 단락, 목록(`ul` `ol` `dl`), 인용
- 표 (`thead` `tbody` `tfoot`, `rowspan`, `colspan`) — 화면 배치에도 사용
- 이미지 (`img`, `alt` 속성)
- 하이퍼링크와 앵커 (`a href="#아이디"`)
- 입력 양식 (`form` `fieldset` `legend` `label` `input` `select` `textarea` `button`)
- 지도 삽입 (`iframe`)
