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

7. Objects
   - An object groups multiple values together
   - object는 {}로 묶어서 여러 요소를 담을 수 있다. {Property: value};
   - object.property에 새로운 요소를 담을 수 있다. 
   - delete object.property를 통해 property를 제거할 수 있다. 
   - object 를 통해서 group을 만들 수 있기 때문에 편리하다. 
   - object['property'] ''을 붙여줘야 한다. 특수문자가 들어간 경우 사용하기 위해서 
   - object inside object, function inside object === method
   - console도 object console.log는 function이다.
   - Built in object JSON JavaScript Object Notation use double quote ""
   - JSON 다른 language에서도 사용할 수 있다. 컴퓨터간 활용이 가능하다는 장점을 갖는다. 
   - convert JSON.strigify(); string형태로 바꾸는것  JSON.parse(); Js object 형태로 바꾸는 것 서로 바꿀수 있다. 
   - localStorage 새로고침하면 모든게 리셋되는데 localStorage를 이용하면 결과가 저장된다. localStorage.setItem('string', 'string')  only support string localStorage에 string형태로 저장한 다음 reset되도 가져올 수 있도록 만든다. variable을 string형태로 넣기 위해서 JSON.stringify()를 쓰고 localStorage.getItem()으로 가져온다음 JSON.parse로 다시 string을 object형태로 바꿀수 있도록 한다. 
   - reset을 하면 localStorage에 있던 것들도 없어져서 null값이 되므로 null값을 받았을때 값을 조건문으로 넣어주어야 한다. 
   - null vs undefined null = empty  undefined default
   - Auto-boxing method :   length, toUpperCase()   string to special object로 number boolean
   - object reference 위치를 가리키다.   = reference를 가리키므로 copy by reference
   - const 만들었지만 object 는 reference이므로 새로운 값을 가르키도록 할 수 있다. 
   - object는 직접 비교할 수 없다 reference이므로 value를 직접 가지는게 아니므로 object1 === object3 ; 는 False로 나온다 
   -  shortcut destructuring : const message = object4.message; const { message } = object4;
   -  short hand : const가 같다면 variable을 그대로 쓸 수 있다. method 바로 function을 넣을수 있다. 

8. Documene Object Model(DOM)
   -  document.body.innerHTML property가 webpage를 바꾸다. 
   -  document.title 로 title도 바꿀수 있다. document는 web과 연결된것 DOM 이라고 부른다. 
   -  document.body  HTML element inside JavaScript   document.body 는 object로 취급 innerHTML은 property이므로 HTML을 바꿀수 있다. JS에서 innerHTML을 수정하는것으로도 HTML의 내용을 바꿀수 있다. 새로운 HTML을 넣을 수 있다. 
   -  document.querySelector() element를 가져온다 button을 가져오면 HTML의 첫번째 button을 JavaScript로 가져온다.
   -  innerHTML property를 수정하면 또 바꿀 수 있다. 
   -  첫번째만 가져오기 때문에 class를 설정해주면 된다.  '.'으로 시작하면 element가 아닌 class를 기준으로 찾는다. 
   -  innerText를 가져오면 좌우 space를 제외하고 가져온다.
   -  HTML과 JS를 clear code로 짜기 위해서는 js를 function으로 바꾸어 준다.
   -  paragraph는 한 block을 차지한다. 
   -  placeholder 빈 상자에 기본입력값  inputElement는 HTML이 안쓰이기 때문에 innerHTML을 안쓴다.
   -  input으로 넣고 바로 계산하도록 만들려면 onkeydown을 사용한다. event는 key가 입력될때마다 발생한다. 
   -  Number() 숫자로 바꿔준다. string이 number로만 구성되어있다면 알아서 number로 바꿔준다. 단 +일경우에는  string으로 더해버린다 따라서 JS에서 math를 하지 말것

9. HTML, CSS, and JavaScript Together
   - CSS Selector 어떤 element에 style을 넣을것인가. button class를 정할수 있다 여러개의 class를 넣을수 있어서 js에서 사용할 class와 CSS에서 사용할 class를 다르게 설정하였다. 
   - CSS property: value ; 
   - JS 로 HTML의 변화에 따라서 다른 CSS를 적용하고 싶으면 class를 다르게 만들어야 하는데 classList라는 object를 사용한다. add class 형태, class를 삭제하려면 classList.remove('class')를 사용해서 만들었던 class를 삭제할 수 있다. 
   - script연결할때는 <scripts src=""> css연결할때는 <link rel="" href="">