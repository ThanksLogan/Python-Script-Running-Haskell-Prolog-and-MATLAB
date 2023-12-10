#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s <num1> <num2> ... <numN>\n", argv[0]);
        return 1;
    }

    int *arrayPtr = NULL;
    int arraySize = argc - 1;
    int threshold = 170;  // Adjust the threshold value as needed

    arrayPtr = (int *) malloc(arraySize * sizeof(int));

    if (arrayPtr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    for (int i = 1; i < argc; i++) {
        arrayPtr[i - 1] = atoi(argv[i]);
    }

    for (int i = 0; i < arraySize; i++) {
        if (arrayPtr[i] > threshold) {
            printf("255 ");
        } else {
            printf("0 ");
        }
    }

    printf("\n");

    // Don't forget to free the allocated memory
    free(arrayPtr);

    return 0;
}
