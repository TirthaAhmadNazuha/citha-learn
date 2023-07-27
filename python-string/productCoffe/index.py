from kopi import Coffee
from grinder import gilingKopi

kopi = Coffee('Arabica', 'Nutty caramel', 'Gayo')
print(kopi.status)
gilingKopi(kopi)
print(kopi.status)