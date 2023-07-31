# Hard 2 (2 coin)

- Some Tech reverse in AdworldCTF.

## BABYRE (patchbyte)

![img](/AdworldCTF/Hard2/BABYRE-(patchbyte)SOLVED/start.png)

- Bắt đầu vào chương trình với ida64 sau khi đọc qua code hàm main. Ta nhận thấy chương trình sẽ cho chúng ta nhập vào 14 byte tương ứng với flag và gọi hàm `judge(s)` với biến `s` ta sẽ đi đến hàm này để xem chương trình sẽ làm gì.

![img](/AdworldCTF/Hard2/BABYRE-(patchbyte)SOLVED/judge.png)

- Nhảy đến đây thì thật bất ngờ ở đây toàn bộ là các giá trị của mảng trong khi code ở đây là truyền vào hàm judge() 1 chuỗi. Sau khi tìm hiểu thì nhớ tới ngôn ngữ C hình như có kỹ xảo thông qua khâu chuỗi tạo ra mệnh lệnh mới.  Vì vậy, ở đây (*(unsigned int (__fastcall **)(char *))judge)(input_flag) nên được phân tích như vậy, unsigned int là loại trả về của hàm judge, (__fastcall **) là quy ước gọi của hàm, (char *) đây chỉ là một chuỗi chuỗi trích xuất các tiêu đề mảng của judge làm tên hàm.

- Tôi sẽ sử dụng 1 script để path lại đống byte đã bị xử lý trước đó vì trước khi nhập flag như đề bài yêu cầu có 1 đoạn đã decode các byte của judge().

```
  for ( i = 0; i <= 181; ++i )
    judge[i] ^= 0xCu;
  printf("Please input flag:");
```
- Đây là đoạn script của tôi để patch byte.

```
st = 0x600b00
for i in range(182):
    patch_byte(st + i, ord(get_bytes(st + i, 1))^0xC)
    
```

![img](/AdworldCTF/Hard2/BABYRE-(patchbyte)SOLVED/patch.png)

- Sau khi patch xong các giá trị đã được trở lại y nguyên ban đầu. 
- Nhấn `c` để makecode. Sau khi makecode xong ta sẽ được đoạn code như sau:

![img](/AdworldCTF/Hard2/BABYRE-(patchbyte)SOLVED/makecode.png)

- Nhấn `p` để makefunc. Sau khi makefunc ta có thể dễ dàng sủ dụng func ở function name.

![img](/AdworldCTF/Hard2/BABYRE-(patchbyte)SOLVED/makefunc.png)

- Từ đây ta có thể dễ dàng reverse lại để tìm ra flag.

```
#include <bits/stdc++.h>
using namespace std;

int main(){
    char v2[100];
    v2[0] = 'f';
    v2[1] = 'm';
    v2[2] = 'c';
    v2[3] = 'd';
    v2[4] = 127;
    char v3[10] = "k7d;V`;np";
    int i;
    for (i = 0; i < strlen(v2); ++i )
        v2[i] ^= i;
    
    for(int j = 0; j < strlen(v3); i++, j++)
        v3[j] ^= i;

    cout << v2 << v3;
    
    return 0;
}
```

### Flag: `flag{n1c3_j0b}`
