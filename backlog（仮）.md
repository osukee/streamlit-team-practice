## 📋 Product Backlog（仮の案）

> ⚠️ このバックログは現在の仮の案です。チームディスカッション後、変更される可能性があります。

### English Version

| ID    | Epic                  | User Story                                                                                                                                                         | Priority | Story Points |
| ----- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- | -----------: |
| PB-01 | Navigation            | As a user, I want to navigate between the main pages so that I can easily move through project setup, task input, scoring, assignment, and dashboard.              | High     |            3 |
| PB-02 | Project Setup         | As a user, I want to create a group project so that I can manage task assignment for a specific group work project.                                                | High     |            3 |
| PB-03 | Member Setup          | As a user, I want to add group members so that each person can participate in task scoring and assignment.                                                         | High     |            3 |
| PB-04 | Member Setup          | As a user, I want to optionally record each member’s available working time so that the assignment can consider workload capacity.                                 | Medium   |            3 |
| PB-05 | Task Brainstorming    | As a user, I want to add project tasks so that the team can list all work that needs to be completed.                                                              | High     |            5 |
| PB-06 | Task Brainstorming    | As a user, I want to categorize tasks so that the team can understand whether the work is planning, development, design, research, presentation, or documentation. | Medium   |            3 |
| PB-07 | Task Brainstorming    | As a user, I want to edit or delete tasks so that the task list can be corrected before scoring.                                                                   | Medium   |            3 |
| PB-08 | Collaborative Scoring | As a user, I want each member to rate every task from 1 to 5 so that task weight is decided by the whole team instead of one person.                               | High     |            8 |
| PB-09 | Collaborative Scoring | As a user, I want to see the average score for each task so that the team can understand the estimated workload of each task.                                      | High     |            5 |
| PB-10 | Collaborative Scoring | As a user, I want to see score disagreement for each task so that the team can identify tasks where members have different assumptions.                            | High     |            5 |
| PB-11 | Collaborative Scoring | As a user, I want the app to flag tasks with high disagreement so that the team can discuss and clarify them before assignment.                                    | High     |            5 |
| PB-12 | Assignment            | As a user, I want the app to automatically assign tasks so that each member’s total workload score is as balanced as possible.                                     | High     |            8 |
| PB-13 | Assignment            | As a user, I want the app to assign heavier tasks first so that large tasks do not accidentally concentrate on one person.                                         | High     |            5 |
| PB-14 | Assignment            | As a user, I want to see each member’s assigned tasks and total workload score so that I can judge whether the assignment feels fair.                              | High     |            5 |
| PB-15 | Assignment            | As a user, I want to manually adjust task assignments so that the final decision can reflect human judgment and team discussion.                                   | Medium   |            5 |
| PB-16 | Assignment            | As a user, I want the app to recalculate workload scores after manual adjustment so that the team can immediately see whether balance improved or worsened.        | Medium   |            5 |
| PB-17 | Dashboard             | As a user, I want to view a bar chart of workload score by member so that workload imbalance is visually clear.                                                    | High     |            5 |
| PB-18 | Dashboard             | As a user, I want to view a task score table so that I can compare task weights, average scores, and disagreement scores.                                          | High     |            5 |
| PB-19 | Dashboard             | As a user, I want to see the balance gap between the highest and lowest workload so that the fairness of the assignment can be measured.                           | High     |            3 |
| PB-20 | Dashboard             | As a user, I want to see warning messages when one member has much higher workload than others so that the team can reconsider the assignment.                     | High     |            5 |
| PB-21 | UX / Guidance         | As a user, I want short explanations for the 1–5 scoring scale so that members can score tasks consistently.                                                       | High     |            3 |
| PB-22 | UX / Guidance         | As a user, I want example tasks for each score level so that I can understand what “light” or “heavy” means.                                                       | Medium   |            2 |
| PB-23 | Sample Data           | As a user, I want to load sample group work data so that I can understand the app without entering everything manually.                                            | High     |            3 |
| PB-24 | Data Handling         | As a user, I want to export task scores and assignment results as CSV so that the team can share or keep the result.                                               | Medium   |            3 |
| PB-25 | Data Handling         | As a user, I want to import task data from CSV so that the team can prepare tasks outside the app and load them quickly.                                           | Low      |            5 |
| PB-26 | Testing               | As a developer, I want to test the app with realistic group work scenarios so that scoring and assignment results are reliable.                                    | High     |            3 |
| PB-27 | Deployment            | As a user, I want to access the app through a Streamlit link so that team members can try the prototype easily.                                                    | Medium   |            5 |
| PB-28 | Presentation          | As a developer, I want to prepare a demo scenario showing unfair assignment before and after using the app so that the app’s value is easy to understand.          | High     |            3 |


