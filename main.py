import tkinter as tk
from tkinter import scrolledtext
import MergeSort as MST
import Quadsort as HST
import Quicksort as QST
import Arraycheck as AC
import random
import timeit

def sort_and_measure(algorithm, data_size, data_type, text_widget):
    result_text = f"{algorithm}: Data Size: {data_size}, Data Type: {data_type}\n"

    # Generate test data
    data = [random.randint(0, 1048576) if data_type == 'int' else random.uniform(0.0, 0.9) for _ in range(data_size)]

    # Time sorting
    start_time = timeit.default_timer()
    sorted_data = algorithm(data.copy())
    time_taken = timeit.default_timer() - start_time

    # Output the results
    result_text += f"{algorithm.__name__}: Time taken: {time_taken:.6f} seconds\n"
    result_text += f"Is the array in order: {AC.is_numerical_order(sorted_data)}\n\n"

    text_widget.insert(tk.END, result_text)

def main():
    random.seed(42)

    algorithms = [MST.three_way_merge_sort_initialization, HST.heapSort, QST.randomized_quick_sort]

    root = tk.Tk()
    root.title("Sorting Algorithms Results")

    text_widget = scrolledtext.ScrolledText(root, width=80, height=20)
    text_widget.pack()

    for algorithm in algorithms:
        for i in range(3, 4):  # Adjust the range as needed
            data_size = 2 ** i
            sort_and_measure(algorithm, data_size, 'int', text_widget)
            sort_and_measure(algorithm, data_size, 'float', text_widget)

    root.mainloop()

if __name__ == "__main__":
    main()
