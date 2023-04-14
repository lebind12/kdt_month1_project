# [11조] Monthly Project 1개월차

- 역할 분담

| 이름 | 역할 |
| --- | --- |
| 신은채 | 데이터 전처리, EDA, 화면 개발 |
| 조석준 | 데이터 전처리, EDA, API 개발 |
| 이우진 | EDA, Django 세팅, API 개발 |
| 한상희 | 노션정리, 데이터 전처리, EDA, 화면 개발 |
- 데이터 셋

    [World Happiness Report up to 2022](https://www.kaggle.com/datasets/mathurinache/world-happiness-report)
    
    - 경제력, 건강, 자유, 사회적 유대감 등의 지표를 통해 Happiness Score를 산출한다.
    - 각 국가별 대륙별로 비교하고 이를 시각화 해본다.
- 화면 개발
    - Web Framework : Django
    - UI : Bootstrap
    - Data 분석: Pandas, Matplotlib, Seaborn, Numpy…
    
- 결과물
    
    [최종 결과물](https://www.notion.so/4c409d78bc724af994313846784cfcd9)
    
    [EDA 결과](https://www.notion.so/EDA-e2e207ecc4cd4eac800a859fc805886d)
    
     📔 [깃허브 레포지터리](https://github.com/lebind12/kdt_month1_project)
    

🏃🏻‍♂️ 결과 도출 과정

1. ChatGPT를 통해 데이터 시각화 프로젝트 입문용으로 좋은 데이터셋을 추천 받았다. 팀원들의 투표를 통해 데이터셋을 선정했다.
2. 스프린트 식으로 데이터셋 각 feature들에 대해 빠르게 브레인스토밍을 진행했다.
3. 시간을 정해 개략적으로 EDA를 진행했다.
    1. 상관 관계 분석을 통해 GDP, Healthy, Social Support feature간의 관계에 대해 좀더 심도있게 살펴보기로 결정했다.
    2. country 이름과 별개로 region이 매핑된 칼럼이 있고 그렇지 않은 칼럼이 있어 전처리 해주기로 결정했다. (후에 groupby로 이용하기 위해)
    3. Social Support의 경우 수치가 달라 Standard scaler를 적용한 값을 이용해 합치기로 결정했다.
    4. 년도별로 같은 의미를 지닌 feature의 칼럼명이 각각 상이해서 칼럼명이 일치하게 조정해줬다.
4. 연도별로 나눠 팀원끼리 데이터 전처리를 진행 + ( Django + Bootstrap)을 세팅했다.
5. 결과 취합전 EDA(진행중)
    1. 데이터 전처리 문제가 있어 처음 부터 다시 진행(기존 Social Support feature에만 적용시켯던 scaler를 Score, GDP, Health, Social Support 모든 컬럼에 대해 반영시켜줌)

---