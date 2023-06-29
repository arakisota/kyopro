import "dart:io";

void main() {
  String date = stdin.readLineSync();
  String modify_date(String date){
    String answer = "2018";
    answer += date.substring(4);
    return answer;
  }
  print(modify_date(date));
}