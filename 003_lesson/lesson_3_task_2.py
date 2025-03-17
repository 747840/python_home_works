from smartphone import Smartphone

catalog = [
    Smartphone("HUAWEI", "Pura70_Ultra_16/1TB_Black", "+79055456213"),
    Smartphone("Samsung_Galaxy", "S24_Ultra_12/512GB_Onyx_Black",
               "+79999999999"),
    Smartphone("Apple_iPhone", "16_Pro_Max_1TB_Natural_Titanium",
               "+77456526231"),
    Smartphone("Xiaomi", "14_Ultra_16/512GB_White", "+79022552222"),
    Smartphone("HONOR_Magic", "V2_16/512GB_Black", "+74444444444")
]

for smartphone in catalog:
    print(f"{smartphone.stamp} - {smartphone.model}. {smartphone.number}")
