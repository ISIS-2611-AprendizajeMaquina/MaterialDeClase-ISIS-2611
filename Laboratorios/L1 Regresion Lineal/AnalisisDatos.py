#!/usr/bin/env python
# coding: utf-8

# # Exploración

# In[311]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, FunctionTransformer,MinMaxScaler
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from statsmodels.formula.api import ols

from statsmodels.stats.diagnostic import linear_rainbow
from scipy.stats import ttest_1samp
from statsmodels.stats.stattools import durbin_watson
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
import scipy.stats as stats
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy.stats import shapiro

from dateutil import parser


# In[312]:


datos_enfermedad = pd.read_csv("data/Datos Lab 1.csv")


# In[313]:


data = datos_enfermedad.copy()


# In[314]:


data.head(20)


# In[315]:


display(data.sample(20))


# In[316]:


data.info()


# In[317]:


dict = pd.read_excel("data/DiccPacientes.xlsx")
pd.set_option('display.max_colwidth', None)
dict


# In[318]:


data.shape


# In[319]:


data.describe()


# In[320]:


data.isna().sum()


# In[321]:


((data.isnull().sum()/data.shape[0])).sort_values(ascending=False)


# In[322]:


numeric_cols = data.select_dtypes(include=[np.number]).columns

n_cols = 4
n_rows = int(np.ceil(len(numeric_cols) / n_cols))

fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, n_rows * 4))
axes = axes.flatten()

for idx, col in enumerate(numeric_cols):
    sns.boxplot(y=data[col], ax=axes[idx], color='skyblue')
    axes[idx].set_title(col, fontweight='bold')

for idx in range(len(numeric_cols), len(axes)):
    axes[idx].axis('off')

plt.show()


# In[323]:


filasAlturaNaN = data[data['Height (cm)'].isna() & data['Height (m)'].isna()]
print(f"Total de filas con ambas alturas faltantes: {len(filasAlturaNaN)}")


# In[324]:


filasAlturaNaN


# In[325]:


filasW_HNaN = data[data['Height (cm)'].isna() & data['Abdominal Circumference (cm)'].isna() & data['Waist-to-Height Ratio'].isna()]
print(f"Total de filas con altura (cm), cintura faltantes y ratio faltante: {len(filasW_HNaN)}")


# In[326]:


filasWHNaN = data[data['Height (cm)'].isna() & data['Abdominal Circumference (cm)'].isna()]
print(f"Total de filas con altura (cm) y cintura faltantes: {len(filasWHNaN)}")


# In[327]:


filasWHNaN


# In[328]:


filasHm_NaN = data[data['Height (m)'].isna() & data['Abdominal Circumference (cm)'].isna()]
print(f"Total de filas con altura (m) y cintura faltantes: {len(filasHm_NaN)}")


# In[329]:


filasHW_NaN = data[data['Height (cm)'].isna() & data['Abdominal Circumference (cm)'].isna() & data['Height (m)'].isna()]
print(f"Total de filas con altura (cm) y cintura faltantes: {len(filasHW_NaN)}")


# In[330]:


filasTodoNaN = data[data['Height (cm)'].isna() & data['Abdominal Circumference (cm)'].isna() & data['Height (m)'].isna() & data['Waist-to-Height Ratio'].isna()]
print(f"Total de filas con faltantes: {len(filasTodoNaN)}")


# In[331]:


filasWNaN = data[ data['Abdominal Circumference (cm)'].isna() & data['Waist-to-Height Ratio'].isna()]
print(f"Total de filas con faltantes: {len(filasWNaN)}")


# In[332]:


filasWeightNaN = data[data['Weight (kg)'].isna() & data['BMI'].isna()]
print(f"Total de filas con peso y BMI faltantes: {len(filasWeightNaN)}")


# In[333]:


data["CVD Risk Level"].value_counts()


# In[334]:


data["Blood Pressure Category"].value_counts()


# In[335]:


data["Sex"].value_counts()


# In[336]:


data["Physical Activity Level"].value_counts()


# In[337]:


data['Smoking Status'].value_counts()


# In[338]:


data['Family History of CVD'].value_counts()


# In[339]:


data["Patient ID"].duplicated(keep=False)


# In[340]:


