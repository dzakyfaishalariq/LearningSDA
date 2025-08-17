# Learning SDA (structur data and algoritma)

structur data dan algoritma adalah pembelajaran yang mengharuskan kita harus mengefisienkan program kita dan melakukan tata letak yang ada di struktur data dan algoritma yang kita buat serta memahami cara kerja dan penyelesaian suatu problem untuk computasi yang digunakan.

##  learning recursif and loop basic

Besic pertama ini adalah penggunaan recursif pada studi kasus bilangan fibonaci rumus yang sesuai dengan fibonaci ini adalah 

$$F(n) = F(n-1) + F(n-2)$$

## learning array sorting bubble short
pengurutan bubble sorting yang digunakan menggunakan iterasi sebanyak panjang array yang diinputkan dengan mencari dan mengubah urutan pada nilai yang lebih kecil di pindahkan ke depan pada nilai bilangan yang besar sesuai dengan kondisi berikut contoh iterasi yang digunakan:
``` txt
iterasi 0 : [1, 3, 2, 4, 4, 6, 4, 2, 7, 9]
iterasi 1 : [1, 2, 3, 4, 4, 4, 2, 6, 7, 9]
iterasi 2 : [1, 2, 3, 4, 4, 2, 4, 6, 7, 9]
iterasi 3 : [1, 2, 3, 4, 2, 4, 4, 6, 7, 9]
iterasi 4 : [1, 2, 3, 2, 4, 4, 4, 6, 7, 9]
iterasi 5 : [1, 2, 2, 3, 4, 4, 4, 6, 7, 9]
iterasi 6 : [1, 2, 2, 3, 4, 4, 4, 6, 7, 9]
iterasi 7 : [1, 2, 2, 3, 4, 4, 4, 6, 7, 9]
iterasi 8 : [1, 2, 2, 3, 4, 4, 4, 6, 7, 9]
iterasi 9 : [1, 2, 2, 3, 4, 4, 4, 6, 7, 9]
[1, 2, 2, 3, 4, 4, 4, 6, 7, 9]

```

sedangkan hasil efisiensi dari algoritma nya adalah dapat menghasilkan eksekusi pogram yang efisien dan lebih cepat dengan perbedaan waktu nya sekitar 3.2901763916015625e-05  sedankan iterasi sesuai dengan panjang array nya mendapatkan waktu sekitar 8.535385131835938e-05 berikut hasilnya

``` txt

iterasi 0 : [1, 3, 2, 4, 4, 6, 4, 2, 7, 9]
iterasi 1 : [1, 2, 3, 4, 4, 4, 2, 6, 7, 9]
iterasi 2 : [1, 2, 3, 4, 4, 2, 4, 6, 7, 9]
iterasi 3 : [1, 2, 3, 4, 2, 4, 4, 6, 7, 9]
iterasi 4 : [1, 2, 3, 2, 4, 4, 4, 6, 7, 9]
iterasi 5 : [1, 2, 2, 3, 4, 4, 4, 6, 7, 9]
[1, 2, 2, 3, 4, 4, 4, 6, 7, 9]

```
dari gambaran di atas kita dapat memperhatikan pada shorting tanpa efisiensi dia akan melakukan iterasi terus menerus sesuai panjang array dan ini mengakibtkan pemborosan waktu eksekusi maka dilakukan efisiensi pada pogram kedua maka di dapatkan iterasi yang hanya dilakukan sesuai dengan kondisi dari array nya apabila sudah terurut maka pogram di berhentikan.