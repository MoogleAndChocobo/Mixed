# Java Language

## simple program

> public    访问修饰符
> static    关键字
> void  返回类型
> String    String类
> args  字符串数组

## keyword

> access control `private,protected,public,default`
> class,method,variable modifier `abstract,class,extends,final,implements,interface,native,new,static,strictfp,synchoronized,transient,volatile`
> program control statement `break,case,continue,default,do,else,for,if,instanceof,return,switch,while`
> error handling `assert,catch,finally,throw,throw,try`
> package `import,package`
> basic types `boolean,byte,char,double,float,int,long,short`
> variable references `super,this,void`
> reserved keywords `goto,const`

## 继承

被继承的类称为超类(super class),派生类称为子类(sub class)

## 接口

在Java中,接口可理解为对象间相互通信的协议,接口在继承中扮演着很重要的角色,接口只定义派生要用到的方法,但是方法的具体实现完全取决于派生类

## Java支持以下基本概念

多态,继承,封装,抽象,类,对象,实例,方法,重载

## 变量

1. 局部变量:在方法,构造方法或者语句块中定义的变量被称为局部变量.变量声明和初始化都是在方法中,方法结束后,变量就会自动销毁;
2. 成员变量:成员变量是定义在类中,方法体之外的变量.这种变量在创建对象对象的时候实例化.成员变量可以被类中方法,构造方法和特定类的语句块访问.
3. 类变量:类变量也声明在类中,方法体之外,但必须声明为static类型.
