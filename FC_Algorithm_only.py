import pandas as pd

df = pd.read_excel("data_RCA.xlsx", sheet_name="Sheet1", header=0)
df.iloc[:, 2:] = df.iloc[:, 2:].applymap(lambda x: 1 if int(x) >= 1 else 0)

# 迭代F, F的初始值为1
def FC(Q, F):
    Q_tem = {}
    F_tem = {}
    for i in df.itertuples():
        f = sum(df.loc[i[0], j] * Q.get(str(j), 1) for j in df.columns[2:])
        F_tem[str(i[1])] = f

    # 迭代Q, Q的初始值为1
    for i in df.columns[2:]:
        q_denominator = sum(
            df.loc[j[0], i] / F.get(str(j[1]), 1) for j in df.itertuples()
        )
        q = 1 / q_denominator
        Q_tem[str(i)] = q

    # Normalization
    for i in Q_tem.items():
        Q_tem[str(i[0])] = round(i[1] / (sum(Q_tem.values()) / len(Q_tem)), 4)

    for i in F_tem.items():
        F_tem[str(i[0])] = round(i[1] / (sum(F_tem.values()) / len(F_tem)), 4)

    # print(Q_tem, F_tem)
    diff = abs(
        sum(Q_tem.values()) + sum(F_tem.values()) - sum(Q.values()) - sum(F.values())
    )
    return Q_tem, F_tem, diff


Q = {}
F = {}
for _ in range(50):
    Q, F, diff = FC(Q, F)
    print(f"第{_}次迭代：", diff)
    if diff == 0:
        break

# output
pd.DataFrame.from_dict(F, orient='index', columns=['F']).reset_index().rename(columns={'index': '国家'}).to_excel("F.xlsx", index=False)
pd.DataFrame.from_dict(Q, orient='index', columns=['Q']).reset_index().rename(columns={'index': '商品类别'}).to_excel("Q.xlsx", index=False)
