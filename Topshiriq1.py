import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# CHIZIQLI VA CHIZIQSIZ TIZIMLAR - BIRLASHTIRILGAN DASTUR
# =========================================================

# -----------------------------
# 1. ASOSIY FUNKSIYALAR
# -----------------------------
x = np.linspace(-3, 3, 1000)

# Chiziqli funksiyalar
linear_1 = 2 * x + 1
linear_2 = -1.5 * x + 2
linear_3 = 0.5 * x - 1

# Chiziqsiz funksiyalar
nonlinear_1 = x**2
nonlinear_2 = x**3 - 2*x
nonlinear_3 = np.sin(x)
nonlinear_4 = np.exp(x) / 10
nonlinear_5 = 1 / (1 + np.exp(-x))

# -----------------------------
# 2. 1-OYNA: ABSTRAKSIYA
# -----------------------------
fig1 = plt.figure(figsize=(16, 10))
fig1.suptitle("CHIZIQLI vs CHIZIQSIZ ABSTRAKSIYA",
              fontsize=20, fontweight='bold')

# 1.1 Chiziqli funksiyalar
ax1 = fig1.add_subplot(2, 3, 1)
ax1.plot(x, linear_1, 'b-', linewidth=2, label='y = 2x + 1')
ax1.plot(x, linear_2, 'r-', linewidth=2, label='y = -1.5x + 2')
ax1.plot(x, linear_3, 'g-', linewidth=2, label='y = 0.5x - 1')
ax1.axhline(y=0, color='black', linewidth=0.6)
ax1.axvline(x=0, color='black', linewidth=0.6)
ax1.set_title("CHIZIQLI (LINEAR) FUNKSIYALAR",
              fontsize=13, color='blue', fontweight='bold')
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.text(-2.8, 6.6,
         "✓ To'g'ri chiziq\n✓ Bir xil o'zgarish\n✓ Superpozitsiya",
         fontsize=10,
         bbox=dict(facecolor='lightblue', alpha=0.5))

# 1.2 Kvadrat
ax2 = fig1.add_subplot(2, 3, 2)
ax2.plot(x, nonlinear_1, color='purple', linewidth=2, label='y = x²')
ax2.axhline(y=0, color='black', linewidth=0.6)
ax2.axvline(x=0, color='black', linewidth=0.6)
ax2.set_title("CHIZIQSIZ - KVADRAT (x²)",
              fontsize=13, color='red', fontweight='bold')
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.text(-2.8, 7.0,
         "✗ Egri chiziq\n✗ O'zgarish tezligi\n  o'zgaradi",
         fontsize=10,
         bbox=dict(facecolor='lightcoral', alpha=0.5))

# 1.3 Kub
ax3 = fig1.add_subplot(2, 3, 3)
ax3.plot(x, nonlinear_2, color='orange', linewidth=2, label='y = x³ - 2x')
ax3.axhline(y=0, color='black', linewidth=0.6)
ax3.axvline(x=0, color='black', linewidth=0.6)
ax3.set_title("CHIZIQSIZ - KUB (x³ - 2x)",
              fontsize=13, color='red', fontweight='bold')
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.grid(True, alpha=0.3)
ax3.legend()

# 1.4 Sinus
ax4 = fig1.add_subplot(2, 3, 4)
ax4.plot(x, nonlinear_3, color='teal', linewidth=2, label='y = sin(x)')
ax4.axhline(y=0, color='black', linewidth=0.6)
ax4.axvline(x=0, color='black', linewidth=0.6)
ax4.set_title("CHIZIQSIZ - SINUS (sin x)",
              fontsize=13, color='red', fontweight='bold')
ax4.set_xlabel("x")
ax4.set_ylabel("y")
ax4.grid(True, alpha=0.3)
ax4.legend()