data.loc[
    (data['Total Cholesterol (mg/dL)'] < data['Estimated LDL (mg/dL)']) |
    (data['Total Cholesterol (mg/dL)'] < data['HDL (mg/dL)']),
    [
        'Total Cholesterol (mg/dL)',
        'Estimated LDL (mg/dL)',
        'HDL (mg/dL)'
    ]
]


# In[341]:


duplicados=data[data["Patient ID"].duplicated(keep=False)].sort_values("Patient ID")
duplicados


# In[342]:


duplicados.iloc[5:80]


# In[343]:


dup_counts= (data["Patient ID"].value_counts()
                            .loc[lambda x: x > 1]
                            .sort_values(ascending=False))
for id_,n in dup_counts.items():
    print(f"Patient ID: {id_} → {n} apariciones")


# # Limpieza Inicial De Datos Modelo 1

# In[344]:


dataModelo1=data.copy()


# In[345]:


def convertir_fecha(fecha):
    if pd.isna(fecha):
        return pd.NaT
    try:
        return pd.to_datetime(fecha)
    except:
        try:
            return pd.Timestamp(parser.parse(str(fecha)))
        except:
            return pd.NaT

dataModelo1['Date of Service'] = dataModelo1['Date of Service'].apply(convertir_fecha)
dataModelo1


# In[346]:


dataModelo1['Date of Service'].isna().sum()


# In[347]:


dataModelo1[dataModelo1.duplicated(keep=False)].sort_values("Patient ID")


# Revisión de el número de duplicados exactos en DataFrame para eliminar.

# In[348]:


dataModelo1=dataModelo1.drop_duplicates(keep="last")
dataModelo1[dataModelo1.duplicated(keep=False)]


# Eliminación de duplicados exactos y revisión de que esto si de realizara correctamente.

# In[349]:


duplicadosModelo1=dataModelo1[dataModelo1["Patient ID"].duplicated(keep=False)].sort_values("Patient ID")
duplicadosModelo1


# Revison de Datos de IDs de pacientes duplicados, para revisar las fechas de toma de los datos y si entre estos hay inconsistencias en el CVD Risk Score y en el CVD Risk Level

# In[350]:


indices_eliminar = []
for (pid, fecha), grupo in dataModelo1.groupby(['Patient ID', 'Date of Service']):
    if len(grupo) > 1:
        scores = grupo['CVD Risk Score'].dropna().unique()
        levels = grupo['CVD Risk Level'].dropna().unique()
        if len(scores) > 1 or len(levels) > 1:
            indices_eliminar.extend(grupo.index.tolist())

dataModelo1 = dataModelo1.drop(indices_eliminar)

dataModelo1 = dataModelo1.sort_values('Date of Service', ascending=False)
dataModelo1 = dataModelo1.drop_duplicates(subset='Patient ID', keep='first')


# Se eliminaron los datos que a pesar de haber sido tomados en la misma fecha tenien valores de 'CVD Risk Score' o 'CVD Risk Level' diferentes. En caso de que no existiera esta diferencia se eliminaron los duplicados menos recientes, dejando solo un dato por paciente.

# In[351]:


dataModelo1.shape


# In[352]:


dataModelo1['CVD Risk Score'].isna().sum()


# Revisar El número de datos que tienen el CVD Risk Score vacio (NaN) para eliminar esos datos

# In[353]:


dataModelo1=dataModelo1.dropna(subset=['CVD Risk Score'])


# Eliminación de datos que teinen CVD Risk Score vacio.

# In[354]:


dataModelo1.shape


# Revisión del tamaño de la matriz luego de esta transformacióny revisión de que se eliminaron el número de datos correcto.

# In[355]:


