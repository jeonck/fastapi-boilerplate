# FastAPI Boilerplate

간단하고 빠르게 시작할 수 있는 FastAPI 보일러플레이트입니다. `uv run` 방식을 통해 의존성을 빠르게 설치하고 관리하여 개발자 경험을 향상시킵니다.

## 빠른 시작

### 저장소 클론 후 uv run으로 바로 실행
```bash
git clone https://github.com/jeonck/fastapi-boilerplate.git
cd fastapi-boilerplate

# 가장 간단한 실행 방법 - 경고 메시지 없이 실행
./run.sh

# 또는 다음 방법으로도 실행 가능
# 현재 활성화된 환경 사용 
# uv run --active run.py

# 또는 다음과 같이 환경 변수 직접 설정
# VIRTUAL_ENV=$(pwd)/.venv uv run run.py
```

이 방식은 필요한 모든 패키지를 가장 빠르게 설치하고 개발 서버를 시작합니다.
별도의 가상 환경 설정이나 패키지 설치 과정이 필요 없습니다!

### 애플리케이션 접속
- 웹 인터페이스: http://localhost:8000
- API 문서: http://localhost:8000/docs
- 대화형 API 문서: http://localhost:8000/redoc


## 기능

- 깔끔하고 간소화된 프로젝트 구조
- 모듈화된 CSS
- 간단한 HTML 템플릿
- RESTful API 엔드포인트
- API 문서 자동 생성
- `uv run`을 통한 빠른 의존성 설치 및 실행
- 200라인 이하의 코드 파일

## 기술 스택

본 보일러플레이트는 다음과 같은 기술 스택을 사용합니다:

### 백엔드
- **FastAPI**: 고성능 웹 프레임워크 (비동기 지원)
- **Uvicorn**: ASGI 서버
- **Pydantic**: 데이터 유효성 검사 및 설정 관리
- **SQLAlchemy**: SQL 툴킷 및 ORM (옵션)
- **Python-Jose**: JWT 토큰 관리 (인증 시스템용)
- **Passlib**: 비밀번호 해싱 (보안용)

### 프론트엔드
- **Jinja2**: 서버 사이드 템플릿 엔진
- **HTML5** + **CSS3**: 웹 페이지 구성
- **기본 JavaScript**: 필요한 클라이언트 측 상호작용 (외부 프레임워크 없음)

### 개발 도구
- **uv**: 고속 Python 패키지 관리자
- **Python 3.8+**: 최신 Python 기능 지원
- **hatchling**: 패키지 빌드 시스템

### 선택적 개발 의존성
- **pytest**: 테스트 프레임워크
- **black**: 코드 포맷터
- **isort**: 임포트 정렬
- **ruff**: 린터 (flake8 대체)
- **mypy**: 정적 타입 체커


## 왜 uv를 사용하나요?

`uv`는 최신 Python 패키지 관리자로 다음과 같은 장점을 제공합니다:

1. **빠른 속도**: pip보다 최대 10-100배 빠른 패키지 설치 속도
2. **자동 의존성 관리**: 필요한 패키지를 자동으로 설치
3. **개발자 경험 향상**: 간편한 프로젝트 시작 방식 제공
4. **가상 환경 자동 관리**: 별도의 가상 환경 설정 필요 없음

## 프로젝트 구조

```
fastapi-boilerplate/
├── app/                 # 애플리케이션 패키지
│   ├── static/          # 정적 파일
│   │   ├── css/         # CSS 모듈
│   │   ├── js/          # JavaScript 파일
│   │   └── img/         # 이미지 파일 (favicon 등)
│   ├── templates/       # Jinja2 템플릿
│   ├── core/            # 핵심 설정 모듈
│   │   └── config.py    # 애플리케이션 설정
│   ├── api/             # API 라우터 모듈
│   ├── models/          # 데이터 모델
│   ├── schemas/         # Pydantic 스키마
│   └── main.py          # 애플리케이션 정의
├── run.py               # 애플리케이션 실행 스크립트
├── run.sh               # 경고 없는 실행 스크립트
├── .uv.toml             # uv 설정 파일
├── pyproject.toml       # 프로젝트 설정
└── README.md            # 프로젝트 문서
```

## 폴더 구조 상세 설명

### `app/` - 애플리케이션 패키지

#### `app/static/` - 정적 파일 디렉토리
- **`css/`**: 스타일시트 파일
  - `style.css`: 기본 스타일
  - `normalize.css`: 브라우저 스타일 정규화
- **`js/`**: JavaScript 파일
  - `main.js`: 기본 JavaScript 함수
