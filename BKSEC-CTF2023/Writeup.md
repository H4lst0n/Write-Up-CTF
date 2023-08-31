# Checker

- Đề bài cho ta 2 file đó là `main.lua` và `checker.lua`. Trong đó file main.lua chưa được biên dịch và file checker.lua đã được biên dịch.
- Đây là nội dung của file `main.lua`.

```
    local util = require "checker"
    -- local util = require("checker")

    io.write("Input flag: ")
    local flag = io.read("*l")
    if util.check(flag, "BKctf2023") then
    print("Correct!")
    else
    print("Wrong...")
    end

``` 

## Solution
- Ta sẽ sử dụng `unlua` để decompile lại file checker. Đây là nội dung file decompile.

```
local flag = {}
function flag.check(v2, v3)
  local v4 = true
  local v5 = string.lower(v3)
  local v6 = {
    46,
    106,
    119,
    140,
    105,
    195,
    195,
    219,
    180,
    116,
    151,
    68,
    191,
    86,
    169,
    205,
    195,
    211,
    107,
    120,
    110,
    129,
    160,
    189,
    189,
    189,
    194,
    164,
    102,
    110,
    123,
    111
  }
  local v7 = {
    219,
    117,
    231,
    96,
    201,
    195,
    228,
    201,
    255,
    228,
    195,
    252,
    219,
    234,
    213,
    138,
    138,
    138,
    96,
    240,
    228,
    207,
    195,
    249,
    207,
    96,
    261,
    195,
    219,
    252,
    99,
    30
  }
  if 32 ~= #v2 then
    v4 = false
  end
  for v8 = 1, #v7 do
    io.write(string.char(v7[v8] / 3))
  end
  for v9 = 1, #v2 do
    local v10 = v2:byte(v9) ~ v5:byte((v9 - 1) % #v5 + 1)
    if v9 > 1 then
      v10 = v10 + v2:byte(v9 - 1)
    end
    if v6[v9] ~= v10 then
      v4 = false
    end
  end
  return v4
end
return flag

```

- Ta sẽ chuyển sang python để dễ đọc.
```
def check(v2, v3):
    v4 = True
    v5 = v3.lower()
    v6 = [
        46, 106, 119, 140, 105, 195, 195, 219, 180, 116,
        151, 68, 191, 86, 169, 205, 195, 211, 107, 120,
        110, 129, 160, 189, 189, 189, 194, 164, 102,
        110, 123, 111
    ]
    v7 = [
        219, 117, 231, 96, 201, 195, 228, 201, 255,
        228, 195, 252, 219, 234, 213, 138, 138, 138,
        96, 240, 228, 207, 195, 249, 207, 96, 261,
        195, 219, 252, 99, 30
    ]
    
    if len(v2) != 32:
        v4 = False
    
    for v8 in v7:
        print(chr(v8 // 3), end="")
    print()
    
    for v9 in range(len(v2)):
        v10 = ord(v2[v9]) ^ ord(v5[(v9 - 1) % len(v5)])
        if v9 > 0:
            v10 = v10 + ord(v2[v9 - 1])
        if v6[v9] != v10:
            v4 = False
    
    return v4

```

- Đây là code solve.

```
v3 = "BKctf2023"
v5 = v3.lower()

v6 = [
        46, 106, 119, 140, 105, 195, 195, 219, 180, 116,
        151, 68, 191, 86, 169, 205, 195, 211, 107, 120,
        110, 129, 160, 189, 189, 189, 194, 164, 102,
        110, 123, 111
    ]
v7 = [
        219, 117, 231, 96, 201, 195, 228, 201, 255,
        228, 195, 252, 219, 234, 213, 138, 138, 138,
        96, 240, 228, 207, 195, 249, 207, 96, 261,
        195, 219, 252, 99, 30
    ]
for v8 in v7:
        print(chr(v8 // 3), end="")
print()

flag = [0] * 32
flag[0] = chr(v6[0] ^ ord(v5[0]))
print()
for v9 in range(1,32):
    x = v6[v9] - ord(flag[v9-1])
    flag[v9] =  chr(x^ ord(v5[v9 % len(v5)]) )
    
print("".join(flag))
```
## Flag

- Flag: `BKSEC{Lua_len_fl@g,Long_nang_lang_lang}`




# Reality

