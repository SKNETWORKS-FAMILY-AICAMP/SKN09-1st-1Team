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
<div>
  <img width=20% height=20% src="https://avatars.githubusercontent.com/u/192183238?s=400&v=4">
</div>

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

# 3. 기술 스택

<p align="center">🛠 **Backend Framework & Language**</p>
<p align="center">
  <img src="https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white" alt="Python">
</p>
<p align="center"><strong>Python:</strong> 이 프로젝트의 주요 언어로 사용되었습니다.<br>간결하고 읽기 쉬운 문법을 통해 빠른 개발이 가능하며, 데이터 처리 및 웹 애플리케이션 개발에 활용하였습니다.</p>

<p align="center">💾 **Database**</p>
<p align="center">
  <img src="https://img.shields.io/badge/-MySQL-4479A1?logo=mysql&logoColor=white" alt="MySQL">
</p>
<p align="center"><strong>MySQL:</strong> 구조화된 데이터 저장 및 관리에 사용된 관계형 데이터베이스입니다.<br>데이터 무결성과 효율성을 제공하며, 대규모 트랜잭션 처리 및 분석에 적합하여 활용하였습니다.<br>Python의 MySQL Connector 라이브러리를 통해 쉽게 연동하였습니다.</p>

<p align="center">⚙️ **Development Tools**</p>
<p align="center">
  <img src="https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/-VS%20Code-007ACC?logo=visual-studio-code&logoColor=white" alt="VS Code">
</p>
<p align="center"><strong>GitHub:</strong> 프로젝트의 코드 버전 관리 및 협업을 위해 사용되었습니다.<br>코드 변경 사항을 기록하고 팀원들과 협력하여 효율적으로 개발할 수 있습니다.<br>GitHub Actions를 통해 CI/CD 파이프라인을 설정할 수도 있습니다.</p>

<p align="center"><strong>Git:</strong> 로컬 및 원격 저장소를 관리하기 위한 버전 관리 도구입니다.<br>브랜치 전략을 통해 여러 기능을 병렬로 개발하고, 안정적인 통합이 가능합니다.<br>커밋 기록과 코드 히스토리를 통해 추적 가능성을 제공합니다.</p>

<p align="center"><strong>VS Code:</strong> 이 프로젝트에서 사용된 주요 개발 환경(IDE)입니다.<br>Python, MySQL, Git 통합을 위한 다양한 확장 기능을 지원합니다.</p>


---

# 4. WBS

1. 엑셀자료로 DB테이블만 작성-> ERD 작성 (30분) -> SQL쿼리문 작성(지역별/년도별)(15분) -> 파이썬으로 데이터 삽입(4시간) -> 명세서 바탕으로 쿼리문 작성(4시간) -> 스트림릿 작성(1시간)
- ** 요구사항명/ 요구사항 내용 ex) 검색기능, 필터링 기능에 대해 요구사항에 작성하기
<div>
  <img width=100% height=100% src="https://raw.githubusercontent.com/Zayden0815/test/refs/heads/main/screen2025-01-08%20115223.png"/>
</div>
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

- 업무영역
	- KIA 자동차 관련 FAQ
- 사용자 
	- 공용 
- 요구사항명 	
	- KIA 기업의 자동차 관련 FAQ 조회
- 개요 	
	- KIA 기업의 자동차 관련 FAQ를 조회하여 소비자들의 니즈를 해결한다. 
- 요구사항내역  
	-소비자가 가지고 있는 문제를 쉽게 찾게 하기 위해서 키워드 선택 박스를 이용하여 빠르게 니즈에 맞는 질문을 찾게 한다.
	-필요성 : FAQ 라는 이름에 맞게 많은 사람들이 찾게되는 질문이므로 궁금한 내용을 빨리 해소할 수 있게 해야 하기 때문이다.
	-전체 질문들은 게시판 형태로 나타나게 하고 키워드 선택시 게시판에 원하는 질문이 나타나게끔 하고 질문을선택했을 때 답변이 나오도록 한다. 				      
---

# 6. ERD
<div>
  <img width=50% height=50% src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/feature/jaehyeok/images/image.png"/>
</div>



# 7. 수행결과(시연 페이지)
1-1. 자동차 조회 시작 페이지
    - 대분류 조건 제시
    	<div>
      		<img width=50% height=50% src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/feature/jaehyeok/images/%EB%8C%80%EB%B6%84%EB%A5%98%20%ED%95%84%ED%84%B0.png"/>
	</div>
 
1-2. 소분류 필터 조건 제시
    - 대분류에서 선택된 필터에 대한 소분류 필터 항목 제시 & 결과값 출력
<div>
  <img width=50% height=50% src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/feature/jaehyeok/images/%EC%86%8C%EB%B6%84%EB%A5%98%ED%95%84%ED%84%B01.png"/>
  <img width=50% height=50% src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/feature/jaehyeok/images/%EC%86%8C%EB%B6%84%EB%A5%98%ED%95%84%ED%84%B02.png"/>
</div>
---



# 8. 한 줄 회고

- 이재혁
	- 프로젝트 동안 Selenium과 MySql을 모듈화해서 연동시도하다 실패했다. 리팩토링해서 다음 프로젝트 전에 파이썬으로 모듈화에 대해 복습해야겠다.

- 김영서 
	- 이번 프로젝트에서 배웠던 모든 것들을 사용하고 싶었지만 모듈화를 쓰지 못해서 아쉬운 점이 있어 다음 프로젝트에서 모듈화를 써보고 싶은 마음이 있습니다. 또한 python으로 구현할 수 있는 함수들과 매서드를 다양하게 써보려고 합니다. 팀원들과의 소통을 통해 주제선정에서의 의견추합과 프로젝트가 진행되면서의 시행착오들을 해결하며 좋은 경험이 되었습니다.

 - 김정훈
   	- 프로젝트 주제에 대하여, 직접적인 소비자와 최종 사용자의 요구 조건을 만족하고 대응 할 수 있도록 프로젝트의 방향성을 선정하고 고려 하는 것이 중요성을 느꼈습니다. 이번 부트캠프에서 배운 커리큘럼을 적극 반영 하여 프로그래밍 언어를 구사하고, 프로젝트에 부합하는 간결한 방법을 모색하여 구현하는 것을 알게 되었습니다. 현업에서 많이 사용하는 office 프로그램들도 접목하여, 데이터 수집을 기본으로 더 많은 양의 데이터를 간결화 하여 처리 할 수 있을 것이라 생각되며, 구현하기 위해 더욱 다양항 방법을 앞으로 모색해 봐야 겠다는 생각을 하게 되었습니다.

