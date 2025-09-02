import pandas as pd # 表形式データを扱う
import matplotlib.pyplot as plt # グラフを描画
import matplotlib # グラフ描画の設定
import os # ファイル管理

matplotlib.rcParams['font.family'] = 'Meiryo'

FILENAME = "students.csv"

# CSV読み込み（存在しなければ空のDataFrameを返す）
def load_data():
    if os.path.exists(FILENAME):
        df = pd.read_csv(FILENAME)
    else:
        df = pd.DataFrame(columns=["name", "programing_score", "network_score", "math_score",  "programing_GPA", "network_GPA", "math_GPA", "GPA"])
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
    df = pd.concat([df, pd.DataFrame([{
        "name": name, 
        "programing_score": programing_score, 
        "network_score": network_score, 
        "math_score": math_score, 
        }])], ignore_index=True)
    
    save_data(df)
    print(f"{name}さんのデータを追加しました。")

# GPAの計算
def GPA_judgement(subject):
    if subject >= 90:
        return 4
    elif subject >= 80:
        return 3
    elif subject >= 70:
        return 2
    elif subject >= 60:
        return 1
    else:
        return 0
    
# プログラミングの分析
def programing_analysis(df):
    if df.empty:
        print("データがありません。")
        return
    analyze(df, "programing_")

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    # ヒストグラム（10点刻み）
    bins = list(range(0, 101, 10))
    hist_data, bins, _ = axes[0].hist(df['programing_score'], bins=bins, edgecolor="black")
    bin_centers = 0.5 * (bins[1:] + bins[:-1])
    axes[0].set_xticks(bin_centers)
    axes[0].set_title("プログラミング点数分布")
    axes[0].set_xlabel("点数")
    axes[0].set_ylabel("人数")

    # 合格率
    pass_count = (df['programing_score'] >= 60).sum()
    fail_count = (df['programing_score'] < 60).sum()
    axes[1].pie([pass_count, fail_count], labels=["合格", "不合格"], autopct="%1.1f%%")
    axes[1].set_title("プログラミング合格率")

    plt.tight_layout()
    plt.show()

# ネットワークの分析
def network_analysis(df):
    if df.empty:
        print("データがありません。")
        return
    analyze(df, "network_")

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    # ヒストグラム（10点刻み）
    bins = list(range(0, 101, 10))
    hist_data, bins, _ = axes[0].hist(df['network_score'], bins=bins, edgecolor="black")
    bin_centers = 0.5 * (bins[1:] + bins[:-1])
    axes[0].set_xticks(bin_centers)
    axes[0].set_title("ネットワーク点数分布")
    axes[0].set_xlabel("点数")
    axes[0].set_ylabel("人数")

    # 合格率
    pass_count = (df['network_score'] >= 60).sum()
    fail_count = (df['network_score'] < 60).sum()
    axes[1].pie([pass_count, fail_count], labels=["合格", "不合格"], autopct="%1.1f%%")
    axes[1].set_title("ネットワーク合格率")

    plt.tight_layout()
    plt.show()

# 数学の分析
def math_analyssis(df):
    if df.empty:
        print("データがありません。")
        return
    analyze(df, "math_")

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    # ヒストグラム（10点刻み）
    bins = list(range(0, 101, 10))
    hist_data, bins, _ = axes[0].hist(df['math_score'], bins=bins, edgecolor="black")
    bin_centers = 0.5 * (bins[1:] + bins[:-1])
    axes[0].set_xticks(bin_centers)
    axes[0].set_title("数学点数分布")
    axes[0].set_xlabel("点数")
    axes[0].set_ylabel("人数")

    # 合格率
    pass_count = (df['math_score'] >= 60).sum()
    fail_count = (df['math_score'] < 60).sum()
    axes[1].pie([pass_count, fail_count], labels=["合格", "不合格"], autopct="%1.1f%%")
    axes[1].set_title("数学合格率")

    plt.tight_layout()
    plt.show()

# GPAの分析
def GPA_analyssis(df):
    if df.empty:
        print("データがありません。")
        return
    
    GPA_series = ((df['programing_score'].apply(GPA_judgement) +
                   df['network_score'].apply(GPA_judgement) +
                   df['math_score'].apply(GPA_judgement)) / 3).round(2)

    print("\n=== GPA分析 ===")
    print(f"平均GPA: {GPA_series.mean():.2f}")
    print(f"最高GPA: {GPA_series.max():.2f}")
    print(f"最低GPA: {GPA_series.min():.2f}")

    # グラフ表示
    fig, ax = plt.subplots(figsize=(8, 6))

    # ヒストグラム（0.5刻み）
    bins = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    hist_data, bins, _ = ax.hist(GPA_series, bins=bins, edgecolor="black")
    bin_centers = 0.5 * (bins[1:] + bins[:-1])
    ax.set_xticks(bin_centers)
    ax.set_xticklabels([f'{b:.1f}' for b in bin_centers]) # ラベルを小数点以下1桁に
    ax.set_title("GPA分布")
    ax.set_xlabel("GPA")
    ax.set_ylabel("人数")

    plt.tight_layout()
    plt.show()

# 成績分析
def analyze(df, subject):
    if df.empty:
        print("データがありません。")
        return
    print("\n=== 成績分析 ===")
    print(f"平均点: {df[subject + 'score'].mean():.2f}")
    print(f"中央値: {df[subject + 'score'].median():.2f}")
    print(f"標準偏差: {df[subject + 'score'].std():.2f}")
    print(f"最高点: {df[subject + 'score'].max()}")
    print(f"最低点: {df[subject + 'score'].min()}")
    pass_rate = (df[subject + 'score'] >= 60).mean() * 100
    print(f"合格率: {pass_rate:.1f}%")

# 初期メニュー
while True:
    print("\n=== 学生成績分析アプリ ===")
    print("1: 学生追加")
    print("2: プログラミングの分析")
    print("3: ネットワークの分析")
    print("4: 数学の分析")
    print("5: GPAの分析")
    print("0: 終了")

    choice = input("選択: ")
    df = load_data()  # 最新データを毎回読み込み

    if choice == "1":
        add_student()
    elif choice == "2":
        programing_analysis(df)
    elif choice == "3":
        network_analysis(df)
    elif choice == "4":
        math_analyssis(df)
    elif choice == "5":
        GPA_analyssis(df)
    elif choice == "0":
        break
    else:
        print("無効な選択です。")