- Trong bài này có 1 số lệnh bị disassembly sau khi bypass qua ta sẽ nhận được đoạn code truyền vào 


```
char __usercall sub_401220@<al>(int a1@<edx>, const char *a2@<ecx>, int a3)
{
  char result; // al
  signed int v5; // esi
  int i; // ecx

  v5 = strlen(a2);
  for ( i = 0; i < a3; ++i )
  {
    result = a2[i % v5];
    *(_BYTE *)(i + a1) ^= result;
  }
  return result;
}
```

- Sau khi xử lý 1 số byte rác thì ta được đoạn code như sau:

```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v3; // ebx
  int v5[21]; // [esp+0h] [ebp-114h] BYREF
  int v6; // [esp+54h] [ebp-C0h] BYREF
  int v7; // [esp+58h] [ebp-BCh]
  char v8[5]; // [esp+5Ch] [ebp-B8h]
  char v9[40]; // [esp+61h] [ebp-B3h] BYREF
  char v10[8]; // [esp+89h] [ebp-8Bh] BYREF
  int v11; // [esp+94h] [ebp-80h]
  unsigned int i; // [esp+98h] [ebp-7Ch]
  char v13[100]; // [esp+9Ch] [ebp-78h] BYREF
  int *v14; // [esp+104h] [ebp-10h]
  int v15; // [esp+110h] [ebp-4h]
  int savedregs; // [esp+114h] [ebp+0h]

  v14 = v5;
  sub_401020("Input the flag: ", v5[0]);
  v15 = 0;
  v7 = 15;
  memset(v13, 0, sizeof(v13));
  if ( !sub_401050("%s", v13) )
    return 0;
  if ( v7 < 18 )
  {
    v6 = v7;
    sub_40468D(&v6, &_TI1H);
  }
  sub_401220(100);
  if ( !NtCurrentPeb()->BeingDebugged )
  {
    v8[0] = 0;
    v8[1] = 0;
    v8[2] = 0;
    v8[3] = 0;
    v8[4] = 6;
    qmemcpy(v9, "8&w0X~B*", 8);
    v9[8] = 127;
    v9[9] = 63;
    v9[10] = 41;
    v9[11] = 26;
    v9[12] = 33;
    v9[13] = 54;
    v9[14] = 55;
    v9[15] = 28;
    v9[16] = 85;
    v9[17] = 73;
    v9[18] = 18;
    v9[19] = 48;
    v9[20] = 120;
    v9[21] = 12;
    v9[22] = 40;
    v9[23] = 48;
    v9[24] = 48;
    v9[25] = 55;
    v9[26] = 28;
    v9[27] = 33;
    v9[28] = 18;
    v9[29] = 126;
    v9[30] = 82;
    v9[31] = 45;
    v9[32] = 38;
    v9[33] = 96;
    v9[34] = 26;
    v9[35] = 36;
    v9[36] = 45;
    v9[37] = 55;
    v9[38] = 114;
    v9[39] = 28;
    qmemcpy(v10, "EDC7,lz8", sizeof(v10));
    for ( i = 0; i < 0x35; ++i )
      byte_4218B0[i] = v8[i];
    goto LABEL_42;
  }
  if ( ((((v13[5] * v13[4]) >> 16) + 1) & (((v13[3] ^ v13[2]) << 16) * (2 * (v13[1] + v13[0]) + 1))) != 0 )
  {
    v5[5] = 0;
    return (int)&loc_401E12;
  }
  if ( ((((v13[11] * v13[10]) >> 16) + 1) & (((v13[9] ^ v13[8]) << 16) * (2 * (v13[7] + v13[6]) + 1))) != 0 )
  {
    v5[6] = 0;
    return (int)&loc_401E01;
  }
  if ( ((((v13[17] * v13[16]) >> 16) + 1) & (((v13[15] ^ v13[14]) << 16) * (2 * (v13[13] + v13[12]) + 1))) != 0 )
  {
    v5[7] = 0;
    return (int)&loc_401DF0;
  }
  if ( ((((v13[23] * v13[22]) >> 16) + 1) & (((v13[21] ^ v13[20]) << 16) * (2 * (v13[19] + v13[18]) + 1))) != 0 )
  {
    v5[8] = 0;
    return (int)&loc_401DDF;
  }
  if ( ((((v13[29] * v13[28]) >> 16) + 1) & (((v13[27] ^ v13[26]) << 16) * (2 * (v13[25] + v13[24]) + 1))) != 0 )
  {
    v5[9] = 0;
    return (int)&loc_401DCE;
  }
  if ( ((((v13[35] * v13[34]) >> 16) + 1) & (((v13[33] ^ v13[32]) << 16) * (2 * (v13[31] + v13[30]) + 1))) != 0 )
  {
    v5[10] = 0;
    return (int)&loc_401DBD;
  }
  if ( ((((v13[41] * v13[40]) >> 16) + 1) & (((v13[39] ^ v13[38]) << 16) * (2 * (v13[37] + v13[36]) + 1))) != 0 )
  {
    v5[11] = 0;
    return (int)&loc_401DAC;
  }
  if ( ((((v13[47] * v13[46]) >> 16) + 1) & (((v13[45] ^ v13[44]) << 16) * (2 * (v13[43] + v13[42]) + 1))) != 0 )
  {
    v5[12] = 0;
    return (int)&loc_401D9B;
  }
  if ( ((((v13[53] * v13[52]) >> 16) + 1) & (((v13[51] ^ v13[50]) << 16) * (2 * (v13[49] + v13[48]) + 1))) != 0 )
  {
    v5[13] = 0;
    return (int)&loc_401D87;
  }
  if ( ((((v13[59] * v13[58]) >> 16) + 1) & (((v13[57] ^ v13[56]) << 16) * (2 * (v13[55] + v13[54]) + 1))) != 0 )
  {
    v5[14] = 0;
    return (int)&loc_401D73;
  }
  if ( ((((v13[65] * v13[64]) >> 16) + 1) & (((v13[63] ^ v13[62]) << 16) * (2 * (v13[61] + v13[60]) + 1))) != 0 )
  {
    v5[15] = 0;
    return (int)&loc_401D5F;
  }
  if ( ((((v13[71] * v13[70]) >> 16) + 1) & (((v13[69] ^ v13[68]) << 16) * (2 * (v13[67] + v13[66]) + 1))) != 0 )
  {
    v5[16] = 0;
    return (int)&loc_401D4B;
  }
  if ( ((((v13[77] * v13[76]) >> 16) + 1) & (((v13[75] ^ v13[74]) << 16) * (2 * (v13[73] + v13[72]) + 1))) != 0 )
  {
    v5[17] = 0;
    return (int)&loc_401D37;
  }
  if ( ((((v13[83] * v13[82]) >> 16) + 1) & (((v13[81] ^ v13[80]) << 16) * (2 * (v13[79] + v13[78]) + 1))) != 0 )
  {
    v5[18] = 0;
    return (int)&loc_401D23;
  }
  if ( ((((v13[89] * v13[88]) >> 16) + 1) & (((v13[87] ^ v13[86]) << 16) * (2 * (v13[85] + v13[84]) + 1))) != 0 )
  {
    savedregs = 387840;
    ++*(_DWORD *)(v3 - 1869609788);
    v5[19] = 0;
    return (int)&loc_401D0F;
  }
  if ( ((((v13[95] * v13[94]) >> 16) + 1) & (((v13[93] ^ v13[92]) << 16) * (2 * (v13[91] + v13[90]) + 1))) == 0 )
  {
LABEL_42:
    v11 = 0;
    JUMPOUT(0x401C97);
  }
  v5[20] = 0;
  return (int)&loc_401CFB;
}
```


## Solution

- Script solve:
```
key = "BKSEECCCC!!!"
v7 = [0, 0, 0, 0, 6]
v8 = [0, 38, 119, 48, 88, 126, 66, 42, 127, 63, 41, 26, 33, 54, 55, 28, 85, 73, 18, 48, 120, 12, 40, 48, 48, 55, 28, 33, 18, 126, 82, 45, 38, 96, 26, 36, 45, 55, 114, 28]
v9 = [69, 68, 67, 55, 44, 108, 122, 56]

x = v7 + v8 + v9

v5 = len(key)
for i in range(len(x)):
    result_byte = ord(key[i % v5])
    x[i] ^= result_byte

result_string = ''.join(chr(byte) for byte in x)

print(result_string)

```

## Flag

```
BKSEC{e4sy_ch4ll_but_th3r3_must_b3_som3_ant1_debug??}
```