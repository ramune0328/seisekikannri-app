import pandas as pd # 表形式データを扱う
import matplotlib.pyplot as plt # グラフを描画
import matplotlib # グラフ描画の設定
import os # ファイル管理

matplotlib.rcParams['font.family'] = 'Meiryo'

FILENAME = r"C:my program\成績管理アプリ\students.csv"

# CSV読み込み（存在しなければ空のDataFrameを返す）
def load_data():
    if os.path.exists(FILENAME):
        df = pd.read_csv(FILENAME)
    else:
        df = pd.DataFrame(columns=["name", "programing-score", "network-score", "math-score"])
    return df

# CSV保存（上書き）
def save_data(df):
    df.to_csv(FILENAME, index=False)
    print("CSVに保存しました。")

# 学生追加（追記）
def add_student():
    df = load_data()
    name = input("学生の名前: ")
    programing_score = int(input("プログラミングの点数: "))
    network_score = int(input("ネットワークの点数: "))
    math_score = int(input("数学の点数: "))
    df = pd.concat([df, pd.DataFrame([{"name": name, "programing-score": programing_score, "network-score": network_score, "math-score": math_score, "total": programing_score + network_score + math_score}])], ignore_index=True)
    save_data(df)
    print(f"{name}さんのデータを追加しました。")

# プログラミングの分析
def programing_analysis(df):
    if df.empty:
        print("データがありません。")
        return
    print("\n=== 成績分析 ===")
    print(f"平均点: {df['programing_score'].mean():.2f}")
    print(f"中央値: {df['programing_score'].median():.2f}")
    print(f"標準偏差: {df['programing_score'].std():.2f}")
    print(f"最高点: {df['programing_score'].max()}")
    print(f"最低点: {df['programing_score'].min()}")
    pass_rate = (df['programing_score'] >= 60).mean() * 100
    print(f"合格率: {pass_rate:.1f}%")

# ネットワークの分析
def network_analysis(df):
    if df.empty:
        print("データがありません。")
        return
    print("\n=== 成績分析 ===")
    print(f"平均点: {df['network_score'].mean():.2f}")
    print(f"中央値: {df['network_score'].median():.2f}")
    print(f"標準偏差: {df['network_score'].std():.2f}")
    print(f"最高点: {df['network_score'].max()}")
    print(f"最低点: {df['network_score'].min()}")
    pass_rate = (df['network_score'] >= 60).mean() * 100
    print(f"合格率: {pass_rate:.1f}%")

# 数学の分析
def math_analyssis(df):
    if df.empty:
        print("データがありません。")
        return
    print("\n=== 成績分析 ===")
    print(f"平均点: {df['math_score'].mean():.2f}")
    print(f"中央値: {df['math_score'].median():.2f}")
    print(f"標準偏差: {df['math_score'].std():.2f}")
    print(f"最高点: {df['math_score'].max()}")
    print(f"最低点: {df['math_score'].min()}")
    pass_rate = (df['math_score'] >= 60).mean() * 100
    print(f"合格率: {pass_rate:.1f}%")

# 成績分析
def analyze(df):
    if df.empty:
        print("データがありません。")
        return
    print("\n=== 成績分析 ===")
    print(f"平均点: {df['score'].mean():.2f}")
    print(f"中央値: {df['score'].median():.2f}")
    print(f"標準偏差: {df['score'].std():.2f}")
    print(f"最高点: {df['score'].max()}")
    print(f"最低点: {df['score'].min()}")
    pass_rate = (df['score'] >= 60).mean() * 100
    print(f"合格率: {pass_rate:.1f}%")

# ヒストグラム
def plot_hist(df):
    if df.empty:
        print("データがありません。")
        return
    df['score'].hist(bins=10, edgecolor="black")
    plt.title("点数分布（ヒストグラム）")
    plt.xlabel("点数")
    plt.ylabel("人数")
    plt.show()

# ランキング（棒グラフ）
def plot_ranking(df):
    if df.empty:
        print("データがありません。")
        return
    ranking = df.sort_values("score", ascending=False).head(10)
    plt.bar(ranking["name"], ranking["score"])
    plt.title("上位10人の点数")
    plt.xlabel("学生名")
    plt.ylabel("点数")
    plt.show()

# 合格率（円グラフ）
def plot_passrate(df):
    if df.empty:
        print("データがありません。")
        return
    pass_count = (df['score'] >= 60).sum()
    fail_count = (df['score'] < 60).sum()
    plt.pie([pass_count, fail_count], labels=["合格", "不合格"], autopct="%1.1f%%")
    plt.title("合格・不合格の割合")
    plt.show()

# 初期メニュー
while True:
    print("\n=== 学生成績分析アプリ ===")
    print("1: 学生追加")
    print("2: 成績分析")
    print("3: ヒストグラム表示")
    print("4: ランキング表示")
    print("5: 合格率グラフ表示")
    print("11: プログラミングの分析")
    print("12: ネットワークの分析")
    print("13: 数学の分析")
    print("0: 終了")

    choice = input("選択: ")
    df = load_data()  # 最新データを毎回読み込み

    if choice == "1":
        add_student()
    elif choice == "2":
        analyze(df)
    elif choice == "3":
        plot_hist(df)
    elif choice == "4":
        plot_ranking(df)
    elif choice == "5":
        plot_passrate(df)
    elif choice == "11":
        programing_analysis(df)
    elif choice == "12":
        network_analysis(df)
    elif choice == "13":
        math_analyssis(df)
    elif choice == "0":
        break
    else:
        print("無効な選択です。")
