import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Set bond parameters
face_value = 1000
coupon_rate = 0.06
years = 5
coupon = face_value * coupon_rate

# Helper function to calculate Macaulay Duration
def macaulay_duration(cash_flows, times, discount_rate):
    discounted_cash_flows = [cf / (1 + discount_rate) ** t for cf, t in zip(cash_flows, times)]
    weighted_times = [t * cf / (1 + discount_rate) ** t for cf, t in zip(cash_flows, times)]
    return sum(weighted_times) / sum(discounted_cash_flows)

# Bullet bond
bullet_cash_flows = [coupon] * (years - 1) + [coupon + face_value]
bullet_times = list(range(1, years + 1))
bullet_duration = macaulay_duration(bullet_cash_flows, bullet_times, coupon_rate)
bullet_wal = years  # All principal paid at maturity

# Amortizing bond
amortizing_principal = face_value / years
amortizing_cash_flows = [(amortizing_principal + coupon)] * years
amortizing_times = list(range(1, years + 1))
amortizing_principal_payments = [amortizing_principal] * years
amortizing_wal = sum(t * p for t, p in zip(amortizing_times, amortizing_principal_payments)) / face_value
amortizing_duration = macaulay_duration(amortizing_cash_flows, amortizing_times, coupon_rate)

# Zero-coupon bond
zero_cash_flows = [0] * (years - 1) + [face_value]
zero_times = list(range(1, years + 1))
zero_duration = macaulay_duration(zero_cash_flows, zero_times, coupon_rate)
zero_wal = years  # All principal paid at maturity

# Prepare data for plotting
bond_types = ['Bullet (6%)', 'Amortizing (6%)', 'Zero-Coupon']
durations = [bullet_duration, amortizing_duration, zero_duration]
wals = [bullet_wal, amortizing_wal, zero_wal]

x = np.arange(len(bond_types))
width = 0.35

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, durations, width, label='Duration')
rects2 = ax.bar(x + width/2, wals, width, label='WAL')

ax.set_ylabel('Years')
ax.set_title('Duration vs Weighted Average Life (WAL) for 5-Year Bonds')
ax.set_xticks(x)
ax.set_xticklabels(bond_types)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.legend()

for rect in rects1 + rects2:
    height = rect.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig('duration_vs_wal.png')
plt.close()
