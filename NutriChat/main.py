import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# --- Configuração Inicial ---

st.set_page_config(page_title="NutriChat", page_icon="🍎")

st.title("🤖 NutriChat: Seu Assistente Nutricional")
st.caption("Um projeto de chatbot nutricional baseado em IA com OpenAI")

try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    st.error("Chave da API da OpenAI não encontrada ou inválida no arquivo .env")
    st.info("Verifique seu arquivo .env e a chave OPENAI_API_KEY.")
    st.stop()

tab1, tab2, tab3 = st.tabs(["💡 Dicas Rápidas", "🍽️ Gerador de Cardápio Simples", "🔬 Análise de Alimentos"])

# --- Aba 1: Dicas Nutricionais ---
with tab1:
    st.header("Tire suas dúvidas sobre nutrição")
    
    user_question = st.text_input("Ex: 'Qual a importância da proteína no café da manhã?'")

    if st.button("Perguntar"):
        if user_question:
            with st.spinner("Pensando..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": "Você é um nutricionista profissional."},
                            {"role": "user", "content": user_question}
                        ]
                    )
                    answer = response.choices[0].message.content
                    
                    st.write("### Resposta do NutriChat:")
                    st.markdown(answer)

                except Exception as e:
                    st.error(f"Ocorreu um erro ao processar sua pergunta: {e}")
        else:
            st.warning("Por favor, digite uma pergunta.")

# --- Aba 2: Gerador de Cardápio Simples ---
with tab2:
    st.header("Crie um plano alimentar simplificado")

    objetivo = st.selectbox(
        "Qual é o seu principal objetivo?",
        ["Manter o peso (saudável)", "Emagrecer", "Ganhar massa muscular (Hipertrofia)"]
    )

    preferencia = st.selectbox(
        "Você tem alguma preferência alimentar?",
        ["Nenhuma", "Vegetariana", "Vegana", "Low Carb", "carnívora"]
    )
    
    restricao = st.selectbox(
    "Você tem alguma restrição alimentar?",
    ["Nenhuma", "Intolerância à lactose", "Alergia ao glúten", "Diabetes", "Alergia a frutos do mar"]
    )

    if 'cardapio_gerado' not in st.session_state:
        st.session_state.cardapio_gerado = ""

    if st.button("Gerar Cardápio"):
        prompt_cardapio = f"""
        Crie um exemplo de plano alimentar para um dia (café da manhã, almoço e jantar) para uma pessoa com o seguinte perfil:
        - Objetivo: {objetivo}
        - Preferência alimentar: {preferencia}
        - Restrição Alimentar: {restricao}
        Apresente o plano de forma organizada e com sugestões de alimentos simples e acessíveis.
        """
        
        with st.spinner("Criando seu plano alimentar..."):
            try:
                response_cardapio = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Você é um nutricionista experiente na criação de planos alimentares."},
                        {"role": "user", "content": prompt_cardapio}
                    ]
                )
                # Armazena o resultado no session_state
                st.session_state.cardapio_gerado = response_cardapio.choices[0].message.content
            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar o cardápio: {e}")
                st.session_state.cardapio_gerado = ""

    # --- Seção de Exibição e Download ---
    # Só exibe esta parte se um cardápio já foi gerado
    if st.session_state.cardapio_gerado:
        st.write("### Sugestão de Cardápio para um dia:")
        st.markdown(st.session_state.cardapio_gerado)
        
        st.write("---")
        
        # Botão de download único para TXT
        st.download_button(
            label="Salvar como TXT",
            data=st.session_state.cardapio_gerado.encode('utf-8'),
            file_name="cardapio.txt",
            mime="text/plain"
        )

with tab3:
    st.header("Analise a tabela nutricional de um alimento")
    
    nome_do_alimento = st.text_input("Digite o nome de um alimento:")

    if st.button("Analisar Alimento"):
        if nome_do_alimento:
            prompt_analise = f"""
            Analise o alimento '{nome_do_alimento}'. Forneça as seguintes informações em tópicos:
            - Informações nutricionais (calorias, proteínas, carboidratos, gorduras por 100g).
            - Prós e contras do consumo.
            - Sugestões de substituições saudáveis, se aplicável.
            """
            
            with st.spinner("Analisando..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": "Você é um nutricionista profissional."},
                            # O conteúdo enviado para a IA deve ser o 'prompt_analise'
                            {"role": "user", "content": prompt_analise}
                        ]
                    )
                    analise_result = response.choices[0].message.content
                    
                    # Exibe o resultado na tela
                    st.write(f"### Análise do Alimento: {nome_do_alimento.title()}")
                    st.markdown(analise_result)

                except Exception as e:
                    st.error(f"Ocorreu um erro ao processar sua análise: {e}")
        else:
            # Mensagem de aviso se o campo estiver vazio
            st.warning("Por favor, digite o nome de um alimento para analisar.")


