#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    bool revisar = true, encontrado;

    while (revisar) {
        encontrado = false;
        FILE *p = popen("tasklist", "r");
        char linea[500];
        
        while (fgets(linea, sizeof(linea), p)) {
            if(strstr(linea,"mainpy.exe")) {
                encontrado = true;
            }
        }
        if (encontrado == false)
            system("start mainpy.exe");
        
        pclose(p);
    }
}