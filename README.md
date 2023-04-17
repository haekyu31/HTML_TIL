# HTML 
----------------
# JS JavaScript Full Course(2023)
google 에 검색 또는 chatGPT 에 검색
1. Number and Math
   1. JS에서 float로 계산하면 오류가 할생할 때가 존재한다.  ex 0.1 + 0.2 -> 0.30000000004 int형태로 바꾼다음 divide
   2. JS %를 계산할때 바로 곱하면 안된다. 
   3. Math.round() 반올림 형태

2. Strings
   1. typeof string 또는 number  string + number = string  
   ```js
   '$' + 20.95 + 7.99 '$20.957.99 '$'를 string처리해서 다음 오는것도 전부 string으로 처리한다.

   '$' + (20.95 + 7.99)
   '$28.939999999999998'

    <!-- 소수점 문제가 생길경우 -->
   '$' + (20.95 + 7.99) / 100
   '$28.94'  
   <!-- string으로 계산을 막기 위해서 -->
   'Items (' + 1 + 1  
   'Items (' + (1 + 1  ) + '): $' + (2095 + 799) / 100
    'Items (2): $28.94'
   ```
   2. string에는 single quotes'', double quotes"" backticks `` template strings interpolation
    ```js
    <!-- ${}  insert value directly into string-->
    `Items (${1 + 1}): $${(2095 + 799) / 100}`
    <!-- 간단하게 정리 되었다. -->
    ```
   3. escape \', \" \n new line
   4. multi line string
   ```js
   `some
    text`
    'some\ntext'
    ```
    use single quote defalut need interpolation, multi-line strings use backtick 
3. HTML CSS JavaScript review script run first , onclick run after comment // /* */ multi-line comment console.log(); console창에 결과를 보내는 방식 js를 확인하는 방법 
4. 