- **`img/`**: 이미지 파일
  - `favicon.ico`: 웹사이트 아이콘

#### `app/templates/` - Jinja2 템플릿
- `base.html`: 기본 레이아웃 템플릿
- `index.html`: 홈페이지 템플릿
- `about.html`: 소개 페이지 템플릿
- `404.html`: 오류 페이지 템플릿

#### `app/core/` - 핵심 설정 모듈
- **`config.py`**: 애플리케이션 설정 (환경 변수, 데이터베이스 URL 등)
- **`security.py`**: 보안 관련 유틸리티 (암호화, 토큰 처리)
- **`database.py`**: 데이터베이스 연결 및 세션 관리

#### `app/api/` - API 라우팅 모듈
- **`deps.py`**: 의존성 주입 함수 (DB 세션, 사용자 인증)
- **`frontend.py`**: 웹 인터페이스 라우터
- **`api_v1/`**: API 버전 1
  - `api.py`: API 라우터 초기화
  - **`endpoints/`**: 엔드포인트 정의
    - `auth.py`: 인증 관련 엔드포인트
    - `items.py`: 아이템 CRUD 엔드포인트
    - `users.py`: 사용자 관련 엔드포인트

#### `app/models/` - 데이터 모델
- **`user.py`**: 사용자 모델
- **`item.py`**: 아이템 모델
- **`base.py`**: 기본 모델 클래스

#### `app/schemas/` - Pydantic 스키마
- **`user.py`**: 사용자 스키마 (요청/응답 검증)
- **`item.py`**: 아이템 스키마
- **`token.py`**: 토큰 스키마
- **`base.py`**: 기본 스키마 클래스

#### `app/main.py` - 애플리케이션 진입점
애플리케이션 초기화, 미들웨어 설정, 라우터 등록 등 애플리케이션의 핵심 진입점

### `run.py` - 실행 스크립트
개발 서버 실행을 위한 간단한 스크립트

### `run.sh` - 경고 없는 실행 스크립트
시스템 환경 변수 불일치 문제를 해결하는 스크립트

### `pyproject.toml` - 프로젝트 설정
프로젝트 메타데이터, 의존성, 빌드 설정 등 정의

### `.uv.toml` - UV 패키지 관리자 설정
가상 환경 관리 및 UV 도구 설정

## API 예시

기본 보일러플레이트는 다음과 같은 엔드포인트를 제공합니다:

- `GET /`: 홈페이지 (HTML)
- `GET /about`: 소개 페이지 (HTML)
- `GET /api/hello`: 간단한 JSON 응답 API

### API 확장 가능성

`api_v1/endpoints/` 폴더에는 다음과 같은 엔드포인트가 추가로 구현되어 있으며, `main.py`에서 활성화할 수 있습니다:

- **인증 API**:
  - `POST /api/v1/auth/login`: 토큰 발급
  - `POST /api/v1/auth/register`: 사용자 등록

- **사용자 API**:
  - `GET /api/v1/users/`: 사용자 목록 조회
  - `GET /api/v1/users/{user_id}`: 특정 사용자 조회
  - `PUT /api/v1/users/{user_id}`: 사용자 정보 수정
  - `DELETE /api/v1/users/{user_id}`: 사용자 삭제

- **아이템 API**:
  - `GET /api/v1/items/`: 아이템 목록 조회
  - `POST /api/v1/items/`: 새 아이템 생성
  - `GET /api/v1/items/{item_id}`: 특정 아이템 조회
  - `PUT /api/v1/items/{item_id}`: 아이템 수정
  - `DELETE /api/v1/items/{item_id}`: 아이템 삭제

## 확장하기

이 보일러플레이트는 필요에 따라 다음과 같이 확장할 수 있습니다:

1. **데이터베이스 통합 (SQLAlchemy)**
   - 모델 정의 및 마이그레이션
   - CRUD 연산 구현
   - 의존성 주입을 통한 DB 세션 관리

2. **사용자 인증 시스템 (JWT)**
   - 로그인/회원가입 엔드포인트
   - 토큰 기반 인증
   - 권한 관리

3. **더 많은 API 엔드포인트**
   - RESTful CRUD 엔드포인트
   - 비동기 API 구현
   - 여러 라우터 모듈로 구성

4. **테스트 작성**
   - 단위 테스트
   - 통합 테스트
   - 테스트 픽스처 및 모의 객체 사용

## 버전 호환성

- Python 3.8 이상
- FastAPI 0.100.0 이상
- Pydantic 2.0.0 이상

## 라이센스

MIT# fastapi-boilerplate
