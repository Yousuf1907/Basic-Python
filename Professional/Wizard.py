import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

df = None

st.set_page_config(
    page_title="Data Visualization and ML App",
    page_icon=":bar_chart:"
)

st.title("Data Visualization and ML App")

st.sidebar.header("Settings")

db_settings = st.sidebar.selectbox("Select Database", ["CSV", "SQLite"])
if db_settings == "CSV":
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
else:
    db_path = st.sidebar.text_input("Enter SQLite database path", "example.db")
    engine = create_engine(f"sqlite:///{db_path}")

    table_list = engine.table_names()  #Fetching tables from database
    selected_table = st.sidebar.selectbox("Select a table", table_list)

    df = pd.read_sql(selected_table, con=engine)

    st.subheader("Raw Data")
    st.write(df)

st.sidebar.subheader("Data Visualization")

chart_type = st.sidebar.selectbox("Select a chart type", ["Bar Chart", "Histogram", "Scatter Plot", "Line Chart", "Area Chart", "Pie Chart", "Radar Chart", "3D Scatter Plot", "Map Plot", "Heatmap"])  # Box plot (Not working)

# ... (your data visualization code)

# Clear the dataset button
 

# Now, in the machine learning section, you can access the global df variable
st.sidebar.subheader("Machine Learning")

if df is not None:
    target_column = st.sidebar.selectbox("Select the target column", df.columns)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Decision Tree Classifier
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Display model performance metrics
    st.subheader("Model Performance Metrics")
    st.write("Accuracy:", accuracy_score(y_test, y_pred))
    st.write("Classification Report:\n", classification_report(y_test, y_pred))
else:
    st.sidebar.warning("Please upload a CSV file or connect to a database to perform machine learning.")

# ... (continue with the rest of your Streamlit app)
