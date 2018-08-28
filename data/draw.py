draw
import matplotlib
matplotlib.use('Agg') # agg
import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.savefig('myfig')


import matplotlib.pyplot as plt
plt.switch_backend('agg')
plt.plot([1,2,3])
plt.savefig('myfig')


import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
plt.plot([1,2,3])
