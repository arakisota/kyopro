import 'dart:io';
void main() {
  String abc = stdin.readLineSync();

  int is_marbles(String s) {
    int answer = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == "1") {
        answer += 1;
      }
    }
    return answer;
  }
  int answer = is_marbles(abc);
  print(answer);
}