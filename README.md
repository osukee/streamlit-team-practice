# streamlit-team-practice
## This is the practice location for Group C.

## Directory Structure
streamlit-team-practice/
├── app.py                         # C：Streamlit UI中心
├── modules/
│   ├── data_manager.py             # B：データ保存・読み込み
│   ├── scoring.py                  # D：平均・ばらつき計算
│   ├── assignment.py               # D：自動割り振り
│   ├── visualization.py            # E：グラフ
│   └── sample_data.py              # B/A：サンプルデータ
├── data/
│   ├── members.csv
│   ├── tasks.csv
│   └── scores.csv
├── README.md                       
└── requirements.txt
└──team.md

### チームのGitHubレポジトリと同期するために（毎作業前にするとよい）
git pull origin main

## How to Create a Branch （ブランチの作り方）
### Branches are created at the Backlog level, not at the individual person level.
命名例:
feature/PB-03-member-setup
feature/PB-05-task-input
feature/PB-08-task-scoring
feature/PB-12-auto-assignment

作るときはこんな感じ:
git checkout main
git pull origin main
git checkout -b feature/PB-08-task-scoring

## How to commit（コミットの仕方）
例：
git add .
git commit -m "PB-xx: message"

## How to push（プッシュの仕方）
初めてそのブランチをpushする場合（例）：
git push -u origin feature/PB-08-task-scoring

2回目以降はこれでOK
git push

