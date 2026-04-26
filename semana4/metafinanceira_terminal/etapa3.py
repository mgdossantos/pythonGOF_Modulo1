# ============================================================
# 🎯 META FINANCEIRA — Etapa 3: for com range()
# ============================================================
# Conceito: repetição com contador numérico usando range().
# Agora mostramos a evolução MÊS A MÊS da poupança.
#
# Estrutura do range():
#
#   range(inicio, fim, passo)
#   range(12)        → 0, 1, 2, ... 11
#   range(1, 13)     → 1, 2, 3, ... 12
#   range(0, 13, 3)  → 0, 3, 6, 9, 12
# ============================================================

objetivo = "Viagem para o Japão"
meta     = 5000.0
meses    = 12
renda    = 3000.0

por_mes    = meta / meses
capacidade = renda * 0.30

print("=" * 50)
print(f"🎯 {objetivo}")
print(f"💰 Meta: R$ {meta:.2f}  |  Guardar/mês: R$ {por_mes:.2f}")
print("=" * 50)

# ============================================================
# 🔁 FOR com range() — conta de 1 até o número de meses
# ============================================================

print(f"\n📅 Progressão mês a mês:\n")
print(f"{'Mês':<6} {'Poupado':>12} {'Falta':>12} {'%':>8}")
print("-" * 40)

for mes in range(1, meses + 1):          # ← range(1, 13) → 1, 2, ..., 12

    poupado   = por_mes * mes
    falta     = meta - poupado
    progresso = (poupado / meta) * 100

    # Ícone de progresso visual simples
    barra = "█" * int(progresso // 10) + "░" * (10 - int(progresso // 10))

    print(f"{mes:<6} R$ {poupado:>8.2f}  R$ {falta:>8.2f}  {progresso:>6.1f}%  {barra}")

print("-" * 40)
print(f"\n🎉 No mês {meses} você atingirá: R$ {meta:.2f}")

# --- Viabilidade ---
print()
if por_mes <= capacidade:
    print("✅ Meta VIÁVEL!")
elif por_mes <= renda * 0.50:
    print("⚠️  Meta DESAFIADORA.")
else:
    print("❌ Meta DIFÍCIL. Considere aumentar o prazo.")

# ============================================================
# 💡 O QUE APRENDEMOS:
#   - range(inicio, fim) gera números de inicio até fim-1
#   - range(1, meses+1) garante que contamos de 1 até meses
#   - Podemos usar o contador (mes) dentro do bloco
#   - f-strings com alinhamento: {valor:<6} {valor:>12}
#
# 🤔 PRÓXIMO DESAFIO: e se a pessoa puder guardar valores
#    diferentes por mês e quiser saber QUANDO vai chegar?
#    → Etapa 4: while!
# ============================================================