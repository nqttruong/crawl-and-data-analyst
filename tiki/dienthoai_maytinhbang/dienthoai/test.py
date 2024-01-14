import pandas as pd

# Tạo DataFrame minh họa
data = {'Gia': ['2.8k', '5k+', '10.000']}
df = pd.DataFrame(data)

def convert_to_number(value):
    if isinstance(value, str):
        if 'k+' in value:
            return float(value.replace('k+', '')) * 1000
        elif 'k' in value:
            return float(value.replace('k', '')) * 1000
        else:
            return float(value) if value else None
    else:
        return value

# Tạo DataFrame minh họa
data = {'Gia': ['2.8k', '5k+', '10.000', '3k', '7k+', 5000.0]}
df = pd.DataFrame(data)

# Áp dụng hàm convert_to_number cho cột 'Gia'
df['Gia'] = df['Gia'].apply(convert_to_number)

# In DataFrame sau khi thực hiện chuyển đổi
print(df)





