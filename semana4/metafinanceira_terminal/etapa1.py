# ============================================================
# 🎯 META FINANCEIRA — Etapa 1: Sem repetição
# ============================================================
# Conceito: código sequencial, linha por linha.
# Problema: e se precisarmos calcular 3 metas diferentes?
#           Teríamos que copiar tudo 3 vezes! 😱
# ============================================================

# --- Dados da meta ---
objetivo = "Viagem para o Japão"
meta     = 5000.0    # R$
meses    = 12
renda    = 3000.0    # R$

# --- Cálculos ---
por_mes    = meta / meses
capacidade = renda * 0.30

# --- Resultados ---
print("=" * 45)
print(f"🎯 Objetivo: {objetivo}")
print(f"💰 Meta: R$ {meta:.2f} em {meses} meses")
print(f"📅 Guardar por mês: R$ {por_mes:.2f}")
print(f"📊 Capacidade (30% da renda): R$ {capacidade:.2f}")
3
if por_mes <= capacidade:
    print("✅ Meta VIÁVEL! Você consegue!")
elif por_mes <= renda * 0.50:
    print("⚠️  Meta DESAFIADORA. Vai precisar de esforço.")
else:
    print("❌ Meta DIFÍCIL. Considere aumentar o prazo.")
print("=" * 45)

# ============================================================
# 😱 PROBLEMA: e se você tiver 3 metas?
#    Você precisaria copiar esse bloco inteiro 3 vezes!
#    → Isso é repetição MANUAL. Existe um jeito melhor...
#    → Na próxima etapa: vamos usar o FOR!
# ============================================================