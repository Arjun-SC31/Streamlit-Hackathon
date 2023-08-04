from connection import KaggleDatasetConnection
import streamlit as st
st.set_page_config(page_title="Kaggle-Streamlit Connection Demo App")
st.title("Kaggle-Streamlit Connector App")
st.info(
    "This is a demo app that presents basic use of custom Kaggle-Streamlit connector built using ExperimentalBaseConnection"
)
st.subheader("Loading dataset from Kaggle Through API")
conn = st.experimental_connection("kaggle_datasets", type=KaggleDatasetConnection)
dataset_path = st.text_input(
    "Kaggle Link Of Dataset", "varsharam/walmart-sales-dataset-of-45stores"
)
file_list = ""
if dataset_path.count("/") == 1:
    owner, dataset = dataset_path.split("/")
    try:
        file_list = conn.list(path=dataset_path, ttl=3600)
        st.json(file_list)
    except Exception as e:
        st.error(f"Oops...{e.__class__}")
if file_list:
    dataset_name = st.text_input(
        "Kaggle Dataset Name", file_list[0]
    ).replace("\"","")
    if dataset_name:
        if st.button("Load Data"):
            try:
                df = conn.get(path=dataset_path, filename=dataset_name, ttl=3600)
                st.write(f"{dataset_name} preview")
                st.dataframe(df.head(20))
            except Exception as e:
                st.error(f"Oops...{e.__class__}")
