import streamlit as st

# Dados de exemplo
genero = ["Forro", "Rap", "Pop", "Pagode"]

# Dicionário relacionando gêneros aos seus livros
musica_por_genero = {
    "Forro": ["Hoje Dói", "Acaso", "Vou Te Amar"],
    "Rap": ["A Vida é Um Desafio", "Canâo Foi Tâo Bom", "O 5° Vigia"],
    "Pop": ["God's Plan", "Billie Jean", "It Was a Good Day"],
    "Pagode": ["Camisa 10", "Quem Ama Sente Saudade", "É Tarde Demais"]
}

# Selectbox para escolher o gênero                
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", genero)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    musica_selecionada = st.sidebar.selectbox(
        "Selecione a música:", 
        musica_por_genero[genero_selecionado]
    )

# Mostrar apenas o livro selecionado
if genero_selecionado and musica_selecionada:
    st.write(f"**Música selecionada:** {musica_selecionada}")
    st.write(f"**Gênero:** {genero_selecionado}")
    

if genero_selecionado == "Forro" and musica_selecionada == "Hoje Dói":
    st.markdown("Uma balada emocional do Forró do Sócio, 'Hoje Dói' fala sobre a dor de um amor perdido. A letra retrata a tentativa de lidar com a saudade e a mágoa, com versos que expressam vulnerabilidade e arrependimento.")
    st.write("A SEGUIR O LINK DA MÚSICA ESCOLHIDA, SE DIVIRTA OUVINDO 🎶😎")    
    st.video("https://youtu.be/vEIzaCtd11E?si=3nSbhnSdWmHaGre1")

elif genero_selecionado == "Forro" and musica_selecionada == "Acaso":
    st.markdown("Com uma pegada poética, 'Acaso' do Forróçacana explora os encontros inesperados da vida. A música celebra o destino e a beleza das coincidências que unem duas pessoas, com uma melodia suave e envolvente.")
    st.write("A SEGUIR O LINK DA MÚSICA ESCOLHIDA, SE DIVIRTA OUVINDO 🎶😎")
    st.video("https://youtu.be/1v_-9n-QDyY?si=VkSsYENLhY-r36KH")

elif genero_selecionado == "Forro" and musica_selecionada == "Vou Te Amar":
    st.markdown("Romântica e esperançosa, 'Vou Te Amar' mistura elementos de forró com declarações de amor eterno. A letra fala sobre encontros predestinados e o desejo de viver um amor verdadeiro, embalado por uma melodia contagiante.")
    st.write("A SEGUIR O LINK DA MÚSICA ESCOLHIDA, SE DIVIRTA OUVINDO 🎶😎")
    st.video("https://youtu.be/8z8kmBgdj2k?si=n6t0WGlYLhBlBwv7")


elif genero_selecionado == "Rap" and musica_selecionada == "A Vida é Um Desafio":
    st.markdown("Clássico dos Racionais MC's, essa música é uma reflexão profunda sobre os desafios enfrentados na periferia. Com letras que abordam sonhos, escolhas difíceis e a luta contra o sistema, 'A Vida é Um Desafio' inspira coragem e resistência.")
    st.write("A SEGUIR O LINK DA MÚSICA ESCOLHIDA, SE DIVIRTA OUVINDO 🎶😎")
    st.video("https://youtu.be/7v7mwrGJBf0?si=sP9p1f5SyEnqB2hK")

elif genero_selecionado == "Rap" and musica_selecionada == "Canâo Foi Tâo Bom":
    st.markdown("Sabotage transforma memórias do bairro do Canão em uma homenagem à comunidade. A música mistura crítica social com nostalgia, exaltando a força da periferia e a importância da educação e da cultura como formas de resistência.")
    st.write("A SEGUIR O LINK DA MÚSICA ESCOLHIDA, SE DIVIRTA OUVINDO 🎶😎")
    st.video("https://youtu.be/WF7LLl7r4Os?si=NY1rc534Vgfy7SwW")

