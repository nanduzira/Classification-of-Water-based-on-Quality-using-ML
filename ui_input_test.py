''' UI Terminal Input Test '''
from water_classifier import classify_water

def terminal_ui():
    ''' UI Module '''
    # # User Data Entry
    print("\t\tKERALA WATER AUTHORITY QUALITY CONTROL SUB-DIVISION\n")
    n_tuples = int(input("Number of Test Parameters :"))

    to_predict_list = []
    
    for i in range(n_tuples):
        temp_list = []
        print("PARAMETER TUPLE SET ", i+1)

        para_turbidity = float(input("\t[1]. Turbidity (NTU) :"))
        temp_list.append(para_turbidity)
        para_electrical_conductivity = float(input("\t[2]. Electrical Conductivity (Micro mhos/cm) :"))
        temp_list.append(para_electrical_conductivity)
        para_ph = float(input("\t[3]. pH :"))
        temp_list.append(para_ph)
        para_total_dissolved_solids = float(input("\t[4]. Total Dissolved Solids (mg/Litre) :"))
        temp_list.append(para_total_dissolved_solids)
        para_acidity = float(input("\t[5]. Acditiy :"))
        temp_list.append(para_acidity)
        para_alkalinity = float(input("\t[6]. Alkalinity :"))
        temp_list.append(para_alkalinity)
        para_total_hardness = float(input("\t[7]. Total Hardness (as CaCO3) :"))
        temp_list.append(para_total_hardness)
        para_calcium = float(input("\t[8]. Calcium (as Ca) :"))
        temp_list.append(para_calcium)
        para_magnesium = float(input("\t[9]. Magnesium (as Mg) :"))
        temp_list.append(para_magnesium)
        para_chloride = float(input("\t[10]. Chloride (as Cl) :"))
        temp_list.append(para_chloride)
        para_fluoride = float(input("\t[11]. Fluoride :"))
        temp_list.append(para_fluoride)
        para_iron = float(input("\t[12]. Iron (as Fe) :"))
        temp_list.append(para_iron)
        para_nitrate = float(input("\t[13]. Nitrate (as NO3) :"))
        temp_list.append(para_nitrate)
        para_sulphate = float(input("\t[14]. Sulphate (as SO4) :"))
        temp_list.append(para_sulphate)
        para_coliforms = float(input("\t[15]. Coliforms :"))
        temp_list.append(para_coliforms)
        para_escherichia_coli = float(input("\t[16]. Escherichia Coli :"))
        temp_list.append(para_escherichia_coli)

        # print("TUPLE :", temp_list)
        to_predict_list.append(temp_list)
    
    final_prediction = classify_water("temp.csv", to_predict_list)

    return final_prediction
    
print(terminal_ui())