Q1 = dataModelo1['CVD Risk Score'].quantile(0.25)
Q3 = dataModelo1['CVD Risk Score'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR


# calculo de el rango aceptado para los valores del CVD Risk Score mediante el Rango Interquartile

# In[356]:


outliers = dataModelo1[(dataModelo1["CVD Risk Score"] < lower_bound) | (dataModelo1["CVD Risk Score"] > upper_bound)]
len(outliers)


# Revisón de número de outliers que hay en la variable CVD Risk Score para eliminarlos de la tabla

# In[357]:


dataModelo1 = dataModelo1[(dataModelo1["CVD Risk Score"] >= lower_bound) & (dataModelo1["CVD Risk Score"] <= upper_bound)]


# Eliminación de las filas con Outliers en la variable CVD Risk Score

# In[358]:


dataModelo1.shape


# Revisión del tamaño de la matriz luego de esta transformacióny revisión de que se eliminaron el número de datos correcto.

# # Partición de los datos Modelo 1

# In[359]:


target = 'CVD Risk Score'
X_m1 = dataModelo1.drop(columns=[target, 'CVD Risk Level'])
y_m1 = dataModelo1[target]


# Separación de los datos en variables independientes X y variable dependiente Y, siendo la variable dependiente Y 'CVD Risk Score'. Se elimino de el DataFrame la variable 'CVD Risk Level'

# In[360]:


X_m1


# Verificación que la separación de las variables X se realizo correctamente

# In[361]:


y_m1


# Verificación que la separación de la variable Y se realizo correctamente

# In[362]:


X_train_m1, X_test_m1, y_train_m1, y_test_m1 = train_test_split( X_m1, y_m1, test_size=0.25, random_state=42)


# división del conjunto de datos en entrenamiento (**train**) y prueba (**test**). con un tamaño del test del 0.25 del total de los datos y con una semilla de 42

# In[363]:


X_train_m1.shape, y_train_m1.shape


# Tamaño del conjunto de entrenamiento

# In[364]:


X_test_m1.shape, y_test_m1.shape


# Tamaño del conjunto de prueba

# # Construcción del pipeline Modelo 1

# In[365]:


cols_to_drop = ['Patient ID', 'Date of Service','Blood Pressure (mmHg)', 'Height (cm)', 'Height (m)', 'Abdominal Circumference (cm)','Weight (kg)']

def drop_columns(df):
    return df.drop(columns=cols_to_drop, errors="ignore")

dropper = FunctionTransformer(drop_columns)


# In[366]:


numeric_features = ['Age','BMI', 'Total Cholesterol (mg/dL)', 'HDL (mg/dL)', 
            'Fasting Blood Sugar (mg/dL)', 'Waist-to-Height Ratio', 'Systolic BP', 
            'Diastolic BP', 'Estimated LDL (mg/dL)'
]

categorical_features = ['Sex', 'Smoking Status', 'Physical Activity Level', 
                        'Family History of CVD', 'Blood Pressure Category'
]


# In[367]:


def height_filler(df):
    df = df.copy()
    mask_cm = df['Height (cm)'].isna() & df['Height (m)'].notna()
    df.loc[mask_cm, 'Height (cm)'] = df.loc[mask_cm, 'Height (m)'] * 100
    mask_m= df['Height (m)'].isna() & df['Height (cm)'].notna()
    df.loc[mask_m, 'Height (m)'] = df.loc[mask_m, 'Height (cm)'] / 100
    return df

llenar_altura = FunctionTransformer(height_filler)


# In[368]:


def WaistHeightRatioCalculator(df):
    df = df.copy()
    mask = df['Waist-to-Height Ratio'].isna() & df['Abdominal Circumference (cm)'].notna() & df['Height (cm)'].notna()
    df.loc[mask, 'Waist-to-Height Ratio'] = df.loc[mask, 'Abdominal Circumference (cm)'] / df.loc[mask, 'Height (cm)']
    return df

calcular_WHR = FunctionTransformer(WaistHeightRatioCalculator)


# In[369]:


def BloodPressureParser(df):
    df = df.copy()
    mask = df['Blood Pressure (mmHg)'].notna() & (df['Systolic BP'].isna() | df['Diastolic BP'].isna())
    bp_split = df.loc[mask, 'Blood Pressure (mmHg)'].str.split('/', expand=True)
    df.loc[mask, 'Systolic BP'] = pd.to_numeric(bp_split[0], errors='coerce')
    df.loc[mask, 'Diastolic BP'] = pd.to_numeric(bp_split[1], errors='coerce')
    return df

parsear_BP = FunctionTransformer(BloodPressureParser)


# In[370]:


def ImputarPeso(df):
    df = df.copy()
    imputer = KNNImputer(n_neighbors=5)
    cols_to_impute = ['Height (cm)', 'Abdominal Circumference (cm)', 'Waist-to-Height Ratio', 'Age', 'BMI', 'Weight (kg)']

    imputed_array = imputer.fit_transform(df[cols_to_impute])

    df_imputed = pd.DataFrame(imputed_array, columns=cols_to_impute, index=df.index)


    df["Weight (kg)"] = df_imputed["Weight (kg)"]
    return df

imputar_peso = FunctionTransformer(ImputarPeso)


# In[371]:


def LlenarBMI(df):
    df = df.copy()
    mask = df['BMI'].isna() & df['Height (m)'].notna() & df['Weight (kg)'].notna()
    df.loc[mask, 'BMI'] = df.loc[mask, 'Weight (kg)'] / (df.loc[mask, 'Height (m)'] ** 2)
    return df

llenar_BMI = FunctionTransformer(LlenarBMI)



# In[372]:


def imputer_colesterol(df):
    df = df.copy()
    mask = (df['Total Cholesterol (mg/dL)']<100) | (df['Total Cholesterol (mg/dL)'] > 400)
    df.loc[mask, 'Total Cholesterol (mg/dL)'] = df.loc[mask, 'Total Cholesterol (mg/dL)'].clip(lower=100, upper=400)
    return df

imputar_colesterol = FunctionTransformer(imputer_colesterol)


# In[373]:


def imputer_LDL_HDL(df):
    df = df.copy()
    mask_LDL = df['Estimated LDL (mg/dL)'] > df['Total Cholesterol (mg/dL)']
    df.loc[mask_LDL, 'Estimated LDL (mg/dL)'] =np.nan

    mask_HDL = df["HDL (mg/dL)"] > df["Total Cholesterol (mg/dL)"]
    df.loc[mask_HDL, "HDL (mg/dL)"] = np.nan


    cols = [
        "Age",
        "BMI",
        "Systolic BP",
        "Diastolic BP",
        "Fasting Blood Sugar (mg/dL)",
        "Total Cholesterol (mg/dL)",
        "HDL (mg/dL)",
        "Estimated LDL (mg/dL)"
    ]

    imputer = KNNImputer(n_neighbors=5)
    imputed_array = imputer.fit_transform(df[cols])

    df_imputed = pd.DataFrame(imputed_array, columns=cols, index=df.index)


    df["HDL (mg/dL)"] = df_imputed["HDL (mg/dL)"]
    df["Estimated LDL (mg/dL)"] = df_imputed["Estimated LDL (mg/dL)"]

    return df

imputar_LDL_HDL = FunctionTransformer(imputer_LDL_HDL)


# In[374]:


def age_imputer(df):
    df = df.copy()
    median_age = df['Age'].median()
    df['Age'] = df['Age'].fillna(median_age)
    df['Age'] = df['Age'].astype(int)
    return df

imputar_edad = FunctionTransformer(age_imputer)


# In[375]:


def sugar_imputer(df):
    df = df.copy()
    col = "Fasting Blood Sugar (mg/dL)"
    df.loc[(df[col] < 40) | (df[col] > 400), col] = np.nan

    cols_knn = [
    "Age",
    "BMI",
    "Systolic BP",
    "Diastolic BP",
    "Total Cholesterol (mg/dL)",
    "HDL (mg/dL)",
    "Estimated LDL (mg/dL)",
    "Fasting Blood Sugar (mg/dL)"
    ]

    imputer = KNNImputer(n_neighbors=5)

    imputed = imputer.fit_transform(df[cols_knn])
    imputed_df = pd.DataFrame(imputed, columns=cols_knn, index=df.index)

    df["Fasting Blood Sugar (mg/dL)"] = imputed_df["Fasting Blood Sugar (mg/dL)"]
    return df

imputar_sugar = FunctionTransformer(sugar_imputer)


# In[376]:


numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", MinMaxScaler())
])


