import streamlit as st
import pandas as pd
from assortment_search import run_assort_search
from attract_tourism import run_at
from checkspam_app import run_checkspam
from draw_map import run_draw_map
from area_search import run_area_search
from name_search import run_name_search

def main() :
    
    choice = st.sidebar.selectbox('검색선택',['국내 관광 명소', 'CCTV 설치와 안전벨 관계', 'SPAM 문자 확인'])

    if choice == '국내 관광 명소' :
        run_at()
    elif choice == 'SPAM 문자 확인' :
        run_checkspam()
    elif choice == 'CCTV 설치와 안전벨 관계' :
        pass
        
    
if __name__ == '__main__' : main()