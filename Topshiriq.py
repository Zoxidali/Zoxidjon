import numpy as np
import matplotlib.pyplot as plt

# ============ CHIZIQLI VA CHIZIQSIZ FUNKSIYALAR ============

# X qiymatlari oralig'i
x = np.linspace(-3, 3, 1000)

# 1. CHIZIQLI funksiyalar (Linear)
linear_1 = 2 * x + 1           # y = 2x + 1
linear_2 = -1.5 * x + 2        # y = -1.5x + 2
linear_3 = 0.5 * x - 1         # y = 0.5x - 1

# 2. CHIZIQSIZ funksiyalar (Nonlinear)
nonlinear_1 = x**2              # y = x² (kvadrat)
nonlinear_2 = x**3 - 2*x        # y = x³ - 2x (kub)
nonlinear_3 = np.sin(x)         # y = sin(x) (trigonometrik)
nonlinear_4 = np.exp(x) / 10    # y = e^x / 10 (eksponensial)
nonlinear_5 = 1 / (1 + np.exp(-x))  # y = sigmoid (logistik)

# ============ GRAFIKLAR ============
fig = plt.figure(figsize=(15, 10))

# ===== 1-QATOR: CHIZIQLI FUNKSIYALAR =====
fig.suptitle('CHIZIQLI vs CHIZIQSIZ ABSTRAKSIYA', fontsize=18, fontweight='bold')

# 1.1 Chiziqli funksiyalar grafigi
ax1 = fig.add_subplot(2, 3, 1)
ax1.plot(x, linear_1, 'b-', linewidth=2, label='y = 2x + 1')
ax1.plot(x, linear_2, 'r-', linewidth=2, label='y = -1.5x + 2')
ax1.plot(x, linear_3, 'g-', linewidth=2, label='y = 0.5x - 1')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.axvline(x=0, color='black', linewidth=0.5)
ax1.set_title('CHIZIQLI (LINEAR) FUNKSIYALAR', fontsize=12, color='blue', fontweight='bold')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.text(-2.8, 7, '✓ To\'g\'ri chiziq\n✓ Bir xil o\'zgarish\n✓ Superpozitsiya', fontsize=9,
         bbox=dict(facecolor='lightblue', alpha=0.5))

# 1.2 Kvadrat funksiya (chiziqsiz)
ax2 = fig.add_subplot(2, 3, 2)
ax2.plot(x, nonlinear_1, 'purple', linewidth=2, label='y = x²')
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axvline(x=0, color='black', linewidth=0.5)
ax2.set_title('CHIZIQSIZ - KVADRAT (x²)', fontsize=12, color='red', fontweight='bold')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.text(-2.8, 7, '✗ Egri chiziq\n✗ O\'zgarish tezligi\n  o\'zgaradi', fontsize=9,
         bbox=dict(facecolor='lightcoral', alpha=0.5))

# 1.3 Kub funksiya (chiziqsiz)
ax3 = fig.add_subplot(2, 3, 3)
ax3.plot(x, nonlinear_2, 'orange', linewidth=2, label='y = x³ - 2x')
ax3.axhline(y=0, color='black', linewidth=0.5)
ax3.axvline(x=0, color='black', linewidth=0.5)
ax3.set_title('CHIZIQSIZ - KUB (x³ - 2x)', fontsize=12, color='red', fontweight='bold')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.legend()
ax3.grid(True, alpha=0.3)

# 1.4 Sinus funksiya (chiziqsiz)
ax4 = fig.add_subplot(2, 3, 4)
ax4.plot(x, nonlinear_3, 'teal', linewidth=2, label='y = sin(x)')
ax4.axhline(y=0, color='black', linewidth=0.5)
ax4.axvline(x=0, color='black', linewidth=0.5)
ax4.set_title('CHIZIQSIZ - SINUS (sin x)', fontsize=12, color='red', fontweight='bold')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.legend()
ax4.grid(True, alpha=0.3)

# 1.5 Eksponensial funksiya (chiziqsiz)
ax5 = fig.add_subplot(2, 3, 5)
ax5.plot(x, nonlinear_4, 'brown', linewidth=2, label='y = eˣ / 10')
ax5.axhline(y=0, color='black', linewidth=0.5)
ax5.axvline(x=0, color='black', linewidth=0.5)
ax5.set_title('CHIZIQSIZ - EKSPONENSIAL (eˣ)', fontsize=12, color='red', fontweight='bold')
ax5.set_xlabel('x')
ax5.set_ylabel('y')
ax5.legend()
ax5.grid(True, alpha=0.3)

