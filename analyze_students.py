#!/usr/bin/env python3
"""
Student Data Analysis Script
============================

This script provides a comprehensive analysis of student performance data,
answering key questions about academic performance and factors influencing success.

Usage:
    python analyze_students.py

Author: Jesús David Silva Rangel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from scipy import stats
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Configuration
warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (12, 8)

def load_data(filepath='data/students_data.csv'):
    """Load and validate the student dataset."""
    try:
        df = pd.read_csv(filepath)
        print(f"✅ Dataset loaded successfully: {df.shape[0]} students, {df.shape[1]} variables")
        return df
    except FileNotFoundError:
        print("❌ Error: Dataset file not found. Please ensure 'data/students_data.csv' exists.")
        return None
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

def analyze_data_quality(df):
    """Perform data quality analysis."""
    print("\n" + "="*60)
    print("DATA QUALITY ANALYSIS")
    print("="*60)
    
    print(f"Dataset shape: {df.shape}")
    print(f"Missing values: {df.isnull().sum().sum()}")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    print(f"Data types:\n{df.dtypes.value_counts()}")
    
    return df.isnull().sum().sum() == 0

def answer_research_questions(df):
    """Answer the 5 key research questions."""
    
    subject_columns = ['Algebra', 'Calculus1', 'Calculus2', 'Statistics', 
                      'Probability', 'Measure', 'Functional_analysis']
    
    print("\n" + "="*60)
    print("RESEARCH QUESTIONS ANALYSIS")
    print("="*60)
    
    # Question 1: Factors influencing performance
    print("\n1️⃣  FACTORS INFLUENCING STUDENT PERFORMANCE:")
    print("-" * 50)
    
    correlations = df[subject_columns + ['Attendance']].corrwith(df['GPA']).sort_values(ascending=False)
    print("Top factors (correlation with GPA):")
    for i, (factor, corr) in enumerate(correlations.head(5).items(), 1):
        print(f"   {i}. {factor}: {corr:.3f}")
    
    # Question 2: Best subjects
    print("\n2️⃣  SUBJECTS BEST MASTERED BY STUDENTS:")
    print("-" * 45)
    
    best_subjects = df[subject_columns].mean().sort_values(ascending=False)
    print("Top performing subjects:")
    for i, (subject, score) in enumerate(best_subjects.head(3).items(), 1):
        print(f"   {i}. {subject}: {score:.2f}")
    
    # Question 3: Worst subjects
    print("\n3️⃣  SUBJECTS WITH LOWEST PERFORMANCE:")
    print("-" * 42)
    
    worst_subjects = df[subject_columns].mean().sort_values(ascending=True)
    print("Subjects needing attention:")
    for i, (subject, score) in enumerate(worst_subjects.head(3).items(), 1):
        print(f"   {i}. {subject}: {score:.2f}")
    
    # Question 4: GPA analysis
    print("\n4️⃣  GPA ANALYSIS AND INFLUENCING FACTORS:")
    print("-" * 45)
    
    gpa_stats = {
        'Mean': df['GPA'].mean(),
        'Median': df['GPA'].median(),
        'Std Dev': df['GPA'].std(),
        'Min': df['GPA'].min(),
        'Max': df['GPA'].max()
    }
    
    print("GPA Statistics:")
    for stat, value in gpa_stats.items():
        print(f"   {stat}: {value:.2f}")
    
    # Question 5: Gender performance
    print("\n5️⃣  PERFORMANCE BY GENDER:")
    print("-" * 32)
    
    gender_stats = df.groupby('gender')['GPA'].agg(['count', 'mean', 'std']).round(2)
    print("Gender performance comparison:")
    print(gender_stats)
    
    # Statistical test for gender difference
    female_gpa = df[df['gender'] == 'female']['GPA']
    male_gpa = df[df['gender'] == 'male']['GPA']
    t_stat, p_value = stats.ttest_ind(female_gpa, male_gpa)
    
    print(f"\nStatistical significance test:")
    print(f"   T-statistic: {t_stat:.3f}")
    print(f"   P-value: {p_value:.3f}")
    print(f"   Significant difference: {'Yes' if p_value < 0.05 else 'No'} (α=0.05)")

def create_predictive_model(df):
    """Create and evaluate a predictive model for GPA."""
    print("\n" + "="*60)
    print("PREDICTIVE MODEL ANALYSIS")
    print("="*60)
    
    # Prepare data
    subject_columns = ['Algebra', 'Calculus1', 'Calculus2', 'Statistics', 
                      'Probability', 'Measure', 'Functional_analysis']
    
    df_model = df.copy()
    
    # Encode categorical variables
    le_gender = LabelEncoder()
    df_model['gender_encoded'] = le_gender.fit_transform(df_model['gender'])
    
    le_from1 = LabelEncoder()
    df_model['from1_encoded'] = le_from1.fit_transform(df_model['from1'])
    
    features = subject_columns + ['Attendance', 'gender_encoded', 'from1_encoded']
    X = df_model[features]
    y = df_model['GPA']
    
    # Train model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print(f"Model Performance:")
    print(f"   R² Score: {r2:.3f}")
    print(f"   RMSE: {rmse:.3f}")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'Feature': features,
        'Coefficient': model.coef_,
        'Abs_Coefficient': np.abs(model.coef_)
    }).sort_values('Abs_Coefficient', ascending=False)
    
    print(f"\nTop 5 Most Important Factors:")
    for i, (_, row) in enumerate(feature_importance.head(5).iterrows(), 1):
        print(f"   {i}. {row['Feature']}: {row['Coefficient']:.3f}")

def generate_recommendations(df):
    """Generate actionable recommendations based on analysis."""
    print("\n" + "="*60)
    print("RECOMMENDATIONS")
    print("="*60)
    
    subject_columns = ['Algebra', 'Calculus1', 'Calculus2', 'Statistics', 
                      'Probability', 'Measure', 'Functional_analysis']
    
    # Identify areas for improvement
    worst_subjects = df[subject_columns].mean().sort_values(ascending=True)
    best_subjects = df[subject_columns].mean().sort_values(ascending=False)
    avg_attendance = df['Attendance'].mean()
    
    print("\n🎯 FOR EDUCATIONAL INSTITUTIONS:")
    print(f"1. Focus on improving {worst_subjects.index[0]} (avg: {worst_subjects.iloc[0]:.1f})")
    print(f"2. Use {best_subjects.index[0]} as a model (avg: {best_subjects.iloc[0]:.1f})")
    print(f"3. {'Maintain' if avg_attendance > 90 else 'Improve'} attendance rates (current: {avg_attendance:.1f}%)")
    
    gender_diff = df.groupby('gender')['GPA'].mean().diff().iloc[1]
    if abs(gender_diff) > 2:
        print(f"4. Address gender performance gap ({abs(gender_diff):.1f} points)")
    else:
        print("4. Continue promoting gender equality in education")
    
    print("\n📚 FOR STUDENTS:")
    print("1. Maintain consistent attendance (strong correlation with GPA)")
    print(f"2. Seek extra help in {worst_subjects.index[0]} and {worst_subjects.index[1]}")
    print(f"3. Build on strengths in {best_subjects.index[0]} and {best_subjects.index[1]}")
    print("4. Participate in study groups and peer tutoring")

def main():
    """Main analysis function."""
    print("🎓 STUDENT DATA ANALYSIS PROJECT")
    print("="*60)
    print("Analyzing student performance data using CRISP-DM methodology")
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    # Perform analyses
    data_quality_ok = analyze_data_quality(df)
    if not data_quality_ok:
        print("⚠️  Warning: Data quality issues detected. Results may be affected.")
    
    answer_research_questions(df)
    create_predictive_model(df)
    generate_recommendations(df)
    
    print("\n" + "="*60)
    print("✅ ANALYSIS COMPLETED SUCCESSFULLY!")
    print("="*60)
    print("📊 Summary:")
    print(f"   • {len(df)} students analyzed")
    print(f"   • {len(df.columns)} variables examined")
    print(f"   • 5 research questions answered")
    print(f"   • Predictive model created")
    print(f"   • Actionable recommendations provided")
    print("\n🚀 For interactive analysis, use the Jupyter notebook: student-data-analysis.ipynb")

if __name__ == "__main__":
    main()