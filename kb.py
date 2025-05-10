# File: pet_expert/kb.py

"""
KB (Knowledge Base) for pet dermatology:
- DISEASE_CAUSE_MAPPING: 각 질병별로 원인 식별자(cause key)와
  그 원인을 유발하는 환경 키워드(trigger keywords) 리스트를 맵핑합니다.
"""

from typing import Dict, List

# ┌──────────────────────────────────────────────────────┐
# │ 질병 : {원인 식별자: [유발 환경 키워드,...], ...}  │
# └──────────────────────────────────────────────────────┘
DISEASE_CAUSE_MAPPING: Dict[str, Dict[str, List[str]]] = {
    'folliculitis': {
        'plastic_bowl_contamination': ['plastic_bowl', 'dirty_water'],
        'poor_hygiene': ['outdoor', 'unclean_bedding', 'lack_grooming'],
        'hormonal_imbalance': ['adolescent', 'intact'],
    },
    'dermatophyte_mycosis': {
        'contact_with_infected': ['multi_pet_household', 'shelter'],
        'humid_environment': ['high_humidity', 'poor_ventilation'],
    },
    # TODO: 다른 질병에 대한 매핑을 여기에 추가
}

def get_causes_for(diagnosis: str) -> Dict[str, List[str]]:
    """
    주어진 diagnosis(질병) 에 대해 가능한 원인 식별자와
    해당 원인을 유발하는 환경 키워드 리스트를 반환합니다.
    """
    return DISEASE_CAUSE_MAPPING.get(diagnosis, {})

def list_supported_diseases() -> List[str]:
    """
    KB에 정의된 모든 질병명을 반환합니다.
    """
    return list(DISEASE_CAUSE_MAPPING.keys())
