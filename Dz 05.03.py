def sort_strings_by_length(strings):
    """
    Функция сортирует список строк по длине строк с помощью пузырьковой сортировки.

    :param strings: Список строк для сортировки.
    :return: Отсортированный список строк.
    """
    n = len(strings)

    # Проходим по всем элементам списка
    for i in range(n):
        # Внутренний цикл для сравнения соседних элементов
        for j in range(0, n - i - 1):
            # Если длина текущего элемента больше длины следующего, меняем их местами
            if len(strings[j]) > len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]

    return strings
