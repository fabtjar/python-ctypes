#ifndef FAB_LIBRARY_H
#define FAB_LIBRARY_H

// Windows needs to specify the DLL can be exported.
#if defined(_WIN32)
    #define FAB_EXPORT __declspec(dllexport)
#endif

#ifndef FAB_EXPORT
    #define FAB_EXPORT
#endif

FAB_EXPORT void say_hello(char* name);
FAB_EXPORT int add(int a, int b);
FAB_EXPORT float approach(float t, float target, float delta);

#endif //FAB_LIBRARY_H