# 1.6 Sigmoid funksiya (chiziqsiz)
ax6 = fig.add_subplot(2, 3, 6)
ax6.plot(x, nonlinear_5, 'darkgreen', linewidth=2, label='y = 1/(1+e⁻ˣ)')
ax6.axhline(y=0, color='black', linewidth=0.5)
ax6.axvline(x=0, color='black', linewidth=0.5)
ax6.axhline(y=1, color='gray', linestyle='--', linewidth=0.5)
ax6.axhline(y=0.5, color='gray', linestyle='--', linewidth=0.5)
ax6.set_title('CHIZIQSIZ - SIGMOID (logistik)', fontsize=12, color='red', fontweight='bold')
ax6.set_xlabel('x')
ax6.set_ylabel('y')
ax6.legend()
ax6.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ============ QO'SHIMCHA TAQQOSLAMA GRAFIK ============
fig2, axes = plt.subplots(2, 2, figsize=(12, 10))
fig2.suptitle('CHIZIQLI va CHIZIQSIZ TIZIMLAR TAQQOSLAMASI', fontsize=16, fontweight='bold')
# Grafik 1: Chiziqli vs Kvadrat
axes[0, 0].plot(x, linear_1, 'b-', linewidth=2, label='Chiziqli (y = 2x + 1)')
axes[0, 0].plot(x, nonlinear_1, 'r-', linewidth=2, label='Chiziqsiz (y = x²)')
axes[0, 0].set_title('Chiziqli vs Kvadrat', fontsize=12)
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('y')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Grafik 2: Chiziqli vs Sinus
axes[0, 1].plot(x, linear_2, 'b-', linewidth=2, label='Chiziqli (y = -1.5x + 2)')
axes[0, 1].plot(x, nonlinear_3, 'r-', linewidth=2, label='Chiziqsiz (y = sin x)')
axes[0, 1].set_title('Chiziqli vs Sinus', fontsize=12)
axes[0, 1].set_xlabel('x')
axes[0, 1].set_ylabel('y')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Grafik 3: Chiziqli vs Eksponensial
axes[1, 0].plot(x, linear_3, 'b-', linewidth=2, label='Chiziqli (y = 0.5x - 1)')
axes[1, 0].plot(x, nonlinear_4, 'r-', linewidth=2, label='Chiziqsiz (y = eˣ/10)')
axes[1, 0].set_title('Chiziqli vs Eksponensial', fontsize=12)
axes[1, 0].set_xlabel('x')
axes[1, 0].set_ylabel('y')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# Grafik 4: Har xil chiziqsiz funksiyalar
axes[1, 1].plot(x, nonlinear_1, 'purple', linewidth=1.5, label='x²')
axes[1, 1].plot(x, nonlinear_2, 'orange', linewidth=1.5, label='x³ - 2x')
axes[1, 1].plot(x, nonlinear_3, 'teal', linewidth=1.5, label='sin x')
axes[1, 1].plot(x, nonlinear_4, 'brown', linewidth=1.5, label='eˣ/10')
axes[1, 1].plot(x, nonlinear_5, 'darkgreen', linewidth=1.5, label='sigmoid')
axes[1, 1].set_title('Chiziqsiz funksiyalar to\'plami', fontsize=12)
axes[1, 1].set_xlabel('x')
axes[1, 1].set_ylabel('y')
axes[1, 1].legend(loc='upper left', fontsize=8)
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ============ MATEMATIK TA'RIFLAR ============
print("\n" + "="*80)
print("CHIZIQLI VA CHIZIQSIZ FUNKSIYALAR - MATEMATIK TA'RIF")
print("="*80)

print("\n📐 CHIZIQLI FUNKSIYA (LINEAR):")
print("   • Formula: f(x) = kx + b")
print("   • Grafik: To'g'ri chiziq")
print("   • Xususiyatlar:")
print("       - f(x₁ + x₂) = f(x₁) + f(x₂)  (Additivlik)")
print("       - f(a·x) = a·f(x)              (Gomogenlik)")
print("       - Birgalikda: f(ax₁ + bx₂) = a·f(x₁) + b·f(x₂) (Superpozitsiya)")

print("\n🔄 CHIZIQSIZ FUNKSIYA (NONLINEAR):")
print("   • Formula: Yuqoridagi shartlarni qanoatlantirmaydigan har qanday funksiya")
print("   • Grafik: To'g'ri chiziq bo'lmagan har qanday egri chiziq")
print("   • Misollar: x², x³, sin(x), eˣ, log(x), |x|, 1/x, sigmoid")
print("   • Xususiyat: f(ax₁ + bx₂) ≠ a·f(x₁) + b·f(x₂)")

print("\n" + "="*80)
print("📊 AMALIY MISOL - SIGNAL QAYTA ISHLASHDA:")
print("="*80)

# Signal misoli
t = np.linspace(0, 2, 500)
signal = np.sin(2 * np.pi * 2 * t)  # 2Hz sinus signal

# Chiziqli ishlov: kuchaytirish
linear_output = 2 * signal

# Chiziqsiz ishlov: kvantlash (oldin ko'rganimizdek)
quant_levels = 4
quantized = np.round(signal * quant_levels) / quant_levels

fig3, axes3 = plt.subplots(3, 1, figsize=(12, 8))
fig3.suptitle('SIGNAL QAYTA ISHLASHDA CHIZIQLI vs CHIZIQSIZ', fontsize=14, fontweight='bold')

axes3[0].plot(t, signal, 'b-', linewidth=2)
axes3[0].set_title('Kirish signali (sinus)')
axes3[0].set_ylabel('Amplituda')
axes3[0].grid(True, alpha=0.3)

axes3[1].plot(t, linear_output, 'g-', linewidth=2)
axes3[1].set_title('Chiziqli ishlov: y = 2·x (kuchaytirish) - Signal shakli saqlanadi')
axes3[1].set_ylabel('Amplituda')
axes3[1].grid(True, alpha=0.3)

axes3[2].step(t, quantized, 'r-', linewidth=2, where='mid')
axes3[2].set_title('Chiziqsiz ishlov: Kvantlash - Signal shakli o\'zgaradi (pog\'onali)')
axes3[2].set_ylabel('Amplituda')
axes3[2].set_xlabel('Vaqt')
axes3[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n✅ XULOSA:")
print("   • CHIZIQLI tizim: Chiqish signali kirish signalining shaklini saqlaydi")
print("   • CHIZIQSIZ tizim: Chiqish signali kirish signalining shaklini o'zgartiradi")
print("   • Analog→Raqamli o'tishdagi KVANTLASH - chiziqsiz jarayon!")