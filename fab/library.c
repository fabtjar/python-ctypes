#include <stdio.h>
#include "library.h"
#include "math.h"

void say_hello(char* name) {
    printf("Hello %s!\n", name);
}

int add(int a, int b) {
    return a + b;
}

float approach(float t, float target, float delta) {
    return t < target ? fminf(t + delta, target) : fmaxf(t - delta, target);
}
