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
3. HTML CSS JavaScript review 
   1. script run first , onclick run after comment // /* */ multi-line comment console.log(); console창에 결과를 보내는 방식 js를 확인하는 방법 

4. variable 
   1. let variable = ; variable을 지정하는 방식 let create new value
   2. Can't use let ,Can't start with a number, special caharacters except $, _
   3. semi colon  = end of an instruction
   4. let을 사용하고 re assigning 할때는 let을 사용하지 않는다. 
   5. a += 1 python 과 같은 방식으로 작동한다. 
   6. backtick 과 함께 사용해서 variable을 넣을 수 있다. 
   7. ++는 +1 과 같다.
   8. JS는 camelCase를 사용한다.

5. booleans
   1. js에서 == 는 같은 타입으로 바꾼다음 비교한다 정확한 type비교까지 하기 위해서는 =을 하나 더 붙인다. === , !==
   2. if statement if (true) {console.log('hello');}
   3. if(){console.log() }else{ console.log()} if else 형식 {} 에 들어가는가 안들어가는가 형태로 
   4. if (condition){ branches} else {optional}
   5. branch에 한가지만 나올경우 {}을 안써도 되지만 두가지 이상이 나올경우 {}을 넣어줘야 한다. 
   6. else if 형태로 조건문을 중첩해서 넣을 수 있다. 
   7. && and operator || or operator  ! not operator
   8. Strategy for JavaScript Figure out what steps we need, Convert these steps into code
   9. Falsy value :  false,  0,  '',  NaN,  undefined , null
   10. true ? 'truthy' : 'falsy' shortcut
   11. guard operator && let message; if (condition){ message = 'hello';}
   12. default operator

6. Function
   - function function(){} reuse code 반복해서 사용할 수 있도록 script를 수정해서 사용
   - Return Statement 값을 function에서 내보내는 기능 return 으로 function이 끝난다. 
   - parameter variable과 같은 기능을 한다. default value
   - 반복되는요소는 함수로 바꾸어서 scripts에 쓰면 아주 편하다.