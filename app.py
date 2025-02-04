# streamlit_app/app.py
import streamlit as st
import pandas as pd
from db_utils import get_recent_data, create_table_if_not_exists

st.title("HVAC IoT MVP - Dashboard")

# On s'assure que la table existe
create_table_if_not_exists()

# Bouton pour rafraîchir les données
if st.button("Rafraîchir"):
    data = get_recent_data(limit=50)
    df = pd.DataFrame(data, columns=["sensor_id", "value", "timestamp"])
    st.dataframe(df)

    # Petit graphe
    if not df.empty:
        st.line_chart(df[['value']])
