from dataclasses import dataclass, asdict
from typing import List

@dataclass
class PetFact:
    breed: str                    # 견종 ex. "Maltese", "Poodle", "Persian"
    age_years: int                # 나이(년단위)
    gender: str                   # 성별"male" / "female"
    neutered: bool                # 중성화 여부
    weight: int          	        #체중 1(0~2kg), 2(2.1~5kg), 3(5.1~10kg), 4(10.1~20kg), 5(20.1~30kg), 6(30.1kg이상)
    lesion_type: str              #CNN에서 도출한 병변 종류A1에서 A6, ex. "A1", "A5"
    underlying_conditions: List[str]  # 기저질환 ex. ["atopy", "food_allergy"], ["autoimmune"]
                                 
    uses_plastic_bowl: bool        #플라스틱식기사용여부 
    season: str                   # "spring"/"summer"/"fall"/"winter"
    bath_freq_per_month: int      # 0,1,2,3,4,5+ 중 하나
    walk_habit: int               # 1~4 산책습관 (1: 냄새만 맡고 지나감, 2: 가끔 물체에 얼굴,몸을 가까이 함, 3: 주변에 몸을 비비거나 눕기도 함, 4 : 풀밭, 먼지에 얼굴,몸을 자주 파묻음)
    sun_exposure: int             # 1~4 햇빛 노출 (1:거의없음, 2:가끔 햇볕을 쬠, 3: 햇빛 아래있는 시간이 꽤 있음, 4: 햇빛 아래 자주 머묾)  
    living_area: str              # "indoor" / "outdoor"
    wash_cycle: int               # 1~4 애완용품 세탁 주기 (1. 주 1회이상 세탁, 2. 2주에 1회정도 세탁, 3. 한 달에 1회정도 세탁, 4. 거의 세탁하지 않음)

    def to_dict(self):
        return asdict(self)