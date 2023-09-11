#include <iostream>
#include <fstream>
#include <cstdlib>

__int64 __fastcall decode_instruction(std::ifstream& file)
{
  char buffer[4];
  file.read(buffer, 4); // Đọc 4 byte từ tệp vào buffer
  if (!file) {
    // Xử lý lỗi nếu có
    std::cerr << "Lỗi đọc tệp.\n";
    exit(1);
  }
  return 0LL;
}

int main() {
    const char* filename = "ok.smol";
    std::ifstream file(filename, std::ios::binary);
    
    if (!file.is_open()) {
        std::cerr << "Không thể mở tệp " << filename << "\n";
        return 1;
    }

    while (true) {
        decode_instruction(file);
    }

    file.close();
    return 0;
}
