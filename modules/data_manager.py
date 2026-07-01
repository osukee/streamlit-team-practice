# B：データ保存・読み込み
"""
データ保存・読み込み機能を管理するモジュール
"""
def add_member(data, member_name):
    """
    メンバーを追加する関数
    """

    # 前後の空白を削除
    member_name = member_name.strip()

    # 空欄チェック
    if member_name == "":
        return data, "Member name cannot be empty."

    # 重複チェック
    for member in data["members"]:
        if member["name"] == member_name:
            return data, "This member already exists."

    # 新しいIDを作成
    new_id = len(data["members"]) + 1

    # メンバー追加
    data["members"].append({
        "id": new_id,
        "name": member_name
    })

    return data, "Member added successfully."
def get_members(data):
    """
    登録済みメンバー一覧を返す
    """
    return data["members"]