| ID    | Epic     | User Story                                                   | Priority | Story Points |
| ----- | -------- | ------------------------------------------------------------ | -------- | -----------: |
| PB-01 | 画面遷移     | ユーザーとして、プロジェクト作成、タスク入力、スコア付け、割り振り、ダッシュボードの各画面を簡単に移動したい。      | High     |            3 |
| PB-02 | プロジェクト設定 | ユーザーとして、特定のグループワーク用にプロジェクトを作成したい。                            | High     |            3 |
| PB-03 | メンバー登録   | ユーザーとして、グループメンバーを登録したい。各メンバーがタスク評価と割り振りに参加できるようにするため。        | High     |            3 |
| PB-04 | メンバー登録   | ユーザーとして、各メンバーの作業可能時間を任意で登録したい。負担の公平性をより正確に判断するため。            | Medium   |            3 |
| PB-05 | タスク洗い出し  | ユーザーとして、プロジェクトに必要なタスクを追加したい。チームで必要な作業を明確にするため。               | High     |            5 |
| PB-06 | タスク洗い出し  | ユーザーとして、タスクをカテゴリ分けしたい。計画、開発、調査、発表、資料作成などの作業内容を把握するため。        | Medium   |            3 |
| PB-07 | タスク編集    | ユーザーとして、スコア付け前にタスクを編集・削除したい。タスク一覧を正しく保つため。                   | Medium   |            3 |
| PB-08 | 共同スコア付け  | ユーザーとして、各メンバーがすべてのタスクを1〜5点で評価したい。タスクの重さを一人の主観で決めないため。        | High     |            8 |
| PB-09 | 共同スコア付け  | ユーザーとして、各タスクの平均スコアを見たい。タスクごとの重さを把握するため。                      | High     |            5 |
| PB-10 | 共同スコア付け  | ユーザーとして、各タスクの評価のばらつきを見たい。メンバー間で認識がズレているタスクを見つけるため。           | High     |            5 |
| PB-11 | 共同スコア付け  | ユーザーとして、ばらつきが大きいタスクに警告を出してほしい。割り振り前に話し合うべきタスクを明確にするため。       | High     |            5 |
| PB-12 | 自動割り振り   | ユーザーとして、各メンバーの合計スコアができるだけ均等になるように、アプリにタスクを自動割り振りしてほしい。       | High     |            8 |
| PB-13 | 自動割り振り   | ユーザーとして、重いタスクから順に割り振ってほしい。重い作業が一人に集中するのを防ぐため。                | High     |            5 |
| PB-14 | 割り振り結果   | ユーザーとして、各メンバーの担当タスクと合計スコアを確認したい。割り振りが公平か判断するため。              | High     |            5 |
| PB-15 | 手動調整     | ユーザーとして、自動割り振り後に担当者を手動で変更したい。最終判断には人間の納得感も必要だから。             | Medium   |            5 |
| PB-16 | 手動調整     | ユーザーとして、手動変更後に負担スコアを再計算したい。調整によって公平性が改善したか確認するため。            | Medium   |            5 |
| PB-17 | ダッシュボード  | ユーザーとして、メンバー別の負担スコアを棒グラフで見たい。負担の偏りを直感的に理解するため。               | High     |            5 |
| PB-18 | ダッシュボード  | ユーザーとして、タスクごとの平均スコアとばらつきを一覧表で見たい。タスクの重さと認識ズレを比較するため。         | High     |            5 |
| PB-19 | ダッシュボード  | ユーザーとして、最大負担と最小負担の差を見たい。チーム内の公平性を数値で判断するため。                  | High     |            3 |
| PB-20 | アラート     | ユーザーとして、特定のメンバーに負担が偏っているときに警告を出してほしい。割り振りを見直すため。             | High     |            5 |
| PB-21 | UX / 説明  | ユーザーとして、1〜5点の評価基準を見たい。メンバー間で評価基準をそろえるため。                     | High     |            3 |
| PB-22 | UX / 説明  | ユーザーとして、軽いタスク・普通のタスク・重いタスクの例を見たい。スコア付けをしやすくするため。             | Medium   |            2 |
| PB-23 | サンプルデータ  | ユーザーとして、サンプルデータを読み込みたい。入力しなくてもアプリの動きを確認できるようにするため。           | High     |            3 |
| PB-24 | データ出力    | ユーザーとして、スコアと割り振り結果をCSVで出力したい。チームで共有・保存するため。                  | Medium   |            3 |
| PB-25 | データ入力    | ユーザーとして、CSVからタスク一覧を読み込みたい。事前に作ったタスク表をそのまま使うため。               | Low      |            5 |
| PB-26 | テスト      | 開発者として、現実的なグループワークのケースでアプリをテストしたい。スコア計算と割り振りが信頼できるか確認するため。   | High     |            3 |
| PB-27 | デプロイ     | ユーザーとして、Streamlitの公開リンクからアプリにアクセスしたい。チームメンバーが簡単に試せるようにするため。  | Medium   |            5 |
| PB-28 | 発表準備     | 開発者として、不公平な割り振りがアプリによって改善されるデモシナリオを用意したい。アプリの価値を分かりやすく伝えるため。 | High     |            3 |
