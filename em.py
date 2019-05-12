import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('font', size=15)

hline = 5
delta_hline = 0.2
delta_x_text = 0.2
x_arrow_1 = 2
x_arrow_2 = 7
x_arrow_3 = 4
x_arrow_4 = 9
x_arrow_5 = 0.5
height = 10
height_tall = 15
delta_height = height_tall - height

text_L = r"$\mathcal{L}(q)$"
text_KL = r"KL$(q||p)$"
text_ln = r"ln $p(\mathbf{X})$"
text_L_old = r"$\mathcal{L}(q, \mathbf{\theta}^{old})$"
text_KL_0 = r"KL$(q||p)=0$"
text_ln_old = r"ln $p(\mathbf{X} | \mathbf{\theta}^{old})$"
text_L_new = r"$\mathcal{L}(q, \mathbf{\theta}^{new})$"
text_ln_new = r"ln $p(\mathbf{X} | \mathbf{\theta}^{new})$"

"""Plot 1."""
plt.figure()

plt.axhline(y=0, linewidth=hline * 4, color='k')
plt.axhline(y=height / 2, xmax=0.5, linewidth=hline, color='b')
plt.axhline(y=height, linewidth=hline * 2, color='r')

plt.annotate(
    s='',
    xy=(x_arrow_1, 0 + delta_hline * 2),
    xytext=(x_arrow_1, height / 2 - delta_hline),
    arrowprops=dict(arrowstyle='<->'))
plt.annotate(
    s='',
    xy=(x_arrow_1,height / 2 + delta_hline),
    xytext=(x_arrow_1,height - delta_hline),
    arrowprops=dict(arrowstyle='<->'))
plt.annotate(
    s='',
    xy=(x_arrow_2,0 + delta_hline * 2),
    xytext=(x_arrow_2,height - delta_hline),
    arrowprops=dict(arrowstyle='<->'))

plt.text(y=3, x=x_arrow_1 + delta_x_text, s=text_L)
plt.text(y=7, x=x_arrow_1 + delta_x_text, s=text_KL)
plt.text(y=5, x=x_arrow_2 + delta_x_text, s=text_ln)

plt.ylim([0, 10])
plt.xlim([0, 10])
plt.axis('off')
plt.savefig('decomposition-EM.png')
plt.show()
plt.close()


"""Plot 2."""
plt.figure()

plt.axhline(y=0, linewidth=hline * 4, color='k')
plt.axhline(y=height / 2, xmax=0.5, linewidth=hline, linestyle='--', color='b')
plt.axhline(y=height, linewidth=hline * 2, color='r')
plt.axhline(y=height, xmax=0.5, linewidth=hline * 2, color='b')

plt.annotate(
    s='',
    xy=(x_arrow_1, 0 + delta_hline * 2),
    xytext=(x_arrow_1, height - delta_hline),
    arrowprops=dict(arrowstyle='<->'))
plt.annotate(
    s='',
    xy=(x_arrow_2, 0 + delta_hline * 2),
    xytext=(x_arrow_2,height - delta_hline),
    arrowprops=dict(arrowstyle='<->'))
plt.arrow(
    x=x_arrow_3, y=height / 2 + delta_hline,
    dx=0, dy = height/2 - delta_hline * 3,
    color='b',
    head_width=0.1)

plt.text(y=3, x=x_arrow_1 + delta_x_text, s=text_L_old)
plt.text(y=9.3, x=-1 + delta_x_text + delta_x_text, s=text_KL_0)
plt.text(y=5, x=x_arrow_2 + delta_x_text, s=text_ln_old)

plt.ylim([0, height])
plt.xlim([0, height])
plt.axis('off')
plt.savefig('E-step-EM.png')
plt.show()
plt.close()

"""Plot 3."""
plt.figure()

plt.axhline(y=0, linewidth=hline * 4, color='k')
plt.axhline(y=height, xmax=0.5, linewidth=hline, linestyle='--', color='b')
plt.axhline(y=height, xmin=0.5, linewidth=hline, linestyle='--', color='r')
plt.axhline(y=height_tall, linewidth=hline * 2, color='r')
plt.axhline(y=height + delta_height / 2, xmax=0.5, linewidth=hline, color='b')

plt.annotate(
    s='',
    xy=(x_arrow_1, 0 + delta_hline * 2),
    xytext=(x_arrow_1, height + delta_height / 2- delta_hline),
    arrowprops=dict(arrowstyle='<->'))
plt.annotate(
    s='',
    xy=(x_arrow_2, 0 + delta_hline * 2),
    xytext=(x_arrow_2, height_tall - delta_hline),
    arrowprops=dict(arrowstyle='<->'))
plt.annotate(
    s='',
    xy=(x_arrow_5, 0 + height + delta_height / 2 + delta_hline),
    xytext=(x_arrow_5, height_tall - delta_hline),
    arrowprops=dict(arrowstyle='<->'))
plt.arrow(
    x=x_arrow_3, y=height + delta_hline,
    dx=0, dy=delta_height/2 - delta_hline * 3,
    color='b',
    head_width=0.1)
plt.arrow(
    x=x_arrow_4, y=height + delta_hline,
    dx=0, dy=delta_height - delta_hline * 4,
    color='r',
    head_width=0.1)

plt.text(y=5, x=x_arrow_1 + delta_x_text, s=text_L_new)
plt.text(y=13.5, x=x_arrow_5 + delta_x_text, s=text_KL)
plt.text(y=5, x=x_arrow_2 + delta_x_text, s=text_ln_new)

plt.ylim([0, height_tall])
plt.xlim([0, height])
plt.axis('off')
plt.savefig('M-step-EM.png')
plt.show()
