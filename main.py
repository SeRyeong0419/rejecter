import os
from reject_module import RejectModule

print("세령이 등장!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("검수도구__ver. 0.7")
print("단일 json 단위만 구현 완료 / 모듈화 완료 / multi json 검수 추가중")

"""
split("_")

PATH
Z:/
    Aivill_3F/
        ...
        Aivill_3F_{name[n]}/
            00_할당/
            01_작업완료/
                ...
                {mmdd}/
                    ...
                    {S}_Clip_{nnnnn}_{nn}/
                        calib/
                        Camera/
                        GNSS_INS/
                        Lidar/
                        Meta/
                        Radar/
                        result/
                        {clip}_sum.csv
                        {clip}_full.csv
            02_반려/
            03_검수대기/
            04_검수완료/
        Drop/
        
    Aivill_4F/
    Aivill_CW/
    TQS/
    
    #recycle/


취합은 검수자 단위 
"""





# super_base = r"C:\aivill_sey_ryeong\labeling\라벨링툴\검수결과\상주근무자\작업완료클립"
# super_base = r"C:\aivill_sey_ryeong\labeling\라벨링툴\검수결과\TQS\작업완료폴더"
super_base = r"C:\aivill_sey_ryeong\labeling\라벨링툴\검수결과\Aivill\작업완료클립"

base_folders = [i for i in os.listdir( super_base ) if ".csv" not in i]

clip_num = 0
reject_num = 0

for base in base_folders:

    # base = r"" ##//클립 바로 상위 폴더

    rej = RejectModule(f"{super_base}/{base}")

    sum, full, rejected = rej.iterate_all() ## pandas df

    clip_num += len(sum)
    reject_num += len(rejected)
    
    sum.to_csv(f"{super_base}/{base}_sum.csv" , index=False, encoding="utf-8-sig")
    full.to_csv(f"{super_base}/{base}_full.csv" , index=False, encoding="utf-8-sig")


print(f"clip num total {clip_num}")

print(f"reject num total {reject_num}")





# base = r"C:\aivill_sey_ryeong\labeling\라벨링툴\extract_2022-08-03-15-44-05\res" ##//클립 바로 상위 폴더

# rej = RejectModule(base)

# sum, full, rejected = rej.iterate_all() ## pandas df



print("\n세령이 퇴장!!!!!!!!!!!!!!!!!!!!!!!!!!")
