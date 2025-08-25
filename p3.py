def en_buyuk_asal_carpan(n):
    i = 2

    while i * i <= n:
        if n % i:
            # Eğer n, i'ye bölünmüyorsa, bir sonraki sayıya geç.
            i += 1
        else:
            # Eğer n, i'ye bölünüyorsa, n'i i'ye bölerek küçült.
            n //= i
    return n

sayi = 600851475143

sonuc = en_buyuk_asal_carpan(sayi)
print(f"{sayi} sayısının en büyük asal çarpanı: {sonuc}")
