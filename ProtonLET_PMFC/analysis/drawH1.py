import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_last_column(filename):
    # '#'으로 시작하지 않는 행만 읽기
    df = pd.read_csv(filename, 
                    comment='#', 
                    header=None, 
                    delimiter='\s+')
    # 마지막 열 반환
    return df.iloc[:, -1]

# 각 파일 읽기
fluence_values = read_last_column('../results/ProtonFluence.csv')
edep_values = read_last_column('../results/EnergyDeposit.csv')
let_values = read_last_column('../results/ProtonLET.csv')

# 데이터 정규화
fluence_norm = fluence_values / fluence_values.max()
edep_norm = edep_values / edep_values.max()

# E/F ratio 계산
ef_ratio = edep_values / fluence_values

# LET의 20mm 위치의 값 찾기 (인덱스 20)
let_20mm = let_values.iloc[200]
# E/F ratio 정규화
ef_ratio_norm = ef_ratio * (let_20mm / ef_ratio.iloc[200])

# 그래프 생성
fig, ax1 = plt.subplots(figsize=(10, 6))

# 첫 번째 y축 (정규화된 Fluence와 Energy Deposit)
ax1.plot(range(len(fluence_norm)), fluence_norm, 'b-', label='Normalized Fluence')
ax1.plot(range(len(edep_norm)), edep_norm, 'r-', label='Normalized Energy Deposit')
ax1.set_xlabel('Position Index')
ax1.set_ylabel('Normalized Value', color='k')
ax1.tick_params(axis='y', labelcolor='k')
ax1.grid(True, alpha=0.3)

# y축 여백 추가
ax1.set_ylim(-0.1, 1.5)  # 여백을 추가하여 y축 범위 설정

# 두 번째 y축 (LET와 정규화된 E/F ratio)
ax2 = ax1.twinx()
ax2.plot(range(len(let_values)), let_values, 'g-', label='LET')
ax2.plot(range(len(ef_ratio_norm)), ef_ratio_norm, 'm-', label='Normalized E/F Ratio')
ax2.set_ylabel('LET (keV/µm)', color='g')
ax2.tick_params(axis='y', labelcolor='g')

# y축 여백 추가
ax2.set_ylim(0, 25)  # LET y축 여백 추가

# 범례 통합 및 위치 조정
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

plt.title('Normalized Fluence, Energy Deposit, LET and E/F Ratio Distribution')
plt.tight_layout()
plt.show()

# 데이터 값 출력
print("\n=== 데이터 값 출력 ===")
print("Index\t\tFluence\t\t\tEdep\t\t\tLET\t\t\tE/F Ratio\t\tNorm E/F")
print("-" * 120)

data_length = min(len(fluence_values), len(edep_values), len(let_values))
for i in range(data_length):
    print(f"{i+1}\t\t{fluence_values.iloc[i]:.4e}\t{edep_values.iloc[i]:.4e}\t{let_values.iloc[i]:.4e}\t{ef_ratio.iloc[i]:.4e}\t{ef_ratio_norm.iloc[i]:.4e}")

# 통계 결과 출력
print("\n=== 통계 결과 ===")
stats = {
    'Fluence': {
        '최대값': fluence_values.max(),
        '최소값': fluence_values.min(),
        '평균값': fluence_values.mean()
    },
    'Energy Deposit': {
        '최대값': edep_values.max(),
        '최소값': edep_values.min(),
        '평균값': edep_values.mean()
    },
    'LET': {
        '최대값': let_values.max(),
        '최소값': let_values.min(),
        '평균값': let_values.mean()
    },
    'E/F Ratio': {
        '최대값': ef_ratio.max(),
        '최소값': ef_ratio.min(),
        '평균값': ef_ratio.mean()
    }
}

for category, values in stats.items():
    print(f"\n[{category}]")
    for stat_name, stat_value in values.items():
        print(f"{stat_name}: {stat_value:.4e}")