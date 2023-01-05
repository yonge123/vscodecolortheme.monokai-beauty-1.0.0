
/**
 * @description  a javascript sample code
 */


class User {
    constructor(name, id, age){
      this.name = name;
      this.id = id;
      this.age = age;
    }
}


let user1 = new User('user1', 1, 12);

console.log(user1.name)
console.log(user1.id)
console.log(user1.age)

