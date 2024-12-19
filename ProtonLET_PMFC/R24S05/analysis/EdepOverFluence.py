import pandas as pd
import numpy as np

def calculate_fluence_over_edep():
    try:
        # txt 파일 읽기 (공백으로 구분된 데이터)
        # engine='python'을 추가하고 error_bad_lines=False로 설정
        fluence_data = pd.read_csv('../results/ProtonFluence.csv', 
                                 delimiter='\s+', 
                                 header=None,
                                 engine='python',
                                 on_bad_lines='skip',
                                 comment='#')  # '#'으로 시작하는 행은 무시
        edep_data = pd.read_csv('../results/EnergyDeposit.csv', 
                               delimiter='\s+', 
                               header=None,
                               engine='python',
                               on_bad_lines='skip',
                               comment='#')  # '#'으로 시작하는 행은 무시
        
        # 4번째 열 추출 (인덱스는 3)
        fluence_values = fluence_data.iloc[:, 3]
        edep_values = edep_data.iloc[:, 3]
        
        # 나누기 연산 수행
        result = edep_values / fluence_values
        
        print("\n=== 각 위치별 값 ===")
        print("Position\t\tFluence\t\t\tEdep\t\t\tRatio")
        print("-" * 80)
        
        # 각 위치별로 값들을 출력
        for i in range(len(result)):
            position = float(str(fluence_data.iloc[i, 0]).replace(',', ''))  # 쉼표 제거 후 float로 변환
            fluence = fluence_values.iloc[i]
            edep = edep_values.iloc[i]
            ratio = result.iloc[i]
            print(f"{i+1}\t{fluence:.4e}\t{edep:.4e}\t{ratio:.4e}")
        
        # 통계 결과 출력
        print("\n=== 통계 결과 ===")
        ratio_stats = {
            'Fluence 최대값': fluence_values.max(),
            'Fluence 최소값': fluence_values.min(),
            'Fluence 평균값': fluence_values.mean(),
            'Edep 최대값': edep_values.max(),
            'Edep 최소값': edep_values.min(),
            'Edep 평균값': edep_values.mean(),
            '최대 비율': result.max(),
            '최소 비율': result.min(),
            '평균 비율': result.mean(),
            '중간값 비율': result.median()
        }
        
        for key, value in ratio_stats.items():
            print(f"{key}: {value:.4e}")
        
        # 결과를 데이터프레임으로 만들기
        result_df = pd.DataFrame({
            'EdepOverFluence': result
        })
        
        # 결과 저장 (헤더에 # 추가)
        with open('../results/EdepOverFluence.csv', 'w') as f:
            f.write('# EdepOverFluence\n')  # 헤더에 # 추가
            result_df.to_csv(f, index=False, header=False)  # 헤더 제외하고 데이터만 저장
        
        print("계산 완료! EdepOverFluence.csv 파일이 생성되었습니다.")
        
    except FileNotFoundError:
        print("Error: 입력 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"에러 발생: {str(e)}")

if __name__ == "__main__":
    calculate_fluence_over_edep()