# In[377]:


categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore", drop="if_binary")),
])


# In[378]:


preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)


# In[379]:


pipeline_regresion=Pipeline(steps=[
    ("llenar_altura", llenar_altura),
    ("calcular_WHR", calcular_WHR),
    ("parsear_BP", parsear_BP),
    ("imputar_peso", imputar_peso),
    ("llenar_BMI", llenar_BMI),
    ("imputar_colesterol", imputar_colesterol),
    ("imputar_LDL_HDL", imputar_LDL_HDL),
    ("imputar_edad", imputar_edad),
    ("imputar_sugar", imputar_sugar),
    ("dropper", dropper),
    ("preprocessor", preprocessor)
])


# In[380]:


from sklearn import set_config
set_config(display="diagram")


# In[381]:


pipeline_regresion


# In[382]:


Xt_train_m1 = pipeline_regresion.fit_transform(X_train_m1)


# In[383]:


feature_names = pipeline_regresion.named_steps["preprocessor"].get_feature_names_out()
Xt_train_df_m1 = pd.DataFrame(
    Xt_train_m1.toarray() if hasattr(Xt_train_m1, "toarray") else Xt_train_m1,
    columns=feature_names,
    index=X_train_m1.index
)


# In[384]:


Xt_train_df_m1