# 1.5 Eksponensial
ax5 = fig1.add_subplot(2, 3, 5)
ax5.plot(x, nonlinear_4, color='brown', linewidth=2, label='y = eˣ / 10')
ax5.axhline(y=0, color='black', linewidth=0.6)
ax5.axvline(x=0, color='black', linewidth=0.6)
ax5.set_title("CHIZIQSIZ - EKSPONENSIAL (eˣ)",
              fontsize=13, color='red', fontweight='bold')
ax5.set_xlabel("x")
ax5.set_ylabel("y")
ax5.grid(True, alpha=0.3)
ax5.legend()

# 1.6 Sigmoid
ax6 = fig1.add_subplot(2, 3, 6)
ax6.plot(x, nonlinear_5, color='darkgreen', linewidth=2, label='y = 1/(1+e⁻ˣ)')
ax6.axhline(y=0, color='black', linewidth=0.6)
ax6.axvline(x=0, color='black', linewidth=0.6)
ax6.axhline(y=1, color='gray', linestyle='--', linewidth=0.7)
ax6.axhline(y=0.5, color='gray', linestyle='--', linewidth=0.7)
ax6.set_title("CHIZIQSIZ - SIGMOID (logistik)",
              fontsize=13, color='red', fontweight='bold')
ax6.set_xlabel("x")
ax6.set_ylabel("y")
ax6.grid(True, alpha=0.3)
ax6.legend()

plt.tight_layout(rect=[0, 0, 1, 0.95])

# -----------------------------
# 3. 2-OYNA: TAQQOSLAMA
# -----------------------------
fig2, axes = plt.subplots(2, 2, figsize=(16, 9))
fig2.suptitle("CHIZIQLI va CHIZIQSIZ TIZIMLAR TAQQOSLAMASI",
              fontsize=20, fontweight='bold')

# Chiziqli vs Kvadrat
axes[0, 0].plot(x, linear_1, color='blue', linewidth=2, label='Chiziqli (y = 2x + 1)')
axes[0, 0].plot(x, nonlinear_1, color='red', linewidth=2, label='Chiziqsiz (y = x²)')
axes[0, 0].set_title("Chiziqli vs Kvadrat", fontsize=15)
axes[0, 0].set_xlabel("x")
axes[0, 0].set_ylabel("y")
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].legend()

# Chiziqli vs Sinus
axes[0, 1].plot(x, linear_2, color='blue', linewidth=2, label='Chiziqli (y = -1.5x + 2)')
axes[0, 1].plot(x, nonlinear_3, color='red', linewidth=2, label='Chiziqsiz (y = sin x)')
axes[0, 1].set_title("Chiziqli vs Sinus", fontsize=15)
axes[0, 1].set_xlabel("x")
axes[0, 1].set_ylabel("y")
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].legend()

# Chiziqli vs Eksponensial
axes[1, 0].plot(x, linear_3, color='blue', linewidth=2, label='Chiziqli (y = 0.5x - 1)')
axes[1, 0].plot(x, nonlinear_4, color='red', linewidth=2, label='Chiziqsiz (y = eˣ/10)')
axes[1, 0].set_title("Chiziqli vs Eksponensial", fontsize=15)
axes[1, 0].set_xlabel("x")
axes[1, 0].set_ylabel("y")
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].legend()

# Chiziqsiz funksiyalar toplami
axes[1, 1].plot(x, nonlinear_1, color='purple', linewidth=1.8, label='x²')
axes[1, 1].plot(x, nonlinear_2, color='orange', linewidth=1.8, label='x³ - 2x')
axes[1, 1].plot(x, nonlinear_3, color='teal', linewidth=1.8, label='sin x')
axes[1, 1].plot(x, nonlinear_4, color='brown', linewidth=1.8, label='eˣ/10')
axes[1, 1].plot(x, nonlinear_5, color='darkgreen', linewidth=1.8, label='sigmoid')
axes[1, 1].set_title("Chiziqsiz funksiyalar to'plami", fontsize=15)
axes[1, 1].set_xlabel("x")
axes[1, 1].set_ylabel("y")
axes[1, 1].grid(True, alpha=0.3)
axes[1, 1].legend(loc='upper left', fontsize=9)

