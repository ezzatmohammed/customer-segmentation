import streamlit as st
import numpy as np
import pandas as pd

# Assuming you have your CSV file in the same directory as the script
df = pd.read_csv("ClusterdData.csv")

def get_Recommendation(User, num_of_recommendation):
    User = int(User)
    Cluster = df[df["User_Id"] == User]["predicted_labels_DBSCAN"].iloc[0]
    df_cluster = df[df["predicted_labels_DBSCAN"] == Cluster]
    df_cluster = df_cluster.groupby("Merchant")["Money_spent"].sum().nlargest(int(num_of_recommendation))
    for index, mer in enumerate(df_cluster.index):
        st.text(f"Recommendation number {index+1} of user {User} is {mer}")

def main():
    st.title("Recommendation App")
    User = st.text_input("Enter User Id")
    num_of_recommendation = st.text_input("Enter num of Rec")
    if st.button("Recommend"):
        if User and num_of_recommendation:
            get_Recommendation(User, num_of_recommendation)
        else:
            st.warning("Please enter User Id and num of Rec.")

if __name__ == "__main__":
    main()
