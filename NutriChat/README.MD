# 🍎 NutriChat: Seu Assistente Nutricional com IA

![Streamlit Badge](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![OpenAI Badge](https://img.shields.io/badge/OpenAI-GPT--4o--mini-000000)
![Python Badge](https://img.shields.io/badge/Python-3.x-3776AB)

Um projeto de chatbot nutricional interativo construído com **Streamlit** e a **API da OpenAI**. O NutriChat atua como um assistente virtual, oferecendo dicas, gerando planos alimentares simplificados e analisando alimentos.

---

## ✨ Funcionalidades

O aplicativo é dividido em três abas principais, cada uma com um propósito nutricional específico:

### 1. 💡 Dicas Rápidas
* Permite ao usuário fazer qualquer pergunta sobre nutrição (Ex: "Qual a importância da proteína no café da manhã?").
* O chatbot responde utilizando a inteligência do modelo `gpt-4o-mini`, atuando como um nutricionista profissional.

### 2. 🍽️ Gerador de Cardápio Simples
* Cria um exemplo de plano alimentar para um dia (café da manhã, almoço e jantar).
* Geração personalizada com base no **Objetivo** (Manter peso, Emagrecer, Ganhar massa), **Preferencia** (Vegetariana, Vegana, Low Carb, etc.) e **Restrição** (Alergia, Intolerância, etc.).
* Permite salvar o cardápio gerado em um arquivo `.txt`.

### 3. 🔬 Análise de Alimentos
* Permite ao usuário digitar o nome de um alimento.
* A IA retorna uma análise completa, incluindo:
    * Informações Nutricionais (calorias, proteínas, etc. por 100g).
    * Prós e Contras do consumo.
    * Sugestões de substituições saudáveis.

---

## 💻 Pré-requisitos

Para rodar este projeto localmente, você precisará ter instalado:

* **Python 3.x**
* Uma chave de API válida da **OpenAI**.

## ⚙️ Instalação e Uso

Siga os passos abaixo no seu terminal (Git Bash, CMD, etc.):

### 1. Clonar o Repositório

```bash
git clone [https://github.com/IsabeladeLima/agent-orchestration-lab.git](https://github.com/IsabeladeLima/agent-orchestration-lab.git)
cd agent-orchestration-lab
```

### 2. Configurar o Ambiente

É altamente recomendado o uso de um ambiente virtual (`venv` ou `conda`).

```bash
# Cria um ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Windows)
.\venv\Scripts\activate

# (Opcional) Ativa o ambiente virtual (Linux/macOS)
# source venv/bin/activate
```

### 3. Instalar Dependências
Instale as bibliotecas necessárias listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Configurar a Chave da API
Crie um arquivo chamado .env na raiz do projeto e insira sua chave da OpenAI, conforme o código espera:

OPENAI_API_KEY="SUA_CHAVE_AQUI"

Lembre-se: O arquivo ´.env´ _deve estar listado no .gitignore para não ser enviado ao GitHub._

### 5. Rodar o Aplicativo
Execute o aplicativo usando o Streamlit:

```bash
streamlit run main.py
```

### Autor:
*Isabela de Lima* - [GitHub Profile](https://github.com/IsabeladeLima)