plt.tight_layout(rect=[0, 0, 1, 0.95])

# -----------------------------
# 4. SIGNAL QAYTA ISHLASH
# -----------------------------
t = np.linspace(0, 2, 1000)
signal = np.sin(2 * np.pi * 2 * t)  # 2 Hz sinus

# Chiziqli ishlov
linear_output = 2 * signal

# Chiziqsiz ishlov: kvantlash
quant_levels = 4
quantized = np.round(signal * quant_levels) / quant_levels

fig3, axes3 = plt.subplots(3, 1, figsize=(16, 9))
fig3.suptitle("SIGNAL QAYTA ISHLASHDA CHIZIQLI vs CHIZIQSIZ",
              fontsize=20, fontweight='bold')

# Kirish signali
axes3[0].plot(t, signal, color='blue', linewidth=2.2)
axes3[0].set_title("Kirish signali (sinus)", fontsize=16)
axes3[0].set_ylabel("Amplituda")
axes3[0].grid(True, alpha=0.3)

# Chiziqli ishlov
axes3[1].plot(t, linear_output, color='green', linewidth=2.2)
axes3[1].set_title("Chiziqli ishlov: y = 2·x (kuchaytirish) - Signal shakli saqlanadi",
                   fontsize=15)
axes3[1].set_ylabel("Amplituda")
axes3[1].grid(True, alpha=0.3)

# Chiziqsiz ishlov
axes3[2].step(t, quantized, where='mid', color='red', linewidth=2.2)
axes3[2].set_title("Chiziqsiz ishlov: Kvantlash - Signal shakli o'zgaradi (pog'onali)",
                   fontsize=15)
axes3[2].set_ylabel("Amplituda")
axes3[2].set_xlabel("Vaqt")
axes3[2].grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.95])

# -----------------------------
# 5. KONSOLGA MATNLI IZOH
# -----------------------------
print("\n" + "=" * 90)
print("CHIZIQLI VA CHIZIQSIZ FUNKSIYALAR - MATEMATIK TA'RIF")
print("=" * 90)

print("\n📐 CHIZIQLI FUNKSIYA (LINEAR):")
print("   • Formula: f(x) = kx + b")
print("   • Grafik: To'g'ri chiziq")
print("   • Xususiyatlar:")
print("       - f(x₁ + x₂) = f(x₁) + f(x₂)   (Additivlik)")
print("       - f(a·x) = a·f(x)               (Gomogenlik)")
print("       - Superpozitsiya bajariladi")

print("\n🔄 CHIZIQSIZ FUNKSIYA (NONLINEAR):")
print("   • Formula: Yuqoridagi shartlarni qanoatlantirmaydigan funksiya")
print("   • Grafik: Egri chiziq")
print("   • Misollar: x², x³, sin(x), eˣ, sigmoid")
print("   • Superpozitsiya bajarilmaydi")

print("\n" + "=" * 90)
print("📊 AMALIY MISOL - SIGNAL QAYTA ISHLASHDA")
print("=" * 90)
print("   • Chiziqli tizim: Chiqish kirish signaliga proporsional bo'ladi")
print("   • Chiziqsiz tizim: Chiqish signal shaklini o'zgartiradi")
print("   • Kvantlash: analog → raqamli o'tishda uchraydigan chiziqsiz jarayon")

print("\n✅ XULOSA:")
print("   • CHIZIQLI tizim signal shaklini saqlaydi")
print("   • CHIZIQSIZ tizim signal shaklini o'zgartiradi")
print("   • Grafiklar orqali farq aniq ko'rinadi")

# -----------------------------
# 6. HAMMA OYNALARNI CHIQARISH
# -----------------------------
plt.show()