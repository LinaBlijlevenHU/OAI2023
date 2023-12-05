# Random lib for shuffling
import random
# Plotting imports
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N_BARS = 50  # Set the number of bars for the dataset

# Keep track of algorithms running
INSERTION_RUNNING, SELECTION_RUNNING = True, True

# Titles for the plots
INSERTION_TITLE, SELECTION_TITLE = 'Insertion Sort', 'Selection Sort'


def simulate_dataset():
    '''
    Simulate a dataset with a set number of elements.

    :return: arr    Numbers from 1 - N
    '''
    # Create a list of N ints from 1-N
    unsorted_array = list(range(1, N_BARS + 1))

    # Shuffle (this function has no return value)
    random.shuffle(unsorted_array)

    return unsorted_array


def update_bar_chart(ax, arr, bar_rects, iterations, title):
    '''
    Update the bar chart to visualize a change in the list.

    :param ax:              Ax for title for subplot
    :param arr:             Values
    :param bar_rects:       Rectangles in the plot
    :param iterations:      Current no. of iterations
    :param title:           (Partial) title for the plot
    '''

    # Update each bar in the figure to its new value
    for rect, val in zip(bar_rects, arr):
        rect.set_height(val)

    # Increment the amount of iterations and update the title
    iterations[0] += 1
    ax.set_title(f'{title} (Iteration {iterations[0]})')


def insertion_sort_animation(ax, arr):
    """
    Perform an insertion sort visualization on a given array.

    :param:     ax      The subplot where the visualization will be displayed (matplotlib obj)
    :param:     arr     The array to be sorted

    Yields:
    Tuple[List[int], List[matplotlib.patches.Rectangle], List[int]]:
        A tuple containing the updated array, bar rectangles, and current iteration count for animation.
    """
    ax.set_title(INSERTION_TITLE)
    bar_rects = ax.bar(range(len(arr)), arr, color='lightblue', edgecolor='black')
    iterations = [0]

    def insertion_sort():
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                yield arr.copy(), bar_rects, iterations
                j -= 1
            arr[j + 1] = key
            yield arr.copy(), bar_rects, iterations

    return insertion_sort


def selection_sort_animation(ax, arr):
    """
    Perform a selection sort visualization on a given array.

    :param:     ax      The subplot where the visualization will be displayed (matplotlib obj)
    :param:     arr     The array to be sorted

    Yields:
    Tuple[List[int], List[matplotlib.patches.Rectangle], List[int]]:
        A tuple containing the updated array, bar rectangles, and current iteration count for animation.
    """
    ax.set_title(SELECTION_TITLE)
    bar_rects = ax.bar(range(len(arr)), arr, color='lightcoral', edgecolor='black')
    iterations = [0]

    def selection_sort():
        """
        Selection sort implementation that yields after every iteration,
        in order to use the data for animation.
        """
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
            yield arr.copy(), bar_rects, iterations

    return selection_sort


def main():
    """
    Run the sorting visualization comparing extravaganza.

    :param
    """
    unsorted_array = simulate_dataset()
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    insertion_sort_func = insertion_sort_animation(axes[0], unsorted_array.copy())
    selection_sort_func = selection_sort_animation(axes[1], unsorted_array.copy())

    def update_fig(frame_data, ax, sort_title):
        """
        Update
        :param: frame_data      Current state of the array
        :param: ax              Subplot to update
        :param: title
        """
        arr, rects, iterations = frame_data
        update_bar_chart(ax, arr, rects, iterations, sort_title)

    def update_insertion(ax, insertion_sort_gen):
        """
        Perform an update on the insertion sort algorithm.

        :param  ax  subplot
        :param insertion_sort_gen:  Generator for insertion sort data
        """
        global INSERTION_RUNNING

        insertion_data = next(insertion_sort_gen, None)

        if insertion_data is not None:
            yield insertion_data, ax, INSERTION_TITLE
        else:
            INSERTION_RUNNING = False

    def update_selection(ax, selection_sort_gen):
        """
        Perform an update on the insertion sort algorithm.

        :param  ax  subplot
        :param selection_sort_gen:  Generator for selection sort data
        """
        global SELECTION_RUNNING

        selection_data = next(selection_sort_gen, None)

        if selection_data is not None:
            yield selection_data, ax, SELECTION_TITLE
        else:
            SELECTION_RUNNING = False

    def combined_sort():
        """
        Run the updates from the sorting algorithms in parallel.
        """
        global INSERTION_RUNNING, SELECTION_RUNNING

        insertion_sort_gen = insertion_sort_func()
        selection_sort_gen = selection_sort_func()

        while INSERTION_RUNNING or SELECTION_RUNNING:
            yield from update_insertion(axes[0], insertion_sort_gen)
            yield from update_selection(axes[1], selection_sort_gen)

    # Magical animation lines
    ani = animation.FuncAnimation(fig, lambda x: update_fig(*x), frames=combined_sort, blit=False, repeat=False)

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()
