#include <iostream>
#include <string>


std::string encrypt_decrypt(std::string text, std::string key) {
  std::string result = "";
  for (int i = 0; i < text.length(); i++) {
    result += text[i] ^ key[i % key.length()];
  }
  return result;
}

int main() {
  std::string text, get_text;
  std::string key, get_key;
  std::cout << "Enter text to encrypt: ";
  getline(std::cin, text);
  std::cout << "Enter key: ";
  std::cin >> key;
  std::string encrypted = encrypt_decrypt(text, key);
  std::cout << "Encrypted text: " << encrypted << std::endl;
  std::cout << "Enter text to decrypt: ";
  std::cin >> get_text;
  std::cout << "Enter key to decrypt: ";
  std::cin >> get_key;
  std::string decrypted = encrypt_decrypt(get_text, get_key);
  std::cout << "Decrypted text: " << decrypted << std::endl;
  return 0;
}
