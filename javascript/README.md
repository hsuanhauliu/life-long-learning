# Javascript
This notebook was written while following this [Youtube video](https://www.youtube.com/watch?v=PkZNo7MFNFg).

## What is JavaScript?
JavaScript is a programming language for the web. It is used to manipulate HTML and CSS, which are the two essential elements of a web page. Read more about Javascript [here](https://www.w3schools.com/whatis/whatis_js.asp).

## Installation
No installation is required. Most, if not all, modern search engines can run Javascript code.

## Basics
### Comment
```
// This is one way to do it

/*
This is another way to do it
*/
```

### Print (To Console)
Javascript's equivalent of print function is called console.log().
```
// This will print whatever string that is passed in on the console.
console.log("hello world");
```

### Variable Declaration
Javascript can determine a data type dynamically using the "var" keyword.
```
var myName = "Andy"
```

We can also declare variables with "let" and "const". Their types will also be determined at run time.
- let: create local variables that are only available in the scope that they are declared.
- const: create variables whose values cannot be changed once declared.

### Data Type
Javascript has data types such as undefined, null, boolean, string, symbol, number, object, etc.

#### Boolean
The boolean values in Javascript are lowercase.

#### String
We can declare strings using single or double quotation marks.
```
var s1 = 'this is valid';
var s2 = "this is also valid";
```

JS strings are immutable, which means the characters in a string cannot be changed once declared.
```
var s = 'something';
s[0] = 'a'  // this will cause an error
```

#### Array
Array behaves like Python list. It can contain data of different types.
```
var ourArray = ["the universe", 42];
var multiArray[["the world", 13], ["the earth", 32]];
```

#### :warning:Object
##### Declaration
One can declare a Javascript object like so.
```
var fruit = {
  1: 30,
  "name": "apple",
  "color": "red",
  "number": 5,
  "tags": ["healthy", "delicious"],
  "my description": "Eat one everyday, keep doctors away."
};
```
The strings on the left side of the colons are called properties (props for short), and the values on the right are our data.

##### Access Properties
To access properties of an object, we use dot notation. We can also use bracket notation as well. It is required if the property name is not of type string, or it has a space in it.
```
console.log(fruit[1]);    // prints 30
console.log(fruit.name);  // prints "apple"
console.log(fruit["my description"]);
```

##### Insertion & Deletion
We can add new properties to objects as well.
```
// insert new properties
fruit.recommended = true;
fruit[healthy] = true;

// delete properties
delete fruit[recommended];
delete fruit.healthy;
```

##### Others
```
// check if the object has the specified property
fruit.hasOwnProperty(recommended);
```

### Function
To declare a function it can be as easy as...
```
function hello() {
  console.log("Hello!")
}
```

## Advanced
### Equality Operator & Strict Equality Operator
There are two types of equality operators, and they are == and ===. The former will attempt to convert both data to the same type before comparing their values, whereas the latter does not.
```
3 == 3    // true
3 == '3'  // true
3 === 3   // true
3 === '3' // false
```

The respective inequality operators are != and !==.

### Something Weird...
Variable inside of the function becomes global if it is declared without any keywords

```
function test() {
  temp = 5;
}
test();
console.log(temp);  // this will print out 5
```

---
typeof is a keyword for determining the type of a variable. It will return a string when called.
```
temp = 5;
console.log(typeof temp); // this will print out "number".
```
