import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.title("QR Code Data")

combine_floors = st.checkbox("Combine Floors?")

time = st.selectbox(
    "Select Time Period",
    ["One Week", "One Month", "Two Months", "All Time"],
    index=None,
    placeholder="Choose a time period..."
)


if time is None:
    st.info("Select a time period to load the dashboard.")
    st.stop()
if time == "One Week":
    if not combine_floors:
        data = pd.read_csv("one_week.csv")
    else:
        data = pd.read_csv("one_week_noFloor.csv")

elif time == "One Month":
    if not combine_floors:
        data = pd.read_csv("one_month.csv")
    else:
        data = pd.read_csv("one_month_noFloor.csv")

elif time == "Two Months":
    if not combine_floors:
        data = pd.read_csv("two_months.csv")
    else:
        data = pd.read_csv("two_months_noFloor.csv")

elif time == "All Time":
    if not combine_floors:
        data = pd.read_csv("full_data.csv")
    else:
        data = pd.read_csv("full_data_noFloor.csv")

counts = data['Location'].value_counts().reset_index()

counts.columns = ["Location", "Count"]

top_n = st.slider("Show top N locations", 5, 50, 15)
counts = counts.head(top_n)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=counts, y="Location", x="Count", ax=ax)

ax.set_title(f"Top {top_n} Locations by Check-ins")
ax.set_xlabel("Num of Scans")
ax.set_ylabel("Location")
plt.tight_layout()

st.pyplot(fig)






