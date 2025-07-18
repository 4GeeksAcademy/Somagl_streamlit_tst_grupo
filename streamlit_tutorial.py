import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def main():
    st.title('Bienvenido a tu guía virtual para alinear tus Chakras')
    st.write('**Por favor seleccione el servicio predictivo que desea utilizar**')
    
    opcion = st.radio('Seleccione el servicio:', 
                      ('Predicción en base al zodiaco (csv)', 'Predicción en base al zodiaco (manualmente)', 'Predicción de imagen','Maqueta','Sliders'), 
                      index=0, 
                      key='option')
    
    if st.button('Empezar!'):
        route_prediction(opcion)

def route_prediction(opcion):
    if opcion == 'Predicción en base al zodiaco (csv)':
        switch_page("pred_iris_csv")
    elif opcion == 'Predicción en base al zodiaco (manualmente)':
        switch_page("pred_iris_man")
    elif opcion == 'Predicción de imagen':
        switch_page("pred_imagen")
    elif opcion == 'Maqueta':
        switch_page("maqueta")
    elif opcion == 'Sliders':
        switch_page("sliders")

if __name__ == "__main__":
    main()

# https://docs.streamlit.io/library/get-started/multipage-apps
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2