# # Entrenamiento Modelo de Regresión Lineal Modelo 1

# In[385]:


Modelo = LinearRegression()


# In[386]:


Modelo.fit(Xt_train_df_m1,y_train_m1)


# In[387]:


y_train_pred_m1 = Modelo.predict(Xt_train_df_m1)


# In[388]:


mae_train = mean_absolute_error(y_train_m1, y_train_pred_m1)
print("MAE  train:", mae_train)


# In[389]:


mse_train_m1 = mean_squared_error(y_train_m1, y_train_pred_m1)
rmse_train = np.sqrt(mse_train_m1)
print("RMSE train:", rmse_train)


# In[390]:


r2_train_m1 = r2_score(y_train_m1, y_train_pred_m1)
print("R²   train:", r2_train_m1)


# ## Limpieza Inicial de datos Modelo 2

# In[391]:


dataModelo2=data.copy()


# In[392]:


dataModelo2[dataModelo2['CVD Risk Score'].notna() & dataModelo2['CVD Risk Level'].isna()]


# No hay filas que contengan CVD Risck Score pero no Risk Level, lo que demuestra que CVD Risk Level se deriva de Risk Score. Dada la importancia de CVD Risck Score en el contexto, se prefiere eliminar todas las entradas que no contengan esta información.

# In[393]:


def convertir_fecha(fecha):
    if pd.isna(fecha):
        return pd.NaT
    try:
        return pd.to_datetime(fecha)
    except:
        try:
            return pd.Timestamp(parser.parse(str(fecha)))
        except:
            return pd.NaT

dataModelo2['Date of Service'] = dataModelo2['Date of Service'].apply(convertir_fecha)
dataModelo2


# In[394]:


dataModelo2['Date of Service'].isna().sum()


# In[395]:


dataModelo2[dataModelo2.duplicated(keep='first')].sort_values("Patient ID")


# Se revisa si entre los duplicados restantes, si hay inconsistencia entre CVD Risk Score o CVD Risk Level.

# In[396]:


indices_eliminar = []
for (pid, fecha), grupo in dataModelo2.groupby(['Patient ID', 'Date of Service']):
    if len(grupo) > 1:
        scores = grupo['CVD Risk Score'].dropna().unique()
        levels = grupo['CVD Risk Level'].dropna().unique()
        if len(scores) > 1 or len(levels) > 1:
            indices_eliminar.extend(grupo.index.tolist())

dataModelo2 = dataModelo2.drop(indices_eliminar)

dataModelo2 = dataModelo2.sort_values('Date of Service', ascending=False)
dataModelo2 = dataModelo2.drop_duplicates(subset='Patient ID', keep='first')


# Se eliminaron los datos que a pesar de haber sido tomados en la misma fecha tenien valores de 'CVD Risk Score' o 'CVD Risk Level' diferentes. En caso de que no existiera esta diferencia se eliminaron los duplicados menos recientes, dejando solo un dato por paciente.

# In[397]:


dataModelo2.shape


# Revisión y eliminación de las filas con CVD Risk Score nulo.

# In[398]:


print(dataModelo2['CVD Risk Score'].isna().sum())
dataModelo2=dataModelo2.dropna(subset=['CVD Risk Score'])


# Revisión de los datos luego de la eliminación.

# In[399]:


dataModelo2.shape


