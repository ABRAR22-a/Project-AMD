# analysis.py
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# تحميل البيانات
df = pd.read_csv("data/financial_data.csv", sep=";")

# تحويل النصوص لأرقام
df["late_payment"] = df["late_payment"].str.strip().str.lower().map({"yes": 1, "no": 0})
df["has_workers"] = df["has_workers"].str.strip().str.lower().map({"yes": 1, "no": 0})
df["housing_status"] = df["housing_status"].str.strip().str.lower().map({"rent": 0, "own": 1})
df["has_dependents"] = df["has_dependents"].str.strip().str.lower().map({"yes": 1, "no": 0})

# حذف أي صف ناقصه تصنيف
df = df.dropna(subset=["financial_distress"])

# حساب المؤشرات
df["expense_ratio"] = df["monthly_expense"] / (df["salary"] + 1)
df["debt_to_income"] = df["debt_amount"] / (df["salary"] + 1)
df["net_balance"] = df[abs("savings_balance")] - df["debt_amount"]

# عرض إحصائيات
print("📊 وصف البيانات:\n", df.describe())

# رسم الرسوم البيانية
plt.figure(figsize=(8, 5))
sns.boxplot(x="financial_distress", y="expense_ratio", data=df)
plt.title("نسبة الصرف مقابل التعثر المالي")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x="financial_distress", y="debt_to_income", data=df)
plt.title("نسبة الديون مقابل التعثر المالي")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x="financial_distress", y="net_balance", data=df)
plt.title("الرصيد الصافي مقابل التعثر المالي")
plt.grid(True)
plt.show()

# حفظ نسخة معالجة
df.to_csv("data/processed_data.csv", index=False)
print("✅ تم حفظ البيانات المعالجة في data/processed_data.csv")
"""