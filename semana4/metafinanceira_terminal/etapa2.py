# ============================================================
# 🎯 META FINANCEIRA — Etapa 2: for com lista
# ============================================================
# Conceito: repetição com FOR iterando sobre uma lista.
# Agora calculamos VÁRIAS metas sem copiar código!
#
# Estrutura do FOR:
#
#   for variavel in lista:
#       bloco que repete
#
# A cada volta, "variavel" recebe o próximo item da lista.
# ============================================================

# --- Lista de metas (cada item é uma tupla: objetivo, meta, meses) ---
metas = [
    ("Viagem para o Japão", 5000,  12),
    ("Notebook novo",       3000,   6),
    ("Reserva de emergência", 10000, 24),
]

renda = 3000.0  # renda mensal (mesma para todos)

# ============================================================
# 🔁 O FOR vai repetir o bloco abaixo para cada meta da lista
# ============================================================

for objetivo, meta, meses in metas:       # ← desempacota cada tupla

    por_mes    = meta / meses
    capacidade = renda * 0.30

    print("=" * 45)
    print(f"🎯 Objetivo: {objetivo}")
    print(f"💰 Meta: R$ {meta:.2f} em {meses} meses")
    print(f"📅 Guardar por mês: R$ {por_mes:.2f}")
    print(f"📊 Capacidade (30%): R$ {capacidade:.2f}")

    if por_mes <= capacidade:
        print("✅ Meta VIÁVEL! Você consegue!")
    elif por_mes <= renda * 0.50:
        print("⚠️  Meta DESAFIADORA. Vai precisar de esforço.")
    else:
        print("❌ Meta DIFÍCIL. Considere aumentar o prazo.")

print("=" * 45)
print(f"\n✔️  Total de metas analisadas: {len(metas)}")

# ============================================================
# 💡 O QUE APRENDEMOS:
#   - FOR percorre cada item de uma lista
#   - O bloco indentado repete para cada item
#   - Podemos desempacotar tuplas direto no FOR
#   - len() conta quantos itens tem na lista
#
# 🤔 PRÓXIMO DESAFIO: e se quisermos ver MÊS A MÊS
#    quanto já teríamos poupado? → Etapa 3: range()!
# ============================================================