pol = ['казак', ' телефон', 'дед', 'шалаш', 'машина']
def polindrom(x):
    return x == x[::-1]
print(list(filter(polindrom, pol)))
  