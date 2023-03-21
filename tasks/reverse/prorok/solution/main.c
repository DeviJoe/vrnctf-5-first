#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <wchar.h>
#include <locale.h>
#include <unistd.h>

char flag[] = "76726e6374667b3768335f35373472355f6b6e30775f345f6c30375f346e645f3472335f35316c336e377d";

int main() {
    printf("You met your old friend - Astrologist Mona Megistus.\n");
    printf("She offers to predict the future of each other by the stars.\n");
    sleep(1);
    printf(".\n");
    sleep(1);
    printf(".\n");
    sleep(1);
    printf(".\n");
    sleep(1);
    printf("- Hmm, in your future I see that you will succeed and all your dreams will come true!\n");
    l:
    printf("- Can you try to guess the RANDOM number that I guessed?\n");
    srand(time(NULL));
    int r = rand();
    int i;
    scanf("%d", &i);

    if (r == i) {
        char str[50];
        for (int i = 0, j = 0; j < strlen(flag); ++i, j += 2) {
            int val[1];
            sscanf(flag + j, "%2x", val);
            str[i] = val[0];
            str[i + 1] = '\0';
        }
        printf("\nYeah! Well done! Look, there is something in the sky: \n%s\n", str);
    } else {
        printf("- Nope(( Again? \n");
        goto l;
    }

    return 0;
}
