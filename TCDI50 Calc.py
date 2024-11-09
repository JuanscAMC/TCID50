import math as m

file_path = input("enter file name:") # insert text file of choice 
Dilution_above_50=m.log10(10**-4) # Virus dilution value above and closest to 50% 
df=float(input("Enter Dilution Factor:"))
Dilution_Factor=m.log10(df) # Dilution Factor used 
Viral_inoculim=float(input("enter viral Inoculated (mL):")) # amount of virus inoculated 

def count_x_and_columns(file_path):
    closest_below = None
    closest_above = None
    target = 0.50 # 50% TCDI constant
    #read Text file 
    with open(file_path, 'r') as file:
        for line in file:
            # Count the amount of wells displaying CFP and the number of columns in the text file
            x_count = line.count('X')
            column_count = len (line.split())
            # Calculate the ratio
            ratio = x_count / column_count if column_count > 0 else 0
            # Track the closest values below the target ratio
            if ratio < target:
                    closest_below = ratio
                    break
             # Track the closest values Above the target ratio
            elif ratio > target:
                    closest_above = ratio
            # Print out details for each line
            print(f"x count: {x_count}, column count: {column_count}, ratio: {ratio:.2f}")
  
    p=((closest_above-.5)/(closest_above-closest_below)) # Calculate PD value 
    TCID50=(Dilution_above_50+(p*Dilution_Factor)) # Calculate TCID50 value
    TCID50_per_mL=(10**-TCID50/Viral_inoculim)  # Calculate TCID50/mL
    print("TCID50:",TCID50)#printTCID50
    print("TCID50 per mL:","%.2e" % TCID50_per_mL)#printTCID50/mL in scientific notation)

if __name__ == "__main__": 
    count_x_and_columns(file_path)