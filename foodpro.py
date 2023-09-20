import streamlit as st
import pandas as pd

df = pd.read_excel('食品營養成分資料庫2022版.xlsx' , usecols='B, C, G, J, K, N, O, P, W')

# Define a function to apply the background color based on a condition
def highlight_above_fifteen(val):
    if val > 15: return 'background-color: yellow'
    else: return ''

st.set_page_config(layout="wide")
col1, col2 = st.columns([3,2])

with col1:
    st.subheader("食品營養成分查詢 / 單位每100g")
    with st.form('search_form'):
        foodname = st.text_input('輸入食品名稱')
        isHighProtein = st.checkbox('高蛋白食物標記(>15g/100g)')
        isHighFat = st.checkbox('高脂肪(>17.5g/100g)')

        submitted = st.form_submit_button('查詢')
        if submitted:
            if isHighProtein:
                result = df.query("食品名稱.str.contains(@foodname)").style.applymap(highlight_above_fifteen, subset=pd.IndexSlice[:, ['粗蛋白(g)']])
            else: result = df.query("食品名稱.str.contains(@foodname)")
            st.write(result)

with col2:
    st.subheader('營養計算機')