# Uso del rango Interquantile para identificar los rangos aceptables del CVD Risk Score y eliminación de outliers.

# In[400]:


Q1 = dataModelo2['CVD Risk Score'].quantile(0.25)
Q3 = dataModelo2['CVD Risk Score'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = dataModelo2[(dataModelo2["CVD Risk Score"] < lower_bound) | (dataModelo2["CVD Risk Score"] > upper_bound)]
len(outliers)

dataModelo2 = dataModelo2[(dataModelo2["CVD Risk Score"] >= lower_bound) & (dataModelo2["CVD Risk Score"] <= upper_bound)]


# Revisión de datos luego de la eliminación.

# In[401]:


dataModelo2.shape


# # Partición de los datos Modelo 2

# Separación de los datos en variables independientes X y variable dependiente Y, siendo la variable dependiente Y 'CVD Risk Score'. Se elimina del DataFrame la variable 'CVD Risk Level'

# In[402]:


target = 'CVD Risk Score'
X_m2 = dataModelo2.drop(columns=[target, 'CVD Risk Level'])
y_m2 = dataModelo2[target]


# 

# In[403]:


X_m2


# In[404]:


y_m2


# Se realiza la división del conjunto de datos en entrenamiento (**train**) y prueba (**test**). con un tamaño del test del 0.25 del total de los datos y una semilla de 42.

# In[405]:


X_train_m2, X_test_m2, y_train_m2, y_test_m2 = train_test_split( X_m2, y_m2, test_size=0.25, random_state=42)


# Se consulta el tamaño de datos de entrenamiento y test.

# In[406]:


X_train_m2.shape, y_train_m2.shape


# In[407]:


X_test_m2.shape, y_test_m2.shape


# # Construcción del pipeline Modelo 2

# En primer lugar, se realiza la modificación de variables para mejorar la calidad de los datos.
# 
# A conitnuación, se usa clipping en percentiles para tratamiento de outliers.
# Para variables fisiológicas, se usan clips a rangos razonables basados en conocimiento médico general.
# 
# Clipping evita que extremos (errores de medición) distorsionen la regresión lineal, que es sensible a outliers.
# 
# Referencias usadas para los límites médicos:
# 
# AHA Low Blood Pressure: https://www.heart.org/en/health-topics/high-blood-pressure/the-facts-about-high-blood-pressure/low-blood-pressure-when-blood-pressure-is-too-low
# 
# Mayo Clinic Hypoglycemia: https://www.mayoclinic.org/diseases-conditions/hypoglycemia/symptoms-causes/syc-20373685
# 
# BMI extremo: https://pubmed.ncbi.nlm.nih.gov/26520917/
# 
# Cholesterol too low: https://www.mayoclinic.org/diseases-conditions/high-blood-cholesterol/expert-answers/cholesterol-level/faq-20057952

# In[408]:


import numpy as np

# Diccionario con límites médicos ajustados al contexto
medical_limits = {
    'Age': (1, 100),                       # jóvenes a muy mayores
    'BMI': (15, 55),                       # desnutrición severa a obesidad mórbida
    'Systolic BP': (60, 220),              # hipotensión grave a crisis hipertensiva
    'Diastolic BP': (40, 130),             # shock a crisis hipertensiva
    'Total Cholesterol (mg/dL)': (50, 400),
    'HDL (mg/dL)': (20, 120),
    'Fasting Blood Sugar (mg/dL)': (40, 300)
}


# A continuación, se implementa una función con el pipeline completo de limpieza y transformación:
# 1. Se hace clipping con los límites médicos establecidos anteriormente para recortar valores imposibles que afectarían la regresión lineal. 
# 2. Imputación estratificada de Age por mediana dentro de Sex.
# 3. Imputación sistólica/diastólica por categoría de presión.
# 4. Se crea una variable Age_bin para imputar Weight / Height / BMI por (Sex, Age_bin)
# 5. Se imputa HDL y Total Cholesterol por Sex
# 6. Imputación de Fasting Blood Sugar por Diabetes Status
# 7. Recalaculación de variables como BMI y Waist-to-Height Ratio si hacen falta.
# 8. Eliminación de columnas no necesarias.
# 
# 

# In[409]:


import numpy as np
import pandas as pd
from sklearn.preprocessing import FunctionTransformer

def clip_medical_limits(df, medical_limits):
    df = df.copy()
    for var, (lower, upper) in medical_limits.items():
        if var in df.columns:
            df[var] = np.clip(df[var], lower, upper)
    return df

def imputar_age_por_sex(df):
    df = df.copy()
    if 'Sex' in df.columns and 'Age' in df.columns:
        df['Age'] = df.groupby('Sex')['Age'].transform(lambda x: x.fillna(x.median()))
    return df

def imputar_bp_por_categoria(df):
    df = df.copy()
    if 'Blood Pressure Category' in df.columns and 'Systolic BP' in df.columns:
        df['Systolic BP'] = df.groupby('Blood Pressure Category')['Systolic BP'].transform(lambda x: x.fillna(x.median()))
    if 'Blood Pressure Category' in df.columns and 'Diastolic BP' in df.columns:
        df['Diastolic BP'] = df.groupby('Blood Pressure Category')['Diastolic BP'].transform(lambda x: x.fillna(x.median()))
    return df

def imputar_peso_altura_bmi_por_sex_agebin(df):
    df = df.copy()
    if 'Age' in df.columns:
        df['Age_bin'] = pd.cut(df['Age'], bins=[0, 20, 40, 60, 80, 120], include_lowest=True)

        if 'Weight (kg)' in df.columns and 'Sex' in df.columns:
            df['Weight (kg)'] = df.groupby(['Sex', 'Age_bin'])['Weight (kg)'].transform(lambda x: x.fillna(x.median()))
        if 'Height (m)' in df.columns and 'Sex' in df.columns:
            df['Height (m)'] = df.groupby(['Sex', 'Age_bin'])['Height (m)'].transform(lambda x: x.fillna(x.median()))
        if 'BMI' in df.columns and 'Sex' in df.columns:
            df['BMI'] = df.groupby(['Sex', 'Age_bin'])['BMI'].transform(lambda x: x.fillna(x.median()))

        df = df.drop(columns=['Age_bin'], errors='ignore')
    return df

def imputar_lipidos_por_sex(df):
    df = df.copy()
    if 'Sex' in df.columns and 'HDL (mg/dL)' in df.columns:
        df['HDL (mg/dL)'] = df.groupby('Sex')['HDL (mg/dL)'].transform(lambda x: x.fillna(x.median()))
    if 'Sex' in df.columns and 'Total Cholesterol (mg/dL)' in df.columns:
        df['Total Cholesterol (mg/dL)'] = df.groupby('Sex')['Total Cholesterol (mg/dL)'].transform(lambda x: x.fillna(x.median()))
    return df

def imputar_azucar_por_diabetes(df):
    df = df.copy()
    if 'Diabetes Status' in df.columns and 'Fasting Blood Sugar (mg/dL)' in df.columns:
        df['Fasting Blood Sugar (mg/dL)'] = df.groupby('Diabetes Status')['Fasting Blood Sugar (mg/dL)'].transform(lambda x: x.fillna(x.median()))
    return df

def recalcular_bmi(df):
    df = df.copy()
    if 'BMI' in df.columns and 'Weight (kg)' in df.columns and 'Height (m)' in df.columns:
        mask_bmi_nan = df['BMI'].isna()
        df.loc[mask_bmi_nan & df['Weight (kg)'].notna() & df['Height (m)'].notna(), 'BMI'] = (
            df['Weight (kg)'] / (df['Height (m)'] ** 2)
        )
    return df

def recalcular_wthr(df):
    df = df.copy()
    if 'Waist-to-Height Ratio' in df.columns and 'Abdominal Circumference (cm)' in df.columns and 'Height (m)' in df.columns:
        mask_wthr_nan = df['Waist-to-Height Ratio'].isna()
        df.loc[mask_wthr_nan & df['Abdominal Circumference (cm)'].notna() & df['Height (m)'].notna(), 'Waist-to-Height Ratio'] = (
            df['Abdominal Circumference (cm)'] / (df['Height (m)'] * 100)
        )
    return df

def drop_cols_modelo2(df, cols_drop):
    df = df.copy()
    return df.drop(columns=cols_drop, errors='ignore')


# Con las funciones implementadas, se procede a realizar las transformaciones en el dataframe.

# In[410]:


cols_drop_m2 = [
    'Patient ID', 'Date of Service', 'Weight (kg)', 'Height (cm)',
    'Blood Pressure (mmHg)', 'Estimated LDL (mg/dL)', 'CVD Risk Level'
]

clipper_m2   = FunctionTransformer(lambda df: clip_medical_limits(df, medical_limits), feature_names_out="one-to-one")
age_m2       = FunctionTransformer(imputar_age_por_sex, feature_names_out="one-to-one")
bp_m2        = FunctionTransformer(imputar_bp_por_categoria, feature_names_out="one-to-one")
whb_m2       = FunctionTransformer(imputar_peso_altura_bmi_por_sex_agebin, feature_names_out="one-to-one")
lipidos_m2   = FunctionTransformer(imputar_lipidos_por_sex, feature_names_out="one-to-one")
azucar_m2    = FunctionTransformer(imputar_azucar_por_diabetes, feature_names_out="one-to-one")
bmi_m2       = FunctionTransformer(recalcular_bmi, feature_names_out="one-to-one")
wthr_m2      = FunctionTransformer(recalcular_wthr, feature_names_out="one-to-one")
dropper_m2   = FunctionTransformer(lambda df: drop_cols_modelo2(df, cols_drop_m2), feature_names_out="one-to-one")


# Con esto, se desarrolla el pipeline. En principio, se identifican las columnas numéricas y categóricas, para después realizar el preprocessing y el column transform.

# In[411]:


from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# 1. Identificar columnas numéricas y categóricas (después de ingeniería)

numeric_features = [
    'Age', 'BMI', 'Systolic BP', 'Diastolic BP', 
    'Total Cholesterol (mg/dL)', 'HDL (mg/dL)', 
    'Fasting Blood Sugar (mg/dL)', 'Waist-to-Height Ratio',
    'Abdominal Circumference (cm)',
]

categorical_features = [
    'Sex', 'Smoking Status', 'Diabetes Status', 
    'Physical Activity Level', 'Family History of CVD', 'Blood Pressure Category'
]

# Asegurarse de que solo existan las que están en X_train
numeric_features = [col for col in numeric_features if col in X_train_m2.columns]
categorical_features = [col for col in categorical_features if col in X_train_m2.columns]

# 2. Preprocesadores
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),   # imputación avanzada
    ('scaler', StandardScaler()),               # escala
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(drop='first', handle_unknown='ignore'))
])

