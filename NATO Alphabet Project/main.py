import pandas as pd
df = pd.read_csv(r"D:\Python Bootcamp\All Practice Projects\NATO Alphabet Project\nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

user_input = input("Enter your first name : ").upper()
user_name_list = [i for i in user_input]
nato_list = [nato_dict[i] for i in user_name_list]
print(nato_list)