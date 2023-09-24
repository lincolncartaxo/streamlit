
import pandas as pd
import streamlit as st

#Conexão - Banco de Dados
conn = st.experimental_connection('crud_python', type='sql')
with conn.session as s:
    
#Sidebar
    
    option=st.sidebar.selectbox("Selecione a operação:",("Ler"))

#Sidebar
st.title("CRUD - Lincoln Cartaxo")

   # st.subheader("Ler Registro")
   # s.execute("select * from cliente")
   # result = mycursor.fetchall() #ler o banco de dados
    #for row in result:
    #    st.write(row)

  #  df = pd.DataFrame(result,columns=['ID','NOME','IDADE','PROFISSÃO'])
  #  df = st.data_editor(df,hide_index=True,num_rows="dynamic", key="data_editor")
  #  st.write("Here's the session state:")
  #  st.write(st.session_state["data_editor"]) # 👈 Access the edited data