# 3. ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ],
    remainder='drop'  # ignora columnas no especificadas
)


# In[412]:


from sklearn.pipeline import Pipeline

pipeline_limpieza_m2 = Pipeline(steps=[
    ("clip_medico", clipper_m2),
    ("imputar_age", age_m2),
    ("imputar_bp", bp_m2),
    ("imputar_peso_altura_bmi", whb_m2),
    ("imputar_lipidos", lipidos_m2),
    ("imputar_azucar", azucar_m2),
    ("recalcular_bmi", bmi_m2),
    ("recalcular_wthr", wthr_m2),
    ("dropper_m2", dropper_m2),
    ("preprocessor", preprocessor)
])


# In[413]:


from sklearn import set_config
set_config(display="diagram")

pipeline_limpieza_m2


# In[414]:


from sklearn.linear_model import Ridge

# Predicciones y métricas igual

# 4. Pipeline completo
model_pipe = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# 5. Entrenar
model_pipe.fit(X_train_m2, y_train_m2)

# 6. Predicciones
y_pred_train = model_pipe.predict(X_train_m2)
y_pred_test  = model_pipe.predict(X_test_m2)

# 7. Métricas
print("Métricas en TRAIN")
print("RMSE:", np.sqrt(mean_squared_error(y_train_m2, y_pred_train)))
print("MAE: ", mean_absolute_error(y_train_m2, y_pred_train))
print("R²:  ", r2_score(y_train_m2, y_pred_train))

print("\nMétricas en TEST")
print("RMSE:", np.sqrt(mean_squared_error(y_test_m2, y_pred_test)))
print("MAE: ", mean_absolute_error(y_test_m2, y_pred_test))
print("R²:  ", r2_score(y_test_m2, y_pred_test))

