import streamlit as st
import time
# 🏠 Cabeçalho
st.title("🚗 Bem-vindo à RideNow")
st.markdown('<h3 style="color:green;">Sua jornada começa aqui!</h3>', unsafe_allow_html=True)
st.write("Alugue a moto ideal com conforto, segurança e liberdade para ir além.")


# 💬 Depoimentos
st.markdown("💬 “A XJ6 é simplesmente sensacional! Conforto e potência na medida certa.” – Carla, RJ")
st.markdown("💬 “A Z900 me surpreendeu! Estilo e desempenho que chamam atenção por onde passa.” – Bruno, SP")
st.markdown("💬 “Aluguei a Lander 250 para uma trilha e foi perfeita! Estável e muito divertida.” – Letícia, MG")
# Dados dos carros organizados por marca
marcas = {
    "Honda": {
        "Biz": 65,
        "CG 160": 95,
        "Pop 110i": 45,
        "CB 300F Twister": 120,
        "NXR 160 Bros": 85,
    },
    "Kawasaki": {
        "300": 120,
        "Z900": 180,
        "Ninja Zx-6r": 220,
        "Ninja Zx-10r": 280,
        "Z1000": 250,
    },
    "Yamaha": {
        "150 Factor": 65,
        "Crosser 150": 80,
        "Fazer 250": 100,
        "Lander 250": 110,
        "XJ6": 160,
    },
}

descricoes = {
     "Pop 110i": "Modelo compacto e econômico, ideal para deslocamentos urbanos curtos com baixo consumo de combustível.",
    "Biz": "Scooter prática e versátil, perfeita para o dia a dia na cidade com câmbio semiautomático.",
    "NXR 160 Bros": "Moto estilo trail, ótima para terrenos mistos e aventuras leves, com bom desempenho e conforto.",
    "CG 160": "Clássica urbana, confiável e robusta, excelente para trajetos médios e uso diário.",
    "CB 300F Twister": "Esportiva leve com design moderno, indicada para quem busca mais potência e estilo na cidade.",
    "300": "Esportiva leve com visual agressivo, ideal para iniciantes que buscam desempenho e estilo.",
    "Z900": "Naked potente com motor de alto torque, perfeita para quem curte velocidade e presença.",
    "Ninja Zx-6r": "Esportiva média com excelente desempenho em pista e estrada, voltada para pilotos experientes.",
    "Ninja Zx-10r": "Superesportiva de alta performance, indicada para uso profissional e competições.",
    "Z1000": "Naked premium com design marcante e motor poderoso, ideal para quem busca adrenalina e sofisticação.",
    "150 Factor": "Moto urbana econômica e confiável, excelente para o dia a dia e iniciantes.",
    "Crosser 150": "Trail leve com bom desempenho em terrenos mistos, ideal para aventuras urbanas e rurais.",
    "Fazer 250": "Urbana potente com ótimo equilíbrio entre desempenho e conforto, indicada para trajetos médios.",
    "Lander 250": "Trail versátil com suspensão elevada, perfeita para quem busca liberdade em qualquer terreno.",
    "XJ6": "Naked esportiva de alta cilindrada, com visual imponente e excelente desempenho em estrada."
}

# 📞 Contato na barra lateral
st.sidebar.image("logo.png")
st.sidebar.title("📱 Fale Conosco")
st.sidebar.markdown('[WhatsApp](https://wa.me/5511998993067)')

# 🚘 Escolha da marca e do veículo na sidebar
marca_selecionada = st.sidebar.selectbox("Escolha a marca", list(marcas.keys()))
modelos_da_marca = list(marcas[marca_selecionada].keys())
modelo_selecionado = st.sidebar.selectbox("Escolha o modelo", modelos_da_marca)

diaria = marcas[marca_selecionada][modelo_selecionado]

# 🧾 Informações do aluguel
st.header("📋 Detalhes do Aluguel")
# Como a imagem está no formato 'Marca Modelo.png', monta o nome correto
nome_arquivo_img = f"{marca_selecionada} {modelo_selecionado}.png"
st.image(nome_arquivo_img)
st.subheader(f"Modelo selecionado: {marca_selecionada} {modelo_selecionado}")
st.markdown("Atenção ⚠️ — Após ler a descrição, preencha o tempo de aluguel e os Km's para obter o valor final.")

# 📌 Descrição condicional
if modelo_selecionado in descricoes:
    st.markdown(f"📌 **Descrição:** {descricoes[modelo_selecionado]}")

# 📥 Entrada de dados
dias = st.number_input("Quantidade de dias de aluguel", min_value=1, step=1)
km = st.number_input("Quilometragem rodada (km)", min_value=0.0, step=0.1)

# 💰 Cálculo do valor
st.markdown("🚗🚗🚗")
if st.button("Calcular valor total"):
    with st.spinner("Calculando..."):
        time.sleep(1.5)
        total_dias = dias * diaria
        total_km = km * 0.15
        aluguel_total = total_dias + total_km

        st.success("✅ Cálculo concluído!")
        st.info(f"Você alugou o {marca_selecionada} {modelo_selecionado} por {dias} dias e rodou {km:.1f} km.")
        st.warning(f"💰 Valor total a pagar: R$ {aluguel_total:.2f}")

# 📍 Rodapé
st.markdown("""
<hr>
<center>
<p style='font-size:12px;'>© 2025 RideNow. Todos os direitos reservados.</p>
</center>
""", unsafe_allow_html=True)

