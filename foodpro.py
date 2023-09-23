import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

df = pd.read_excel('食品營養成分資料庫2022版.xlsx' , usecols='B, C, G, J, K, N, O, P, W')

def highlight_protein(val):
    if val > 15: return 'background-color: yellow'
    else: return ''
def highlight_fat(val):
    if val > 17.5: return 'color: red'
    else: return ''

st.set_page_config(layout="wide")

st.subheader("食品營養成分查詢 / 單位每100g")
with st.form('search_form'):
    foodname = st.text_input('輸入食品名稱')
    isHighProtein = st.checkbox('高蛋白食物標記(>15g/100g)')
    isHighFat = st.checkbox('高脂肪(>17.5g/100g)')
    submitted = st.form_submit_button('查詢')
    if submitted:
        result = df.query("食品名稱.str.contains(@foodname)")
        if isHighProtein and isHighFat:
            result = result.style.map(highlight_protein, subset='粗蛋白(g)').map(highlight_fat, subset='粗脂肪(g)')
        else:
            if isHighProtein:
                result = result.style.map(highlight_protein, subset='粗蛋白(g)')
            if isHighFat:
                result = result.style.map(highlight_fat, subset='粗脂肪(g)')
        st.write(result)