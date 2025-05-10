# durable_rules
Expert System

durable_rules/
├── models.py //fact 정의
├── kb.py //질병 - 원인 매핑
├── inference/  //사용자 환경과 가장 밀접한 원인 추론
│   ├── __init__.py
│   ├── engine.py
│   └── rules.py
└── main.py
