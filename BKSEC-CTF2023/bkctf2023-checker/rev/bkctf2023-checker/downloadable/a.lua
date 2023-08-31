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