elif genero_selecionado == "Rap" and musica_selecionada == "O 5° Vigia":
    st.markdown("Narrativa intensa de Ndee Naldinho, 'O 5° Vigia' descreve os bastidores de um assalto a banco. Com influência do gangsta rap, a música se tornou um marco do rap nacional nos anos 2000, destacando a realidade urbana e a tensão constante vivida nas ruas.")
    st.write("A SEGUIR O LINK DA MÚSICA ESCOLHIDA, SE DIVIRTA OUVINDO 🎶😎")
    st.video("https://youtu.be/N8TN4Rj4kb0?si=6IUHc7PDc02Qo9QJ")    

elif genero_selecionado == "Pop" and musica_selecionada == "God's Plan":
    st.markdown("Drake celebra a gratidão e a proteção divina em 'God's Plan'. A música mistura trap e pop rap, com uma mensagem positiva sobre superar dificuldades e ajudar os outros, tornando-se um dos maiores sucessos do artista.")
    st.write("A SEGUIR O LINK DA MÚSICA ESCOLHIDA, SE DIVIRTA OUVINDO 🎶😎")
    st.video("https://youtu.be/9TincgwjtmA?si=AKobPrI95HlI-OJd")

elif genero_selecionado == "Pop" and musica_selecionada == "Billie Jean":
    st.markdown("Um dos maiores hits de Michael Jackson, 'Billie Jean' combina funk, R&B e dance-pop. A letra gira em torno de uma acusação de paternidade, enquanto a produção inovadora e o icônico moonwalk marcaram a história da música pop.")
    st.write("A SEGUIR O LINK DA MÚSICA ESCOLHIDA, SE DIVIRTA OUVINDO 🎶😎")
    st.video("https://youtu.be/OZGtRvYF-A4?si=lQ6EILCkrDekTRSX")

elif genero_selecionado == "Pop" and musica_selecionada == "It Was a Good Day":
    st.markdown("Ice Cube retrata um raro dia de paz em meio à violência urbana de Los Angeles. 'It Was a Good Day' é uma celebração da tranquilidade, onde tudo corre bem e não há necessidade de recorrer à violência — um alívio na rotina tensa da periferia.")
    st.write("A SEGUIR O LINK DA MÚSICA ESCOLHIDA, SE DIVIRTA OUVINDO 🎶😎")
    st.video("https://youtu.be/OFq5nGCoOVc?si=QgRJ1DtdcgEv7rm-")

elif genero_selecionado == "Pagode" and musica_selecionada == "Camisa 10":
    st.markdown("Camisa 10")
    st.write("Essa música é uma declaração de amor incondicional. O eu lírico compara conquistas grandiosas, como ser o camisa 10 do Barcelona ou ganhar na Mega-Sena, com a felicidade de estar ao lado da pessoa amada. Mesmo com fama e riqueza, ele escolhe o amor verdadeiro. A letra usa metáforas exageradas para reforçar a lealdade e o valor do sentimento.")
    st.video("https://www.youtube.com/watch?v=oZgYN4qfpl4")

elif genero_selecionado == "Pagode" and musica_selecionada == "Quem Ama Sente Saudade":
    st.markdown("Quem Ama Sente Saudade")
    st.write("Essa canção expressa a dor da saudade e os conflitos de um relacionamento marcado por ciúmes e inseguranças. O eu lírico revela que, apesar de ter perdoado a pessoa amada, ainda sente tristeza e desconfiança. A música destaca como o amor verdadeiro é acompanhado por saudade intensa e preocupação constante.")
    st.video("https://youtu.be/PQqOSqHZOTc?si=Ftowha2R0ETtfnlx")

elif genero_selecionado == "Pagode" and musica_selecionada == "É Tarde Demais":
    st.markdown("É Tarde Demais")
    st.write("A música retrata um relacionamento que não resistiu às pressões externas e à falta de confiança. O eu lírico lamenta que o amor verdadeiro não foi valorizado e que a separação foi causada por interferências de terceiros. Agora, mesmo com arrependimento da outra parte, ele afirma que é tarde demais para voltar atrás.")
    st.video("https://youtu.be/mZK0m7jMlZA?si=JDLeWD34dMK7ajeU")