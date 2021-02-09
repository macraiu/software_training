#include <stdio.h>
#include <stdlib.h>

__uint8_t IsBigEndian();

int main () {

   printf("%d", IsBigEndian());

   return 0;
}


__uint8_t IsBigEndian()
{
   u_int16_t x = 1;
   u_int8_t *ptr = &x;
   return (*ptr == 0);
}