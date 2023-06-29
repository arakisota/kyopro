import 'dart:io';
void main() {
  String s = stdin.readLineSync();
  int calc_prices(String s) {
    int price = 700;
    for (int i = 0; i < 3; i++) {
      if (s[i] == 'o') {
        price += 100;
      }
    }
    return price;
  }

  print(calc_prices(s));
}