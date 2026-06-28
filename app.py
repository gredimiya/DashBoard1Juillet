import streamlit as st
import datetime as dt
from math import e
import plotly.graph_objects as go
import pandas as pd

def data():
    l=[{
        "jour": dt.datetime.strptime("30/05/2026", "%d/%m/%Y").date(),
        "niveau_d_amour": 100
    },
    {
        "jour": dt.datetime.strptime("31/05/2026", "%d/%m/%Y").date(),
        "niveau_d_amour": 110
    }
    ]
    for i in range(1, 31):
        l.append({
            "jour": dt.datetime.strptime(f"{i:02d}/06/2026", "%d/%m/%Y").date(),
            "niveau_d_amour": l[-1]["niveau_d_amour"] + 30 * e ** (0.1 * i)
        })
    return l

def main():
    st.set_page_config(page_title="Bilan d'amour", page_icon="❤️", layout="wide")

    col1, col2 = st.columns(2)

    with st.container():
        with col1:
            st.header("❤️ Bilan de mon amour pour Violette ❤️")
            st.subheader("Ceci est un bilan de mon amour pour toi après 1 mois ensemble.")
            ## Filtre
            st.subheader("Cette page n'as pas de filtre car j'aime tout de toi")
        with col2:
            st.image("source\Hamster.jpg")

    with st.container():
        ## Evolution de l'amour au fil des jours
        with col1:
            with st.container(border=True):
                st.title("Voici l'évolution de mon amour pour toi au fil des jours :")
                l = data()
                ligne = go.Figure()
                ligne.add_trace(go.Scatter(x=[item["jour"] for item in l], y=[item["niveau_d_amour"] for item in l], mode='lines'))
                ligne.update_layout(yaxis=dict(visible=False, range=[0, max(item["niveau_d_amour"] for item in l) + 10]), xaxis_title="Jour", yaxis_title="Niveau d'amour")
                st.plotly_chart(ligne)

        ## Jauge d'amour
        with col2:
            with st.container(border=True):
                st.title("Voici une jauge de mon amour pour toi :")
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = 125,
                    title = {'text': "Pourcentage d'amour"},
                    number = {'suffix': "%"},
                    gauge = {'axis': {'range': [0, 100]},
                            'bar': {'color': "red"},
                            }))
                st.plotly_chart(fig)
    
    with st.container():
         with col1:
            with st.container(border=True):
                st.title("Carte des points importants en France")
                ## coordonée 45°36'31.5"N 5°09'11.3"E
                df = pd.DataFrame({
                    'lat': [45.60875],
                    'lon': [5.15314]
                })
                st.map(df, zoom=5)


if __name__ == "__main__":
    main()
