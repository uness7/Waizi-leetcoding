#include <stdio.h>
#include <stdlib.h>

typedef struct s_dict {
    char key;
    int value;
} t_dict;

int getValue(t_dict dict[], int size, char key) {
    int i;

    for (i = 0; i < size; i++) {
        if (dict[i].key == key) {
            return (dict[i].value);
        }
    }
    return (-1); // Key not found
}

int romanToInt(char* s) {
    t_dict values[] = {{'I', 1},   {'V', 5},   {'X', 10},  {'L', 50},
                       {'C', 100}, {'D', 500}, {'M', 1000}};
    int i = 0;
    int result = 0;
    int current, next;

    while (s[i]) {
        current = getValue(values, sizeof(values) / sizeof(values[0]), s[i]);

        if (s[i + 1] &&
            current <
                getValue(values, sizeof(values) / sizeof(values[0]), s[i + 1]))
            result -= current;
        else
            result += current;
        i++;
    }
    return (result);
}

