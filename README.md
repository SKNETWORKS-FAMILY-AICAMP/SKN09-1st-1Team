# SKN09-1st-1Team

# 1. 팀 소개

- 팀 명 : 재혁아해조
- 김도연, 김영서, 김정훈, 이재혁
- 멤버 개인 깃허브 계정과 연동

---

# 2. 프로젝트 개요

**프로젝트 명**

전국 차량 지역별 목적별 현황 조회 시스템 & 기아자동차의 FAQ 구현


**프로젝트 목표**

전국 차량 데이터를 지역과 목적별로 확인할 수 있도록 한다.
기아자동차 FAQ를 확인할 수 있도록 한다.


**프로젝트 필요성**

지역과 차종 및 유형을 기준으로 원하는 차량 데이터를 쉽고 빠르게 조회할 수 있는 시스템을 개발하여, 기업 또는 정부기관에서 필요한 관련 차량 데이터를 쉽게 제공하고, 데이터 기반 의사결정을 지원해주는 플랫폼을 제공하고자 했다.


**프로젝트 개요**

전국에 등록된 차량의 수를 지역별, 차종별, 유형별로 조회할 수 있는 시스템이다.
전국에 등록된 차량은 사용자가 원하는 조건에 맞는 데이터를 조회하기 어렵다. 예를 들어 서울과 부산만 확인한다거나, 자가용 차량만 확인하거나, 또는 특수목적 차량만 확인하기 어려움이 있다. 따라서 모든 조건을 복합적으로 조건을 걸었을 때도 정확한 데이터를 볼 수 있는 것이 핵심 기능이다.


---

# 3. 기술 스택

> Data Pipeline
> 

https://camo.githubusercontent.com/26af553b066d017a2f36cc4eb3bb99233747fab6b8b7b59f318c9eb70bb7dde1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f56697375616c73747564696f636f64652d3030374143433f7374796c653d666f722d7468652d6261646765266c6f676f3d56697375616c73747564696f636f6465266c6f676f436f6c6f723d7768697465

https://camo.githubusercontent.com/7d5764a6c6bd91d84ba33e5f48649daebbd51e96335e9aceb61154d2a3778bbe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465

https://camo.githubusercontent.com/1c4643d749125cc35e86a7e3ab7ba30e4e5555ff33c740def5fc9ea8a49b5a78/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50616e6461732d3135303435383f7374796c653d666f722d7468652d6261646765266c6f676f3d50616e646173266c6f676f436f6c6f723d7768697465

https://camo.githubusercontent.com/b0c5e90caca848af7c6a6ae15b1072939fd77ae9c37a844eac7259a057032182/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d7953514c2d3434373941313f7374796c653d666f722d7468652d6261646765266c6f676f3d4d7953514c266c6f676f436f6c6f723d7768697465

https://camo.githubusercontent.com/7dcbcf51cfb0e754c79c1552e22b4525c4bf43a7d0c28cae3d3c0a581b0feb07/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e75782d4643433632343f7374796c653d666f722d7468652d6261646765266c6f676f3d4c696e7578266c6f676f436f6c6f723d7768697465

> UI
> 

https://camo.githubusercontent.com/bf0c067ff0a184afb632629abb5c46f9356492fa6985b0fe4ce062d5080df475/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53747265616d6c69742d4646344234423f7374796c653d666f722d7468652d6261646765266c6f676f3d53747265616d6c6974266c6f676f436f6c6f723d7768697465

> Co-Work Tools
> 

https://camo.githubusercontent.com/fd654a8e3b6004b25126b0a14c1109ace9465ff11909f168d6f6bf669318050a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446973636f72642d3538363546323f7374796c653d666f722d7468652d6261646765266c6f676f3d446973636f7264266c6f676f436f6c6f723d7768697465

https://camo.githubusercontent.com/62780b271c043bc23b7925a9a65df4ca7238f4627beea95a59ea88f6af282ba3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d476974266c6f676f436f6c6f723d7768697465

https://camo.githubusercontent.com/98b22de6373b893a56875c85abeb8c35c2c3bf26944f31dce6b00c9a16708456/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3138313731373f7374796c653d666f722d7468652d6261646765266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465

---

# 4. WBS

1. 엑셀자료로 DB테이블만 작성-> ERD 작성 (30분) -> SQL쿼리문 작성(지역별/년도별)(15분) -> 파이썬으로 데이터 삽입(4시간) -> 명세서 바탕으로 쿼리문 작성(4시간) -> 스트림릿 작성(1시간)
- ** 요구사항명/ 요구사항 내용 ex) 검색기능, 필터링 기능에 대해 요구사항에 작성하기

---

# 5. 요구사항 명세서

- ** 스크래핑해서 DB에 저장한것 ERD 구조 필요

---

# 6. ERD

<img align=left src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/feature/jaehyeok/images/image.png"/>

---

# 7. 수행결과(시연 페이지)
1-1. 자동차 조회 시작 페이지
    - 대분류 조건 제시
      <img align=left src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/feature/jaehyeok/images/%EB%8C%80%EB%B6%84%EB%A5%98%20%ED%95%84%ED%84%B0.png"/>

1-2. 소분류 필터 조건 제시
    - 대분류에서 선택된 필터에 대한 소분류 필터 항목 제시 & 결과값 출력
<img align=left src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/feature/jaehyeok/images/%EC%86%8C%EB%B6%84%EB%A5%98%ED%95%84%ED%84%B01.png"/>
<img align=left src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-1Team/blob/feature/jaehyeok/images/%EC%86%8C%EB%B6%84%EB%A5%98%ED%95%84%ED%84%B02.png"/>

---

# 9. 한 줄 회고

 *** 프로젝트를 통해 어떤걸 배웠는지, 성장했는지 (힘들었던 경험/ 기술적인 / 커뮤니케이션)
