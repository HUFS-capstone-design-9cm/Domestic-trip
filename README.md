# Domestic-trip


# git 사용법
- 1. git clone [git repository 경로]

- 2. cd [프로젝트 이름] (수정한 파일이 있는 디렉토리로 이동)

- 3. branch
  - git branch [브랜치 이름] : 브랜치 생성
  - git checkout [브랜치이름] : 브랜치로 이동
  - git checkout -b [브랜치이름] : 브랜치 생성 & 해당 브랜치로 이동 

- 4. 수정사항 반영
  - git remote update (branch push전 main에 있는 최신파일로 업데이트)
  - git pull
  
- 5. add, commit, push
  - git add . : 변경된 모든 파일 스테이징 영역에 추가 || git add [올리고 싶은 파일]
  - git commit -m "커밋 메시지"
  - git push origin [브랜치이름]

### 반드시 branch생성 후 푸시할 것!

# commit 컨벤션
- FEATURE : 기능을 추가 또는 수정
- ENV: 개발 환경을 추가 또는 수정 (eslint 변경, dockerfile 변경 등)
- FIX : 버그를 해결
- DOCS : 문서를 수정 (README.md 변경)
- REFACTOR : 코드를 리팩토링, 디렉토리 구조 변경
- TEST : 테스트 코드를 추가 또는 수정
- CHORE: 단순오타, 주석추가
- ex) git commit -m "FEATURE: login 기능 추가"
