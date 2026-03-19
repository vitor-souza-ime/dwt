# 📊 Transformada Discreta de Wavelet (DWT) com Python

Este projeto demonstra a aplicação da **Transformada Discreta de Wavelet (DWT)** para análise e remoção de ruído em sinais, utilizando Python.

O código implementa um pipeline completo que inclui:

- Geração de sinal sintético
- Adição de ruído e descontinuidade
- Decomposição via DWT
- Análise estatística dos coeficientes (CLI)
- Remoção de ruído (denoising)
- Reconstrução do sinal
- Visualização gráfica

---

## 🧠 Conceito

A DWT permite decompor um sinal em diferentes níveis de resolução:

- **Aproximação (A)** → baixa frequência (tendência)
- **Detalhes (D)** → alta frequência (ruído e variações rápidas)

Essa abordagem é amplamente utilizada em:

- Processamento de sinais
- Compressão de dados
- Análise de vibração
- Sinais biomédicos (ECG, EEG)
- Detecção de falhas

---

## ⚙️ Tecnologias utilizadas

- Python 3.x
- NumPy
- PyWavelets
- Matplotlib

---

## 📦 Instalação

Instale as dependências com:

```bash
pip install numpy pywavelets matplotlib
````

---

## ▶️ Execução

Execute o script Python:

```bash
python main.py
```

---

## 🔬 Etapas do Código

### 1. Geração do sinal

* Sinal senoidal (base)
* Adição de ruído gaussiano
* Inserção de descontinuidade

---

### 2. Transformada Wavelet

* Wavelet utilizada: `db4`
* Nível de decomposição: `3`

Resultado:

* A3 → aproximação
* D3, D2, D1 → detalhes

---

### 3. Análise no terminal (CLI)

O programa imprime:

* Tamanho dos coeficientes
* Média
* Desvio padrão
* Primeiros valores

Exemplo:

```
Aproximação A3
  Tamanho: 56
  Média: ...
  Desvio padrão: ...
```

---

### 4. Denoising (remoção de ruído)

Aplicado:

* Threshold universal
* Thresholding suave (`soft threshold`)

Objetivo:

* Remover componentes de alta frequência (ruído)
* Preservar estrutura do sinal

---

### 5. Reconstrução

O sinal é reconstruído usando:

```python
pywt.waverec()
```

---

### 6. Visualização

O código gera dois gráficos:

#### 📈 Gráfico 1:

* Sinal ruidoso
* Coeficientes (A3, D3, D2, D1)
* Sinal reconstruído

#### 📉 Gráfico 2:

* Sinal original (limpo)
* Sinal com ruído
* Sinal filtrado (denoised)

---

## 📊 Interpretação dos Resultados

* **A3** → tendência global do sinal
* **D3/D2** → estruturas intermediárias
* **D1** → ruído de alta frequência

Após o denoising:

* Redução significativa do ruído
* Preservação da forma original

---

## 🚀 Possíveis extensões

* Comparação com FFT
* Uso de outras wavelets (`haar`, `sym`, `coif`)
* Aplicação em sinais reais
* Extração de features para Machine Learning
* Implementação em sistemas embarcados

---

## 📚 Referências

* PyWavelets Documentation
* Mallat, S. (Wavelet Theory)
* Daubechies, I. (Wavelets and Signal Processing)

---

## 👨‍💻 Autor

Projeto desenvolvido para fins educacionais e análise em processamento digital de sinais.

