# Изменения
+ Изменены методы кодирования и декодирования таким образом, чтобы, если встречается одиночный символ, в сжатом виде перед ним не стояла единица. Иначе кодировка одного символа занимает в два раза больше места.
+ Для визуализации сжатия добавлена переменная, которая считает степень сжатия и выводит ее в консоль в процентах.