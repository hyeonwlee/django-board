# Django Board


## 1. 소개

점프 투 장고 교재를 따라 Django 프레임워크를 학습하며 구현한 간단한 질문·답변 게시판 프로젝트입니다.


## 2. 사용 기술

- 언어: Python
- 프레임워크: Django 5.2
- 데이터베이스: SQLite
- 화면: Django 템플릿, HTML/CSS, Bootstrap


## 3. 주요 내용

구현한 주요 기능은 다음과 같습니다.
- 질문·답변 작성, 수정, 삭제 및 추천
- 회원 가입, 로그인·로그아웃
- 질문 검색, 페이지네이션 및 상세 조회
- 답변 댓글 작성
- 모델, 폼, URL 라우팅, 뷰, 템플릿 구성


## 4. 실행 방법

프로젝트 루트에서 다음 명령어를 실행합니다.

```bash
python -m pip install "Django>=5.2,<5.3"
python manage.py migrate
python manage.py runserver
```

브라우저에서 http://127.0.0.1:8000/에 접속합니다.