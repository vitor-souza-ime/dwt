import numpy as np
import pywt
import matplotlib.pyplot as plt

# ==============================
# 1. Gerar sinal de teste
# ==============================
np.random.seed(42)

t = np.linspace(0, 1, 400)

# Sinal original (limpo)
sinal_limpo = np.sin(2 * np.pi * 5 * t)

# Adicionando ruído
ruido = 0.6 * np.random.randn(len(t))
sinal_ruidoso = sinal_limpo + ruido

# Criando uma descontinuidade
sinal_ruidoso[200:] += 2

# ==============================
# 2. Aplicar DWT
# ==============================
wavelet = 'db4'
nivel = 3

coef = pywt.wavedec(sinal_ruidoso, wavelet, level=nivel)

# ==============================
# 3. CLI (análise dos coeficientes)
# ==============================
print("\n=== ANÁLISE DWT ===\n")

for i, c in enumerate(coef):
    if i == 0:
        tipo = f"Aproximação A{nivel}"
    else:
        tipo = f"Detalhe D{nivel - i + 1}"
    
    print(f"{tipo}")
    print(f"  Tamanho: {len(c)}")
    print(f"  Média: {np.mean(c):.4f}")
    print(f"  Desvio padrão: {np.std(c):.4f}")
    print(f"  Primeiros valores: {c[:5]}\n")

# ==============================
# 4. DENOISING (remoção de ruído)
# ==============================
# Threshold universal
sigma = np.median(np.abs(coef[-1])) / 0.6745
threshold = sigma * np.sqrt(2 * np.log(len(sinal_ruidoso)))

coef_denoised = coef.copy()

for i in range(1, len(coef_denoised)):
    coef_denoised[i] = pywt.threshold(coef_denoised[i], threshold, mode='soft')

# Reconstrução do sinal
sinal_rec = pywt.waverec(coef_denoised, wavelet)

# Ajuste de tamanho (às vezes fica 1 amostra a mais)
sinal_rec = sinal_rec[:len(sinal_ruidoso)]

# ==============================
# 5. PLOTAGEM COMPLETA
# ==============================
total_plots = len(coef) + 2  # sinal original + coef + reconstruído

plt.figure(figsize=(12, 10))

# --- Sinal original ---
plt.subplot(total_plots, 1, 1)
plt.plot(sinal_ruidoso)
plt.title("Sinal Ruidoso")

# --- Coeficientes ---
for i, c in enumerate(coef):
    plt.subplot(total_plots, 1, i + 2)
    
    if i == 0:
        plt.plot(c)
        plt.title(f"Aproximação (A{nivel})")
    else:
        plt.plot(c)
        plt.title(f"Detalhe (D{nivel - i + 1})")

# --- Sinal reconstruído ---
plt.subplot(total_plots, 1, total_plots)
plt.plot(sinal_rec)
plt.title("Sinal Reconstruído (Denoised)")

plt.tight_layout()
plt.show()

# ==============================
# 6. COMPARAÇÃO FINAL
# ==============================
plt.figure(figsize=(10, 5))

plt.plot(sinal_limpo, label="Original (limpo)")
plt.plot(sinal_ruidoso, label="Ruidoso", alpha=0.6)
plt.plot(sinal_rec, label="Denoised", linestyle='--')

plt.legend()
plt.title("Comparação de Sinais")
plt.show()
