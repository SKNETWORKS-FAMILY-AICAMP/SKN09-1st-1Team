# SKN09-1st-1Team

# 1. 팀 소개
- 팀 명 : 재혁아해조
- 프로젝트 : 자동차등록조회 & 기업FAQ

## Team Members
### 이재혁
<div>
  <img width=20% height=20% src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/main/images/%EB%98%90%EB%98%90.jpg">
</div>


- **Role:** 팀장
- **Responsibilities:**
  - DB 테이블 작성
  - Team DATA 관리
  - PROJECT ISSUES DEVELOP
- **GitHub:** [@ohdyo](https://github.com/ohdyo)

### 김도연
![Profile](https://github.com/doyeon158/profile.jpg)
- **Role:** 팀원
- **Responsibilities:**
  - python code 작성
  - DATA crowling
  - REDME 관리
- **GitHub:** [@doyeon158](https://github.com/doyeon158)

### 김영서
![Profile](https://github.com/youngseo98/profile.jpg)
- **Role:** 팀원
- **Responsibilities:**
  - python code 작성
  - MYSQL 데이터 베이스 관리
  - REDME 관리
- **GitHub:** [@youngseo98](https://github.com/youngseo98)

### 김정훈
![Profile](https://github.com/Zayden0815/profile.jpg)
- **Role:** 팀원
- **Responsibilities:**
  - python code 작성
  - WBS 관리
- **GitHub:** [@Zayden0815](https://github.com/Zayden0815)

---

# 2. 프로젝트 개요

**프로젝트 명**

전국 차량 지역별 목적별 현황 조회 시스템 & 기아자동차의 FAQ 구현


**프로젝트 목표**

전국 차량 데이터를 지역과 목적별로 확인할 수 있도록 한다.
기아자동차 FAQ를 확인할 수 있도록 한다.


**프로젝트 필요성**

지역과 차종 및 유형을 기준으로 원하는 차량 데이터를 쉽고 빠르게 조회할 수 있는 시스템을 개발한다. 기업의 비즈니스 또는 정부기관 등 새로운 차량 정책에 관련한 필요 데이터를 쉽게 제공하고, 데이터 기반 의사결정을 지원해주는 플랫폼을 제공하고자 했다.



**프로젝트 개요**

전국에 등록된 차량의 수를 지역별, 차종별, 유형별로 조회할 수 있는 시스템이다.
전국에 등록된 차량은 사용자가 원하는 조건에 맞는 데이터를 조회하기 어렵다. 예를 들어 서울과 부산만 확인한다거나, 자가용 차량만 확인하거나, 또는 특수목적 차량만 확인하기 어려움이 있다. 따라서 모든 조건을 복합적으로 조건을 걸었을 때도 정확한 데이터를 볼 수 있는 것이 핵심 기능이다.


---

# 3. 기술 스택

- 🛠Backend Framework & Language
- ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
  
- 💾 Database
- ![MySQL](https://img.shields.io/badge/-MySQL-4479A1?logo=mysql&logoColor=white)

- 🤖 AI Model
- ![ChatGPT](https://img.shields.io/badge/-ChatGPT-412991?logo=openai&logoColor=white)
  
- ⚙️ Development Tools
- ![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white)
- ![Git](https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white)
- ![VS Code](https://img.shields.io/badge/-VS%20Code-007ACC?logo=visual-studio-code&logoColor=white)





-기술 스택 설명

-🛠 Backend Framework & Language -

Python: 
이 프로젝트의 주요 언어로 사용되었습니다.
간결하고 읽기 쉬운 문법을 통해 빠른 개발이 가능하며, 데이터 처리 및 웹 애플리케이션 개발에 활용하였습니다.

-💾 Database -

MySQL: 
구조화된 데이터 저장 및 관리에 사용된 관계형 데이터베이스입니다.
데이터 무결성과 효율성을 제공하며, 대규모 트랜잭션 처리 및 분석에 적합하여 활용하였습니다.
Python의 MySQL Connector 라이브러리를 통해 쉽게 연동하였습니다.

-⚙️ Development Tools -

GitHub: 
프로젝트의 코드 버전 관리 및 협업을 위해 사용되었습니다.
코드 변경 사항을 기록하고 팀원들과 협력하여 효율적으로 개발할 수 있습니다.
GitHub Actions를 통해 CI/CD 파이프라인을 설정할 수도 있습니다.

Git:
로컬 및 원격 저장소를 관리하기 위한 버전 관리 도구입니다.
브랜치 전략을 통해 여러 기능을 병렬로 개발하고, 안정적인 통합이 가능합니다.
커밋 기록과 코드 히스토리를 통해 추적 가능성을 제공합니다.

VS Code:
이 프로젝트에서 사용된 주요 개발 환경(IDE)입니다.
Python, MySQL, Git 통합을 위한 다양한 확장 기능을 지원합니다.


---

# 4. WBS

1. 엑셀자료로 DB테이블만 작성-> ERD 작성 (30분) -> SQL쿼리문 작성(지역별/년도별)(15분) -> 파이썬으로 데이터 삽입(4시간) -> 명세서 바탕으로 쿼리문 작성(4시간) -> 스트림릿 작성(1시간)
- ** 요구사항명/ 요구사항 내용 ex) 검색기능, 필터링 기능에 대해 요구사항에 작성하기

---

# 5. 요구사항 명세서

- 업무 영역
  - 지역, 목적별 자동차 등록 대수 조회 서비스
- 사용자
  - 공용
- 요구사항명
  - 조건별 자동차 등록 조회
- 개요
  - 주어진 조건에서 사용자의 요구에 맞게 조회 가능 시스템 구축
- 요구사항 내역 
	- 원하는 목적의 카테고리에 맞게 옵션을 준다.
	- 구체적인 검색을 위해 대분류와 소분류를 통해서 옵션을 제공한다.
	- 옵션 별 다중 선택을 가능하게 하여 여러번 검색의 피로를 없앤다.
		- 만약 지역 옵션을 선택시 해당 도시에 없는 시군구가 옵션으로 보여지는걸 회피하기 위해서 도시에서 선택된 요소로만 시군구 리스트를 보여준다.
	- 최종적으로 원하는 데이터를 차트 형식으로 보여준다.

---

# 6. ERD
<div>
  <img width=50% height=50% align=left src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/feature/jaehyeok/images/image.png"/>
</div>
---



** # 7. 수행결과(시연 페이지) **
1-1. 자동차 조회 시작 페이지
    - 대분류 조건 제시
      <img align=left src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/feature/jaehyeok/images/%EB%8C%80%EB%B6%84%EB%A5%98%20%ED%95%84%ED%84%B0.png"/>

1-2. 소분류 필터 조건 제시
    - 대분류에서 선택된 필터에 대한 소분류 필터 항목 제시 & 결과값 출력
<div>
  <img align=left src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/feature/jaehyeok/images/%EC%86%8C%EB%B6%84%EB%A5%98%ED%95%84%ED%84%B01.png"/>
  <img align=left src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/feature/jaehyeok/images/%EC%86%8C%EB%B6%84%EB%A5%98%ED%95%84%ED%84%B02.png"/>
</div>
---



# 9. 한 줄 회고

 *** 프로젝트를 통해 어떤걸 배웠는지, 성장했는지 (힘들었던 경험/ 기술적인 / 커뮤니케이션)
